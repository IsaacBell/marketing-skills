---
name: search-indexing
description: When the user wants faster search indexing for a new or recently updated site (primarily Bing/Yandex via the IndexNow protocol), or mentions "IndexNow," "instant indexing," "Bing indexing," or "my new site isn't showing up in search." Complements ai-agent-visibility (robots.txt/sitemap/llms.txt) and is most useful right after launch, when a brand-new domain has zero backlinks and no crawl history.
---

# Search Indexing (IndexNow)

A live, crawlable site is still invisible until something tells search engines it exists. Submitting a sitemap starts that process for Google but can take weeks on a new domain. IndexNow is a direct push notification to Bing and Yandex (not Google, which doesn't support the protocol) that a URL is new or changed — the closest thing to instant indexing available to a small site.

## Setup

1. Generate an API key (any UUID/random string works).
2. Publish a verification file at `https://yourdomain.com/{key}.txt` containing just the key.
3. Submit URLs via a `GET`/`POST` to `https://api.indexnow.org/indexnow` with the key, key location, and URL list.

## When to submit

- New page goes live, or a page's content/meta materially changes.
- Once per deploy, batched — not on every minor edit.
- Prioritize commercially important pages (home, pricing, contact) over incidental ones.

## Keep it in sync with the sitemap, not a separate list

Pull the URL list from the same source that generates `sitemap.xml`. A hand-maintained second list drifts and quietly stops matching real pages. If there's a build/deploy step already, add an IndexNow submission call to it rather than a standalone script that's easy to forget to run.

## What this does and doesn't fix

- Fixes: Bing/Yandex indexing lag on a new or updated URL.
- Does not touch Google — that's still sitemap + Search Console + time + inbound links (see `ai-agent-visibility`).
- Does not substitute for having a sitemap or robots.txt at all — this is an accelerant on top of those, not a replacement.

## Output format

- API key + verification file location
- Submission trigger (manual, or wired into the existing deploy step)
- Confirmation path: Bing Webmaster Tools submission log

## Related

- `ai-agent-visibility` (this repo): robots.txt, sitemap.xml, llms.txt — do this first
- `seo-audit` (this repo): broader indexing/crawlability check beyond just IndexNow
