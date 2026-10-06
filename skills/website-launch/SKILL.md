---
name: website-launch
description: "Plan, run, or audit the launch of a small-business website, in order: decisions, build checks, domain and hosting, search indexing (Google and Bing), AI search visibility, keeping prices and claims in sync, launch day, and the first 30 days. Use when the user mentions launching or relaunching a site, a launch checklist, 'is my site indexed', 'why am I not on Google', or a go-live review. Orchestrates search-indexing, ai-agent-visibility and seo-audit rather than repeating them."
---

# Website Launch

A live site is not a found site. This skill is the whole launch in one ordered pass. Every item is something you can check and pass or fail. Facts were checked on 2026-09-29. Crawler names, product names and Search Console screens change, so recheck anything time-sensitive against the vendor's own page before relying on it.

## Required inputs

- The domain, and the chosen address (`www` or plain). Ask; do not guess.
- The page list, including tool pages and sub-apps.
- A facts sheet: business name, prices, services, area, hours, phone, email.
- Who controls DNS and hosting.

If the facts sheet does not exist, create it first. Every later check compares against it.

## Method

Work the phases in order. For each item: run the check, record pass or fail, apply the fix, run the check again. Report what was verified and what was not.

### 1. Decide first

- Domain registrar account is owned by the client, not the developer. Fix: client creates the account; the developer starts a transfer.
- One address chosen and written down. Using both splits ranking.
- Facts sheet, page list, one action per page, dated launch plan.

### 2. Build

- Real text is in the HTML the server sends: `curl -s URL | grep "a sentence from the page"`. If missing, the page is built in the browser; ask for server rendering or static generation.
- Every page has its own title (under 60 characters) and description (under 155).
- Every page is linked from the menu or footer, tool pages and sub-apps included. Orphans are not crawled.
- Contact form: submit from a phone, message reaches the inbox, not spam.
- Form options changed: the server-side allow-list changed too. Test a submission with each new option. Forms and servers keep separate lists, and a mismatch drops real messages silently.
- Mobile check on a real phone; PageSpeed Insights not red on the homepage and one deep page.
- Privacy policy linked in the footer if data is collected.

### 3. Domain and hosting

- All four versions (`http`/`https`, `www`/plain) end on the chosen address with one permanent redirect: `curl -sI URL` shows `301` and a `location:` line.
- The canonical tag on every page equals the chosen address exactly, including scheme and trailing-slash style.
- Padlock on every page; no mixed content.
- Private files are not served. Each returns 404: `/.env`, `/.git/config`, `/package.json`, `/scripts/`. Fix with the host's ignore file (`.vercelignore` on Vercel), redeploy, recheck. If one was exposed, rotate every secret in it.
- No `noindex` in the live HTML or in an `X-Robots-Tag` header. Test and preview builds often ship it.
- SPF, DKIM and DMARC pass: send to a Gmail address, "Show original", three PASS.
- Relaunch only: each old address redirects to its matching new page, not the homepage.

### 4. Get indexed

- Day one: search `site:yourdomain.com` in Google and Bing. Nothing is normal on a new site; it is the baseline.
- Google Search Console: Domain property verified by DNS TXT record, which survives redesigns.
- `sitemap.xml` opens, lists every page from the page list with canonical URLs only, and is submitted in Search Console (status Success).
- `robots.txt` opens, has no lone `Disallow: /`, and ends with a `Sitemap:` line.
- Request indexing for the five key pages (daily quota applies).
- Bing Webmaster Tools: import from Search Console. Bing's index feeds ChatGPT search and Copilot.
- IndexNow: key file at the site root opens; ping after every deploy. Bing and other engines use it; Google does not. See `search-indexing`.
- Days 7, 14 and 30: repeat `site:`; read the Search Console Pages report and act on each "not indexed" reason.

### 5. AI search visibility

- `robots.txt` names AI crawlers explicitly. Separate the search bots from the training bots and decide per bot. See `ai-agent-visibility`.
- `llms.txt` at the root: name, one-line summary, services with prices, key links, contact. Facts only. Not every AI tool reads it.
- A host or CDN firewall does not block the search bots. Get written confirmation, or test with a crawler user agent.
- Prices, area and top questions are plain page text, not only images, PDFs or pop-ups.
- Days 7 and 30: ask ChatGPT, Perplexity and Copilot about the business by name; log the answers; trace each wrong fact to its source.

