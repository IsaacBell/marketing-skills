---
name: brand-identity
description: When the user wants their brand, product, or personal name recognized as a distinct entity by search engines and AI answer engines (Knowledge Graph, Knowledge Panel, AI Overviews/Perplexity citation), or wants a consistency audit across multiple sites/profiles owned by the same person or brand. Also use for "entity SEO," "Knowledge Panel," "brand entity," "who am I to Google," or when one person/brand runs several domains that should read as one identity.
---

# Brand Identity

Search and AI answer engines match meaning, not just keywords. They resolve a name to an **entity** — a specific person, brand, or product with a stable identity — and use that resolution to decide whose content to cite. A founder running several properties (a consulting site, a product, a side domain, a GitHub profile) is the same entity to a human but often reads as several unrelated identities to a crawler, because nothing ties them together.

## Core idea

An entity is singular and well-defined: a name, a set of attributes, and relationships to other entities. Keywords are ambiguous strings; entities are not. The practical goal is making it unambiguous which entity owns which claim, across every surface an agent or crawler might find.

## Audit

For a person or brand with 2+ live properties:

1. Pull the name, one-line description, and logo/photo as they currently appear on each property (homepage, About page, GitHub bio, LinkedIn, etc).
2. Flag mismatches: different name forms, inconsistent one-line descriptions, missing links between properties, no property stating "these are the same operator."
3. Check for `Organization`/`Person` schema (JSON-LD) on each site. Most small sites have none — that's the single highest-leverage fix, not a nice-to-have.

## Implementation

- **Person schema**: `name`, `url`, `sameAs` (GitHub, LinkedIn, other owned domains), `affiliation` where relevant. Place on the primary "hub" site (the one meant to be the canonical reference).
- **Organization schema**: `@id` as a stable URL (e.g. `https://example.com/#organization`), `name`, `url`, `logo`, `sameAs`. Repeat on every property, always pointing back to the same hub `@id` — this is what tells a crawler "these are the same thing," not just visually consistent branding.
- **Consistency, not merger**: separate properties at different price points or audiences don't need to become one site. They need to cross-link and use identical name/description strings so an agent resolving one can find the others.

## When properties are deliberately different audiences

A multi-property founder doesn't need one voice everywhere — a high-ticket consulting site and a budget small-business-build site can stay distinct. What they need is one property (usually a personal site or GitHub profile) acting as the entity's home, with `sameAs` links out, so a visitor or AI agent landing on any one property can find the others as the same operator rather than assuming a coincidence of name.

## Output format

- Entity audit: name/description/logo consistency gaps, by property
- Schema to add: Organization + Person, with `@id` and `sameAs` values filled in
- One property named as the canonical "entity home"
- What NOT to do: don't chase a Knowledge Panel directly (Google grants these, you can't request one) — consistency and schema are the controllable inputs

## Related

- `ai-agent-visibility` (this repo): robots.txt/sitemap/llms.txt — crawlability, a prerequisite for entity resolution to happen at all
- `voice-and-positioning` (this repo): per-property voice, once the entity layer is consistent
- `solopreneur` (this repo): which property to prioritize when several exist
