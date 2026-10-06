---
name: wordpress-mcp-site-ops
description: Safely change copy and SEO on a live WordPress site through an MCP plugin endpoint (JSON-RPC over the site's REST API), with a backup that cannot silently come back empty, surgical replacements inside block/ACF content, and live verification. Use when asked to "update the site copy via MCP," apply audit fixes to a WordPress site, or change Yoast-driven SEO output. Also routes the fixes that content tools cannot reach (site URL, Yoast sitewide settings, redirects) to the right place.
---

# WordPress MCP Site Ops

Several WordPress plugins expose the site as an MCP server: a JSON-RPC endpoint under `/wp-json/<plugin>/v1/mcp` with a bearer token. Agents can list, read and write posts, pages, media and menus through it. The tools are powerful, and the failure modes are quiet. A dead token, a WAF, or a bad replacement can produce "success" with no change, or an empty backup. This skill is the safe loop.

## Preflight (stop at the first failure)

1. **Discover, don't assume.** Call `tools/list` first. Tool names and argument keys differ by plugin and version (`page_id` vs `id`, `field` vs none). Build calls from the listed `inputSchema`, not from memory or an old script.
2. **Auth check.** Make one read call, for example the current-user tool. A `401` with an empty body means the token was revoked or rotated. Stop. Ask the owner to regenerate it in the plugin's settings and store it in the secret manager. Never ask for the token in chat, and never put it on a command line. Inject it with your secret manager's run command (for example `<secret-manager> run -- <cmd>`).
3. **WAF check.** A `403` for the same request that works in `curl` is usually the host firewall rejecting the default `Python-urllib` user agent. Send an explicit `User-Agent`, or use `curl`.
4. **Backup, and prove it.** Dump every page and post (raw content plus status) to a timestamped JSON file before the first write. The backup script must fail on HTTP errors (`curl -sSf`, or raise on status) and must assert a nonzero page count. Without that, a 401 writes a valid-looking file with `"pages": []` and uploads it as your restore point. Check the file's page/post counts against the listing before you continue.

## Editing content

- **Read raw first.** Fetch the page's raw `post_content`, not the rendered HTML. Block themes and ACF blocks store field values twice: as JSON attributes in the block comment (`<!-- wp:acf/hero {"data":{"title":"…","_title":"field_…"}} -->`) and sometimes as rendered markup. Change the JSON attribute. The rendered output comes from it.
- **Match stored encoding.** Stored content uses `&amp;`, `—`, curly quotes and escaped slashes where the rendered page shows `&`, `—` and `/`. Copy the search string from the raw fetch, not from the live page.
- **Surgical replace over full overwrite.** Prefer a search/replace tool on one field, one string per call. Log the reported change count, and treat `0` as a failure, not a no-op. Use a full-content update only for a page you generated whole from a file in the repo.
- **Keep replacements in a reviewable file.** Put the `(old, new)` pairs in a script or JSON list committed next to the site's other tooling. That file is the change record and the rollback map (swap the columns).
- **Titles and meta descriptions** usually live in SEO-plugin post meta (Yoast: `_yoast_wpseo_title`, `_yoast_wpseo_metadesc`), not in `post_content`. Check whether the MCP exposes post meta before you promise these.

## What content tools usually cannot reach

Route these to wp-admin, WP-CLI through the host, or the owner. Do not hack them in through page content:

| Symptom (from a crawl) | Root cause | Where to fix |
|---|---|---|
| `robots.txt` `Sitemap:` line, sitemap `<loc>`s or Yoast `sameAs` use `http://` on an https site | Settings → General: WordPress Address / Site Address still `http` | wp-admin, or `wp option update home/siteurl` |
| Person/Organization schema lacks GitHub or other owned sites in `sameAs` | Yoast → Settings → Site representation / the user's profile "Other profiles" | wp-admin |
| No `og:image` on any page | Yoast → Social sharing default image is unset | wp-admin (upload the image via media tools first) |
| Two blog archives (`/blog/` and `/blog-2/`), one with a theme placeholder h1 | Settings → Reading "Posts page" points at one page, and the theme or an old import made another | Pick one, set it as the posts page, 301 the other (redirect plugin or host rules) |
| Stale page after a successful write | Host/page cache (LiteSpeed, host CDN) | Purge the cache in the host panel or with its API |

## Verify live

Re-crawl the changed URLs, for example with `../portfolio-cohesion-audit/scripts/extract.py`. Confirm the new strings, h1, canonical, OG tags and JSON-LD on the live page, not in the API response. Diff before and after on visible text to catch collateral edits. If a change doesn't show, purge the cache before you retry the write. Retrying the write stacks replacements.

## Guardrails

- One site, one token, one backup per session. Do not reuse a backup from an earlier session as the restore point.
- Never change user accounts, roles, plugins or the site URL through the MCP without explicit owner approval. These are account and security settings, not copy.
- Keep personal data, tokens, hostnames of private infrastructure and client names out of committed replacement files and skill notes.

## Related

- `portfolio-cohesion-audit`: finds what to change; this skill applies it on WordPress
- `brand-identity`: the schema values (`@id`, `sameAs`) worth setting in the SEO plugin
- `ai-agent-visibility`: robots/sitemap/llms.txt expectations
