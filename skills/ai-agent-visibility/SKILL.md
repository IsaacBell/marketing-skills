---
name: ai-agent-visibility
description: "Make a site legible to AI agents and crawlers by adding a robots.txt, sitemap.xml, and llms.txt — for a site that has none of these and is invisible to search and to agentic browsing as a result."
---

# AI Agent Visibility

## Goal

Give a site the three plain-text files that make it discoverable and legible to crawlers and AI agents: `robots.txt`, `sitemap.xml`, and `llms.txt`. Use this when a site is missing one or more of these, or when someone reports a site is "invisible to AI agents" or "not showing up" — verify first (see Workflow step 1) rather than assuming the cause is JS rendering or a block; the far more common cause for a small or new site is simply that none of these files exist and the domain has never been indexed.

This skill only makes a site legible once something visits it. It does not get the site crawled or indexed — that still requires the owner to submit the sitemap in Google Search Console / Bing Webmaster Tools and, for a brand-new domain, to earn inbound links over time. Say this plainly when delivering the files.

## Required inputs

- Domain (e.g. `https://www.example.com`)
- List of pages to include: path + one-line description of each
- A short business/service summary: what it does, who it's for, and (if relevant) pricing or key facts an agent would want to answer questions with

## Workflow

1. Check current state before writing anything: fetch `/robots.txt`, `/sitemap.xml`, and `/llms.txt` on the live domain. Note which exist. If a `robots.txt` already exists and disallows something, do not blindly replace it — read it first; a `Disallow` may be intentional (e.g. blocking `/admin`), and only the missing pieces should be added.
2. Confirm the site's content is actually crawlable: fetch the homepage HTML directly (not via a browser that runs JS) and confirm the real content is present in the raw response. If the content only appears after client-side rendering, that's a separate, bigger problem (SSR/prerendering) than this skill fixes — flag it instead of proceeding.
3. Draft `robots.txt`: `User-agent: *` allow-all as a baseline, plus explicit named entries for AI/agent crawlers so they're allowed even if a future rule narrows the wildcard — at minimum `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `ClaudeBot`, `Claude-User`, `anthropic-ai`, `PerplexityBot`, `CCBot`, `Google-Extended`. Add a `Sitemap:` line pointing at the domain's `/sitemap.xml`.
4. Draft `sitemap.xml` (standard `urlset`/`sitemaps.org` schema) from the page list — one `<url>` per page, `lastmod` as today's date, `changefreq` set per page's real update cadence (don't default every page to the same value).
5. Draft `llms.txt` following the community convention: an `H1` with the site/business name, a one-line `>` blockquote summary, then short sections (e.g. "## What we do" / "## Pages") stating plain facts — pricing, platforms, who it's for, page links with one-line descriptions each. No marketing language. Keep it under ~40 lines; an agent should be able to answer basic questions from this file alone without fetching anything else.
6. Place all three files at the site's static root so they resolve at `/robots.txt`, `/sitemap.xml`, `/llms.txt`.
7. Deploy, then re-fetch all three URLs live to confirm they resolve (not a 404) and render as plain text/XML, not the site's own 404 page.
8. Tell the site owner explicitly: these files make the site legible once crawled, but a new or low-authority domain still needs the sitemap submitted in Search Console / Bing Webmaster Tools, and backlinks, to actually get indexed. Offer to help with the submission step if you have access; otherwise name it as their next manual step.

## Output format

Three files: `robots.txt`, `sitemap.xml`, `llms.txt`. Write them directly into the site's source if you have repo access; otherwise print all three, each under its own `### filename` heading in a fenced code block, so they can be copy-pasted.

## Guardrails

- Never overwrite an existing `robots.txt` or `llms.txt` without reading it first — a `Disallow` rule already there may be deliberate.
- Don't claim this fixes indexing or rankings; it only removes a barrier to legibility. Say so.
- `llms.txt` is facts, not copy: no adjectives doing the selling ("industry-leading", "seamless"), just what the business does, what it costs, and how to reach it.
- If the homepage content doesn't appear in a raw (non-JS) fetch, stop and flag the rendering issue instead of producing files that won't actually solve "invisible to AI agents."
- Name AI crawlers explicitly in `robots.txt` rather than relying only on `User-agent: *` — some agent operators check for their own named entry and are more cautious about a bare wildcard.