### 6. Keep everything in sync

- A price or claim lives in page text, page description, structured data, `llms.txt` and the share image. After any change, search the whole project for the old value and replace every match.
- Structured data passes Google's Rich Results Test and matches the facts sheet.
- Share image matches the current headline. Platforms cache the first image; use their debug tools to refresh.
- Every new page, the same day: menu link, sitemap entry, IndexNow ping, `llms.txt` line, unique title and description.
- Tool pages and sub-apps are in the sitemap, linked, and share the main footer.
- Zero broken links from the menu, footer and buttons.
- Business name, address and phone are spelled identically on the site, the Google profile and every directory.

### 7. Launch day and the first 30 days

- Freeze prices and copy; run the sync check.
- Ten-minute test: the four addresses, padlock, form, `site:`, sitemap, robots.txt, the private-file paths.
- Analytics real-time view shows a phone visit and a test conversion.
- Uptime monitor on; domain and hosting renewals on a calendar someone reads.
- One-page "where everything lives": who holds each account and login. Take a full backup.
- Google Business Profile claimed and verified (can take days); details match the facts sheet.
- Ask 3 to 5 clients for reviews with a direct link. Ask every client, not only happy ones. Never buy reviews.
- Claim Bing Places, Apple Business Connect and the directories the customers use, with matching details.
- Four weekly 15-minute checks: Search Console, Bing, a test form submission, the AI questions. On day 30, compare with day one.

## Output format

- A pass/fail table per phase, with the exact command or URL used for each check.
- The fix for each failure, written as one plain step.
- What was not verified, and why.

## Writing the version for a site owner

Owners are not developers. Keep each check under about 15 words, name where to look and what a pass looks like, and put commands in a developer note, not the check.

## Examples

Owner-facing check.

Bad, and rejected in review: "Own your domain account and login, not your developer or agency." The reader cannot tell where to look or what a pass is.

Good:

```
- [ ] **Your domain account is under your email, not your developer's.**
  - *Why:* If they vanish, you can't renew it or change where it points. *Fix:* Make your own registrar account and ask them to transfer the domain to it.
```

Length.

Bad, about 50 words, with a keyboard shortcut and a paragraph of explanation: "Open your homepage, right-click, choose View Page Source, press Ctrl+F (Cmd+F on Mac) and search for a sentence from the page. Some sites only build their text after the page loads. You see the text, but search engines and AI tools can receive an empty page."

Good, 14 words for the check, the rest in why and fix:

```
- [ ] **Search View Page Source (Ctrl+F) for a sentence from your homepage. It's there.**
  - *Why:* Some sites build their text after loading, so search engines and AI tools see a blank page. *Fix:* Make sure the page text is rendered on the server.
```

Commands in an owner-facing fix. Bad: "Check with `curl -sI http://www.yourdomain.com`: you should see `301` and a `location:` line." Good: "Make sure every other version of the address redirects permanently to [chosen address]." Keep the command out of an owner-facing check.

Audit report.

Bad: "SEO looks fine and the site seems fast."

Good, every row has evidence:

```
| Check                          | Result | Evidence                                    |
| Home meta description          | FAIL   | 183 characters, limit 160                    |
| Sitemap lists /services        | pass   | https://example.com/services in sitemap.xml  |
| Private files not served       | FAIL   | /config.yml returns 200, expected 404        |
| Contrast, secondary text       | FAIL   | 4.49:1 on the darker panel, minimum 4.5      |
```

Fictional example: findings from one launch, each caught by a scripted check and not by eye:

- Two meta descriptions ran over the length limit. Google truncates near 160 characters.
- A build file was about to be served publicly by the host. Fix: add it to the ignore file, and make the check assert the ignore entries.
- Secondary text sat just under the AA contrast bar.
- A blog section appeared as `/blog/index` in the sitemap instead of `/blog`.
- A slogan repeated on every page. Once per page reads as confidence; everywhere reads as a slogan.

## Related

- `search-indexing`: IndexNow setup and wiring.
- `ai-agent-visibility`: robots.txt, sitemap.xml, llms.txt from scratch.
- `seo-audit`: broader crawl and on-page audit.
- `markdown-blog`: publishing posts that support the launch.
