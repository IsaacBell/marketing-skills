---
name: markdown-blog
description: "Add a markdown blog to an existing static site with Hugo, served under /blog on the main domain, with no CMS, database or account. Use when the user wants a blog on a static or hand-written site, mentions Hugo, 'blog on my domain', 'markdown posts', or is choosing between a headless CMS and a static generator. Covers layout, URL style, canonical and sitemap, the Vercel project and rewrite, mise tasks, and the publish routine."
---

# Markdown Blog (Hugo)

Posts are markdown files with frontmatter. Hugo turns them into static HTML at deploy time. Nothing runs when a visitor opens a page. No CMS, no database, no account.

## When to choose this

- One author, or a few technical authors, publishing evergreen posts.
- The main site is static HTML with no build step.
- Do not choose it if several non-technical editors need an admin UI, drafts and scheduling. A headless CMS fits that; it also needs a framework, a database and file storage, which is real cost.

Prefer the same domain (`/blog`) over a separate blog domain. Authority stays on one site and posts link straight to the service pages.

## Structure

```
blog/                         # its own project folder
  hugo.toml
  vercel.json
  mise.toml
  content/blog/_index.md
  content/blog/<slug>.md
  layouts/_default/{baseof,list,single}.html
  layouts/partials/url.html
  layouts/sitemap.xml
  layouts/index.html          # noindex redirect to /blog
```

No theme. A theme adds a dependency and a design to fight. Write three small templates on the main site's stylesheet.

## Decisions that matter

- **Separate Vercel project, rewritten under `/blog`.** The main site has no build step and serves its whole folder. Mixing a Hugo build in forces a copy-and-delete step to keep the source files from being served. A second project, with rewrites in the main site's `vercel.json`, isolates it. Rewrites go above any catch-all:
  - `/blog/sitemap.xml` to `https://<project>.vercel.app/sitemap.xml`
  - `/blog` to `https://<project>.vercel.app/blog`
  - `/blog/:path*` to `https://<project>.vercel.app/blog/:path*`
- **`uglyURLs = true`.** Posts build to `blog/slug.html`, and `cleanUrls` serves them at `/blog/slug` with no trailing slash. Default Hugo output (`slug/index.html`) fights a no-trailing-slash site and can loop under rewrites.
- **One URL partial.** `.Permalink | replaceRE `(/index)?\.html$` "" | replaceRE `/$` ""`. Use it for the canonical tag, `og:url`, sitemap and links. Without it the section page becomes `/blog/index`.
- **Custom sitemap template** (`layouts/sitemap.xml`) that lists only the blog section using that partial. Emit the XML declaration through `printf ... | safeHTML`; Go templates escape `<?`.
- **Load the main site's CSS and font by absolute URL** (`https://<main-domain>/assets/site.css`) so the blog cannot drift. A relative `/assets/...` works only behind the main domain's rewrite. On the blog project's own URL, on every preview and under `hugo server`, it returns 404 and the page renders unstyled with no font. The font file needs `access-control-allow-origin: *` on the main site for the cross-origin load; check it with `curl -I`. Behind the main domain the absolute URL is same-origin, so nothing is lost.
- **Disable RSS, taxonomies and terms** unless wanted. RSS permalinks carry `.html` and disagree with the canonical URLs.
- **Base URL is the public domain**, not the `.vercel.app` address. Canonical tags then point away from the project's own URL.

## Frontmatter

```
---
title: "Quoted, because titles often contain a colon"
description: "One sentence, under about 155 characters."
slug: url-slug
date: 2026-01-01
---
```

Quote `title` and `description`. An unquoted `: ` breaks YAML and will break Hugo or Astro later. Hugo skips future-dated posts by default.

## Tooling with mise

```
[tools]
hugo = "<pinned version>"

[tasks.dev]     run = "hugo server"
[tasks.build]   run = "hugo --gc --minify"
[tasks.deploy]  depends = ["build"]; run = "vercel deploy --prod --yes"
```

Pin the same Hugo version in `vercel.json` under `build.env.HUGO_VERSION`. Confirm the deploy platform can install that version before trusting the pin.

## Writing posts

Before drafting, read up to two comparable pieces in the same publication and adopt their structure, tone, and conventions. Check whether the topic already lives somewhere; extend the owning page rather than starting a rival one beside it. A heading states the finding, and the first sentence under it never repeats the heading.

