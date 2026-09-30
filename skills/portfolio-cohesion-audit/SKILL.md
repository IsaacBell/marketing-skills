---
name: portfolio-cohesion-audit
description: Evidence-first audit of whether one operator's several live properties (personal site, studio/agency site, GitHub profile, side store) read as one coherent person to a stranger and to crawlers, with a technical SEO pass on each. Use when a solo founder asks "does this look coherent or confusing," "audit my sites and GitHub together," or runs offers at different price points/audiences and wants to know what to fix. Produces a verdict, an identity string, a link/schema plan and a per-property fix list.
---

# Portfolio Cohesion Audit

`brand-identity` says *what* a consistent entity looks like (same name strings, `sameAs`, one hub). `solopreneur` says *which* property to push. This skill is the measurement between them. Crawl every property live, reduce each one to comparable fields, and find the exact places a stranger loses the thread. Use it before either of the other two when the user's question is "how do I come across."

Different price points are not the problem by themselves. A $500 store build and a fractional-CTO retainer can belong to one person. Confusion comes from four specific, observable defects:

1. **Title soup.** One person carries several role labels, sometimes on the same site.
2. **One-way links.** Property A names B, but B never names A. Every property except the one a stranger lands on is invisible.
3. **Tier leakage.** A monetization or pricing signal from one tier appears on another tier's surface, for example a tip jar or a $19 product beside an enterprise offer.
4. **Description drift.** Property A describes B differently than B describes itself.

Measure these four. Do not score vibes.

## Step 1 — Crawl, deterministically and cheaply

Run `scripts/extract.py <url>` for each site. The script uses only the standard library. It fetches the homepage, up to 7 first-party pages linked from it, and `robots.txt`, `sitemap.xml` and `llms.txt`. It emits JSON with title, meta description, canonical, robots meta, OG/Twitter tags, h1/h2, a JSON-LD summary (`@type`, `@id`, `sameAs`, `founder`…), image alt counts, internal/external links and visible text. It does not render JavaScript. If `words` is near 0 on a page that shows content in a browser, read that page in a browser instead.

Fetch pages the homepage does not link (often `/about/`) with `page()` from the same module. Follow external links that point to another property the operator owns. These links often reveal a property the user did not mention, and that property is part of the audit.

GitHub: `gh api users/<login>` (bio, company, blog, hireable), `/social_accounts`, `/repos`, the profile README (`repos/<login>/<login>/readme`), and pinned repos from the profile HTML. Check that the `company` handle resolves. A dead `@org` link is common.

Write the crawl output to a gitignored working dir, not to the conversation. Read it with `jq` projections. Read raw HTML only when a field looks wrong.

## Step 2 — Stranger read, delegated

Send the visible text to a cheap worker model with `stranger-read-prompt.md`. Label properties with letters, never with the owner's name. The worker extracts the headline claim, audience, price signal, CTA, voice (I/we/brand), every name form, every job title, cross-mentions and proof, then answers "same person obvious?" for each pair. Extraction is rote work. Keep judgment for the lead model.

Spot-check every quote that will become a finding with `grep` on the crawl JSON. Workers attribute nav and footer text to the wrong page.

## Step 3 — Build four matrices (the actual audit)

**Identity strings.** For each property, list name forms, role titles and the one-line description, taken from the h1, `<title>`, meta description, schema `description`, llms.txt, GitHub bio and repo description. Count distinct titles per person. More than one title across the whole portfolio is a finding. Also flag spelling drift in the brand name (`FooStudio` / `Foo Studio` / `FOO STUDIO`) and "I" vs "we" on a one-person site.

**Link graph.** Draw directed edges: visible link, visible name mention, schema `sameAs`/`founder`/`@id` reference. Record where each edge lives (home, about, footer). Rules:
- Every property must reach the hub within one click, and the hub must name every live property somewhere. A missing reverse edge is the most common finding.
- A lower-priced property should link up to the hub. A named senior operator raises trust for small buyers.
- The hub should link down from about/work pages, not from its money pages. A $500 link beside a high-ticket CTA anchors the price down.
- Schema edges must mirror visible edges. Use the same `@id` for the person on every site (for example `founder: {"@id": "<hub>/#person"}`) and put every owned profile in `sameAs`.

**Price ladder.** Put each property's price anchors on one line, low to high: explicit prices, "from $X", tip jars, donation buttons, product prices. The ladder itself is fine. Flag any rung that appears on the wrong surface. Also flag a high-ticket surface with no price context at all when a lower tier shows exact prices.

**CTA inventory.** List every booking, contact and payment endpoint (scheduler links, forms, Ko-fi, email). Several scheduler URLs for one person is a finding. Pick one per tier.

## Step 4 — Technical SEO, only what matters across properties

Check these per property. They are the defects that repeat on multi-property founders:
- Sitemap and robots `Sitemap:` line use the same scheme and host as the canonicals. WordPress sites often emit `http://` here when Settings → General still says `http`. The same root cause puts an `http://` self-URL in Yoast's `sameAs`.
- Canonical present on every indexable page, not only home.
- `og:image` present. Without it, every share of every property renders as a blank card.
- Exactly one h1 per page. Theme-placeholder h1s count as defects ("Check Our latest Post").
- Duplicate archives, for example `/blog/` and `/blog-2/`: pick one and 301 the other.
- Schema: the org/service entity has an `@id`, and a `founder` or `sameAs` pointing to the hub person.
- `llms.txt` name and description match the site's own h1 and schema.
- Stale or dated copy ("coming soon as of <date>", old issue numbers).

Run `seo-audit` separately for a deep single-site crawl. This pass exists to compare properties, not to replace it.

## Step 5 — Verdict and fixes

Write the verdict as a stranger's path: "Land on B: you see <x>, you cannot tell <y>. Land on C: <x> undercuts A's <y>." Then:

1. **Identity string.** One sentence: `<Name> — <one title> for <one audience>`. Every property states its role relative to it, for example "the build studio of <Name>" or "the open-source work of <Name>."
2. **Per-property fixes**, ordered by stranger impact, each tied to a crawl observation. Say which file, setting or field changes.
3. **Link and schema plan.** The missing edges, and the exact JSON-LD `@id`/`founder`/`sameAs` values.
4. **Leave alone.** Name what is already coherent, so the user does not churn it.

Keep the report short. The user needs about 10 fixes, not 40.

## Guardrails

- Visit every property live, in this session. Memory of the owner's own sites is stale, and so is the owner's memory.
- Do not recommend merging properties at different price points. Recommend explicit role labels and two-way links.
- Do not treat the owner's own business as a client case study without saying so. Labeled self-built proof is fine. Unlabeled self-built proof is a credibility risk if discovered.
- Separate donation/tip mechanics from paid offers on any surface a high-ticket buyer sees.
- In repos whose hooks block personal names in shell commands, put URLs and handles in a file and read them from the file (`$(cat handle.txt)`). Do not work around the hook.

## Related

- `brand-identity`: schema and entity-home theory this audit checks against
- `solopreneur`: what to do with the verdict (which lane to push, whom to hire)
- `seo-audit`: deep single-site crawl with OpenSEO
- `ai-agent-visibility`: robots/sitemap/llms.txt setup when Step 4 finds them missing
