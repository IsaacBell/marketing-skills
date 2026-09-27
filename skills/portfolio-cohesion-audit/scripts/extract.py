"""Crawl a site's homepage + first-party nav pages; emit compact SEO/identity signals as JSON."""
import json, re, sys, urllib.request, urllib.parse
from html.parser import HTMLParser

UA = "Mozilla/5.0 (compatible; audit/1.0)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.geturl(), dict(r.headers), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, url, dict(e.headers or {}), ""
    except Exception as e:
        return 0, url, {}, f"ERR {e}"


class P(HTMLParser):
    def __init__(s):
        super().__init__()
        s.title = ""; s.meta = {}; s.links = []; s.canon = None; s.h = []; s.ld = []
        s.imgs_noalt = 0; s.imgs = 0; s.lang = None; s.text = []
        s._in = None; s._buf = ""; s._skip = 0

    def handle_starttag(s, t, a):
        a = dict(a)
        if t == "html": s.lang = a.get("lang")
        if t == "meta":
            k = a.get("name") or a.get("property")
            if k: s.meta[k.lower()] = a.get("content", "")
        if t == "link" and "canonical" in (a.get("rel") or ""): s.canon = a.get("href")
        if t == "a" and a.get("href"): s.links.append(a["href"])
        if t == "img":
            s.imgs += 1
            if not a.get("alt"): s.imgs_noalt += 1
        if t in ("title", "h1", "h2") or (t == "script" and a.get("type") == "application/ld+json"):
            s._in = t if t != "script" else "ld"; s._buf = ""
        elif t in ("script", "style", "noscript"): s._skip += 1

    def handle_endtag(s, t):
        if s._in and (t == s._in or (s._in == "ld" and t == "script")):
            v = re.sub(r"\s+", " ", s._buf).strip()
            if s._in == "title": s.title = v
            elif s._in == "ld": s.ld.append(v)
            else: s.h.append(f"{s._in}: {v[:120]}")
            s._in = None
        elif t in ("script", "style", "noscript") and s._skip: s._skip -= 1

    def handle_data(s, d):
        if s._in: s._buf += d
        elif not s._skip: s.text.append(d)


def ld_summary(raw):
    out = []
    for r in raw:
        try:
            j = json.loads(r)
        except Exception:
            out.append("INVALID JSON-LD"); continue
        items = j.get("@graph", [j]) if isinstance(j, dict) else j
        for it in items:
            if isinstance(it, dict):
                out.append({k: it.get(k) for k in ("@type", "@id", "name", "url", "sameAs", "jobTitle", "founder", "priceRange", "worksFor", "description") if it.get(k)})
    return out


def page(url):
    st, final, hdr, body = fetch(url)
    p = P(); p.feed(body)
    text = re.sub(r"\s+", " ", " ".join(p.text)).strip()
    host = urllib.parse.urlparse(final).netloc
    internal, external = set(), set()
    for l in p.links:
        u = urllib.parse.urljoin(final, l.split("#")[0])
        n = urllib.parse.urlparse(u)
        if n.scheme not in ("http", "https"): continue
        (internal if n.netloc == host else external).add(u)
    return {
        "url": url, "status": st, "final": final, "lang": p.lang, "title": p.title,
        "desc": p.meta.get("description"), "canonical": p.canon, "robots_meta": p.meta.get("robots"),
        "og": {k: v for k, v in p.meta.items() if k.startswith(("og:", "twitter:"))},
        "headings": p.h[:12], "jsonld": ld_summary(p.ld), "words": len(text.split()),
        "imgs": p.imgs, "imgs_noalt": p.imgs_noalt, "external_links": sorted(external),
        "internal_links": sorted(internal), "text": text[:5000],
        "x_robots": hdr.get("X-Robots-Tag") or hdr.get("x-robots-tag"),
    }


def site(root, maxpages=8):
    home = page(root)
    base = home["final"]
    extra = {}
    for f in ("robots.txt", "sitemap.xml", "llms.txt"):
        st, _, _, b = fetch(urllib.parse.urljoin(base, "/" + f))
        extra[f] = {"status": st, "head": b[:800] if st == 200 else ""}
    pages = [home]
    for u in [u for u in home["internal_links"] if u.rstrip("/") != base.rstrip("/")][: maxpages - 1]:
        pages.append(page(u))
    return {"root": root, "files": extra, "pages": pages}


if __name__ == "__main__":
    print(json.dumps(site(sys.argv[1]), indent=1))