### Diagram source

Commit the diagram source (PlantUML, Mermaid, or the text format the build reads) and render it in the build; never paste a screenshot as the only copy. A picture with no source cannot be diffed, so nobody maintains it, and a stale render misleads. Delete the old render in the same change that updates the source.

### Copy-pasteable commands

Every command in a post is copy-pasteable as written, with concrete example values. Label variants inside the code block with a comment, for example a read-only form and a form that writes to production, so a reader cannot pick the destructive one by accident.

## Publish routine

1. Add `content/blog/<slug>.md`.
2. `mise run build`; open the built page and check title, canonical, and that tables and code blocks rendered.
3. `mise run deploy`, then deploy the main site if its files changed.
4. Add the post to the main site's `llms.txt`. The blog index and sitemap update themselves.
5. Ping IndexNow for the new URLs. The ping script must read the blog sitemap as well as the main one.
6. Submit the blog sitemap once in Search Console and Bing Webmaster Tools, and list it in `robots.txt`.

## Verify

- `curl -s -o /dev/null -w '%{http_code}' https://<project>.vercel.app/blog/<slug>` returns 200.
- After the main site deploys, the same path on the main domain returns 200 and its canonical is the main-domain URL.
- Sitemap URLs have no `.html` and no trailing slash.
- Preview deployments are often behind the host's login (Vercel Authentication answers 302). Check them with the host's own authenticated fetch (`vercel curl <path> --deployment <url>`), not plain `curl`. The production alias is public, and the main site's rewrite needs it public.
- Run an accessibility scan (axe-core over the index and every post, three widths, light and dark) before the first deploy and after any change to the base template. Reading the CSS misses what a scan finds: unstyled links fall back to browser blue and fail contrast on a dark theme.
- Every post has a line in `llms.txt` with the post's own description. The two are written by hand in two places, so check them with a small script that compares the frontmatter against the file, and run it on deploy. A site that adds posts for months without this check ends up with new posts missing.
- Open the live page after deploying. Look for a loaded font (`document.fonts`), the link colour, and anything peeking in at the viewport edge.

## Maintaining posts

Update a post in the same change as the thing it describes; documentation is part of done, not a follow-up task. When a post is superseded, add a short banner naming what replaced it and where the current version lives, rather than deleting it. When a fact changes, sweep every page that states it and scope the sweep so it does not become a rewrite.

## Examples

Frontmatter.

Bad. A colon followed by a space is YAML syntax, so this title breaks the parse in Hugo and in Astro:

```
title: Bing Webmaster Tools: import your site in two minutes
```

Good:

```
title: "Bing Webmaster Tools: import your site in two minutes"
description: "Why a new site needs Bing as well as Google, and how to import from Search Console."
```

Config.

Bad. Hugo 0.167 warns on the old key: `project config key languageCode was deprecated in Hugo v0.158.0 and will be removed in a future release. Use locale instead.`

```
languageCode = "en-us"
```

Good:

```
locale = "en-us"
```

Sitemap output.

Bad. Two faults in one file, both real. The XML declaration is HTML-escaped, and the section page is listed as `/blog/index`:

```
&lt;?xml version="1.0" encoding="UTF-8"?><urlset ...><url><loc>https://example.com/blog/index</loc>
```

Good. Emit the declaration through `printf ... | safeHTML`, and trim `/index.html` in the URL partial:

```
<?xml version="1.0" encoding="UTF-8"?><urlset ...><url><loc>https://example.com/blog</loc>
```

URL shape.

Bad. Default Hugo output puts each post at `slug/index.html`, which fights a no-trailing-slash site and can loop behind a rewrite.

Good. `uglyURLs = true` builds `blog/slug.html`, and the host's clean-URL setting serves `/blog/slug`.

Build proof.

Good. A clean build prints no warnings, lists every post plus the index, the redirect page and the sitemap, and the built pages carry a canonical tag on the public domain:

```
public/blog/index.html
public/blog/<slug>.html   (one per post)
public/index.html         (noindex redirect to /blog)
public/sitemap.xml
<link rel=canonical href=https://example.com/blog/<slug>>
```

## Related

- `website-launch`: the checks a new blog must also pass.
- `search-indexing`: IndexNow wiring.
