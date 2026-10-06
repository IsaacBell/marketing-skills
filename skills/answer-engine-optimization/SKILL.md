---
name: answer-engine-optimization
description: "Optimize content so AI assistants and AI search summaries cite it — ChatGPT, Claude, Perplexity, Google AI Overviews, Bing Copilot. Use when the user mentions AEO, GEO, generative engine optimization, LLM optimization, 'getting cited by ChatGPT', or AI search visibility. Content-and-citation strategy, not crawler plumbing — for the robots.txt/sitemap.xml/llms.txt files that make a site machine-readable in the first place, use ai-agent-visibility. For traditional Google ranking work, use seo-audit."
---

# Answer Engine Optimization (AEO)

## Goal

Get content cited inside AI-generated answers, not just ranked in a results list. The user may never click through — the win is the assistant naming the brand, quoting the fact, or linking the page as a source. This is a different target than SEO: SEO optimizes a page to be the destination; AEO optimizes a paragraph to be the *quotable* thing.

## How citation actually works

Every AI answer engine retrieves candidate content before it generates a response (this is RAG — retrieval-augmented generation), then writes an answer grounded in whatever it pulled back. If content never gets retrieved, it can never get cited, no matter how well-written it is. So AEO is two problems stacked:

1. **Retrievability** — can the engine's crawler or search index find and fetch this page at all?
2. **Citability** — once retrieved, is there a self-contained chunk of text clear enough to lift into an answer?

Engines differ in how they retrieve, and that changes where effort pays off:

