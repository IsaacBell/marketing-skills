---
name: branding
description: Define, audit, or apply brand strategy — purpose, positioning, story, voice and tone (not visual design specifics). Use when the user mentions "brand strategy," "brand voice," "brand story," "positioning," "brand archetype," "brand guidelines," "messaging," or wants their communication to read as one coherent identity across a website, social, and product.
---

# Brand Strategy

Covers the strategic layer of a brand: why it exists, who it's for, how it's positioned against alternatives, what story it tells, and how it sounds. Not colors, fonts, or logo files — those are implementation, and belong in whatever visual-design tooling this repo already has for that.

## Before writing anything

Identify three things:

1. **Scope** — is this a brand new definition, an audit of something that already exists, or an alignment pass to catch drift across touchpoints?
2. **Touchpoints** — where does this brand actually show up (site, social, product copy, a newsletter, a deck)? A brand voice only matters where a real audience encounters it.
3. **What already exists** — read any existing site copy, about page, or prior brand notes before proposing anything new. A founder's actual writing, even unpolished, is better source material than a generic positioning template.

If this is an audit rather than a from-scratch definition, don't rewrite what's already working. Name what's consistent, then flag the specific places where the voice contradicts itself or the positioning is vague enough to apply to any competitor.

## The five things a brand strategy has to answer

- **Purpose**: why this exists beyond making money, in one sentence a stranger could repeat back.
- **Audience**: who specifically it serves — not "everyone," a description specific enough to exclude people.
- **Positioning**: for [audience] who [need], this is a [category] that [does the thing]. Unlike [the obvious alternative], it [does something they don't, and why that matters].
- **Values**: 3-5 things the brand actually stands for, each one a real trade-off (a value that costs nothing to claim isn't a value).
- **Differentiation**: the concrete, provable reason to pick this over the alternative — not an adjective ("better," "innovative") but a fact (a founder's specific background, a real product decision, a track record).

Weak positioning is the most common failure here — a sentence so generic it could describe any competitor. Test it: swap in a rival's name. If the sentence still reads fine, it isn't positioning yet.

## Story, briefly

A brand story only needs to do one job: make the audience the protagonist, not the founder. The founder's origin story matters as color (why this got built, what problem was personally felt) but the story that sells is the customer's — what they're stuck with now, what changes once they use this, and what proof exists that it actually changes (a real result, not a hypothetical one).

Skip the full hero's-journey scaffolding unless the deliverable specifically calls for a long-form about page or pitch narrative. Most of the time, two or three sentences following that shape (their problem → the shift → the better state, with one piece of proof) is the whole asset.

**Archetype, if useful**: naming a single dominant tone — the wise-and-direct sage, the scrappy outlaw, the reliable everyman, the polished authority — can shortcut a lot of voice decisions at once. Use it as a filter for consistency checks, not as a mandatory step; skip it entirely if the user just wants a voice-and-tone note, not a full identity workup.

## Voice and tone

Voice is the personality that stays constant. Tone is how that personality flexes by context (a support reply is warmer than a pricing page, an error message is more direct than a launch post). Define both concretely:

- **Voice**: 2-3 adjectives, each with a one-line gloss of what it means in practice (not "bold" alone — "bold: states the opinion first, then the reasoning").
- **Avoid**: specific words or patterns that don't fit (buzzwords, hedging language, a term a competitor overuses).
- **Preferred**: specific substitutions ("customer" not "user," "built" not "leveraged") — this is the part that actually gets reused in review, so make it concrete enough to check copy against.

If this repo maintains project-specific context (an existing context file, prior brand notes), keep the working voice/tone/avoid/preferred list there rather than restating it fresh each time — it should compound across sessions, not get rederived per request.

## Applying it across touchpoints

Once purpose, positioning, story, and voice exist, the practical work is checking that every touchpoint (site copy, social bio, product onboarding text, a deck) actually reflects them — not that each touchpoint independently sounds fine. Drift usually shows up as: a positioning line on the homepage that doesn't match how the founder describes the product in conversation, or a voice that's confident on the marketing site and hedging in the product UI.

When the deliverable needs to be implementation-ready (a style guide section, copy for a deck, paragraph styles for a doc), hand off the specific colors/type/spacing work to this repo's visual-design tooling — this skill defines what those specs should express, not the HEX values themselves.

## Output format

- **Positioning statement** (the single sentence, competitor-tested)
- **Purpose, audience, values, differentiation** (short, concrete, no filler adjectives)
- **Story** (2-3 sentences, customer as protagonist, one proof point)
- **Voice & tone** (adjectives with glosses, avoid list, preferred terms)
- **Consistency check**, when auditing: specific places where a touchpoint contradicts the above, with the exact fix