- Some run their own crawl and index (Perplexity, ChatGPT's web search) — behaving like a second search engine you need to be indexed by, independent of Google.
- Some lean on an existing search engine's index under the hood (Bing Copilot rides Bing; Google's AI Overviews ride Google's own index) — meaning standard SEO fundamentals (crawlability, backlinks, structured data) still carry most of the weight.
- Smaller or newer AI tools often buy retrieval from a third-party search API rather than building their own — which means showing up in general web search results indirectly feeds them too.

Practical implication: don't treat "optimize for AI search" as one job. Confirm the page is crawlable and indexed by traditional means first (that alone captures the engines riding an existing search index), then layer citation-specific formatting on top for the engines running independent retrieval.

## Step 1 — Confirm retrievability before touching content

- Check whether the AI crawlers relevant to the target engines are allowed in `robots.txt`. Training crawlers (used to build the underlying model) and retrieval/search crawlers (used to answer live queries) are often named separately — blocking the former doesn't necessarily block the latter, and blocking the latter kills citation eligibility outright. If this file doesn't exist or hasn't been audited, hand off to `ai-agent-visibility` first — AEO work on an unindexed or blocked site is wasted effort.
- Confirm the content that matters is present in the raw HTML response, not injected client-side. Most of these crawlers do not execute JavaScript; anything rendered only after hydration is invisible to them.
- There is no submission portal for most AI crawlers — they discover pages the same way traditional search engines do, through crawling and sitemaps. A sitemap and inbound links still matter here.
- Check the CDN or firewall, not only `robots.txt`. Since July 2025, Cloudflare blocks known AI crawlers by default on newly added domains, so a site can block them with a clean `robots.txt` and an owner who never chose to.

### Signals you can prove from outside

These need no access to the site's accounts, so they work for an audit and for a cold email. Each one is a fact the owner can verify in a browser.

1. **Text only after JavaScript.** View Source (Ctrl+U) and search for the homepage headline. If it is missing, crawlers that do not run JavaScript see an empty page.
2. **Crawlers blocked.** `robots.txt` disallows GPTBot, ClaudeBot, PerplexityBot or OAI-SearchBot, or disallows Googlebot by mistake. A firewall that returns 403 to those user agents counts too.
3. **Leftover `noindex`.** A `noindex` meta tag or `X-Robots-Tag` header carried over from a staging site.
4. **Thin index coverage.** A `site:` search returns far fewer pages than the sitemap lists, or nothing.
5. **Absent from the answer.** Ask ChatGPT or Perplexity for "[their service] in [their city]". If it names competitors and not them, that is the opening line; the four checks above usually explain why.

A missing `llms.txt` is not on this list. Almost no site has one and few AI tools read it, so its absence is not a problem worth selling.

## Step 2 — Structure content to be citable

An AI answer engine lifts a chunk of text, not a whole page. Make the chunks it would lift self-contained and correct in isolation:

- **Answer the question directly, early.** Under each subheading, give the direct answer in the first sentence or two, then support it with the specifics. Don't bury the conclusion under three paragraphs of throat-clearing.
- **One idea per block.** A paragraph or list that only makes sense with the paragraph before it is a paragraph nothing will quote cleanly.
- **Use structure the answer can borrow.** Numbered steps, definition lists, comparison tables, and short bulleted takeaways translate cleanly into an AI-generated answer; a wall of narrative prose doesn't.
- **Name the entity plainly.** State the brand, product, or author's name near the claim being made, not just in the byline or footer — some engines attribute more reliably when identity is co-located with the fact.
- **Keep it current.** Several engines weight freshness heavily, especially the ones running independent crawls. A page that hasn't been touched in years is a weaker citation candidate than a recently updated one saying the same thing, all else equal.

## Step 3 — Write for extraction, not persuasion

Marketing copy that's built to persuade over several paragraphs works against citation. Write the parts that need to be cited more like reference material:

- State facts and numbers plainly, with the source of the number if it's not proprietary.
- Avoid front-loading brand voice or a hook before the actual answer — that's the first thing a retrieval system truncates or skips.
- Where a competitor or alternative reasonably belongs in the answer, don't omit it just to look better by comparison — an engine assembling a balanced answer is less likely to cite a source that reads as one-sided, and an incomplete answer is a worse outcome than being cited alongside a competitor.

## Step 4 — Distribute beyond the owned site

AI engines cite third-party platforms as readily as brand-owned pages, sometimes more readily, because platform-level trust transfers. Depending on the topic, that can mean a well-maintained GitHub README, a genuinely useful contribution to a community wiki or Q&A site, or a detailed video with a transcript. Treat this as extending the citable surface area, not as a replacement for owned content — and only contribute where it's genuinely useful; placement that reads as manipulative tends to get penalized by the platform itself, not just ignored by the AI engine.

### Comparison pages decide the shortlist

When someone asks how two products compare, the engine builds the answer from what it retrieves at that moment: review sites, forums, and any credible article that answers the question directly. It does not wait for a retrain, so publishing now can change the answer. With no comparison of your own, a competitor's version becomes the default.

1. Ask the engine how it compares the two products and to list its sources. Note what it already reads.
2. Use the competitor's product hands-on. Do not write from their marketing site.
3. Publish the comparison, then two or three genuinely rewritten versions elsewhere. Never post the same text twice; duplicates compete with each other.

Good looks like a side-by-side with real test results and plain statements of where each product is weaker.

### Category roundups

Engines answer "best tools for X" from roundups, often without showing which one. Build it from your comparison work, add screenshots and technical detail, and place competitors fairly, including where they beat you.

### Review sites carry the sentiment answer

When a prospect asks what customers say, the engine quotes review platforms, and one old negative review can follow the brand through every answer. It cannot be argued away. Earn volume honestly: invite satisfied customers to review on one chosen site, not several, and embed that site's rating widget on your own pages.

### Community forums are a long game

Forums get cited for comparison questions, and they are moderated against promotion. A new account posting links gets removed; an account that answers questions usefully for months earns the standing to mention its product when asked. Plan in quarters, not weeks.

## Step 5 — Measure presence, sentiment and citations

Three separate measurements:

- **Presence**: is the brand named in the answer at all?
- **Sentiment**: is it praised, criticized or listed flatly?
- **Citations**: is the domain used as a source?

Answers vary from run to run, so one manual test proves nothing. Fix a list of prompts, built from keyword research and the follow-up questions search engines suggest, re-run it weekly or monthly, and read the direction across samples. Tag AI referrals as their own channel in analytics so they do not disappear into organic search.

## What to skip

- Chasing exact citation-rate percentages by platform — these move constantly and aren't independently verifiable enough to plan against. Track whether the brand shows up when you ask the target engines directly, over time, instead.
- Optimizing for model *training* data. That's a slow, mostly unmeasurable channel compared to retrieval-time optimization. Put effort into RAG-era retrieval and citation, not into trying to influence a future training run.

## Output format

When delivering AEO recommendations, give:

- **Retrievability check**: crawler access, indexing status, JS-rendering risk — pass/fail with evidence.
- **Citability rewrite**: specific paragraphs or sections restructured for direct-answer-first, with before/after where useful.
- **Distribution targets**: 1-3 concrete third-party placements worth pursuing, and why they fit this topic.
- **What not to do**: call out anything in the current content actively working against citation (buried answers, no clear entity, stale dates).
