# Stranger-read prompt (for a cheap worker model)

Paste this above the page text. Label properties A, B, C… and never tell the worker they share an owner. The worker should only extract; the lead model judges.

```
You are a stranger with no context reading several web properties. For EACH property output exactly these fields, one line each, quoting short exact phrases from the text as evidence (max 15 words per quote):
- headline_claim:
- who_its_for:
- price_signal: (exact prices if stated, else cheap/mid/high-ticket inferred + why)
- primary_cta:
- voice: (I / we / brand; formal/casual)
- operator_name_forms: (every way the owner or brand is named)
- job_titles_used: (every role label, verbatim)
- mentions_other_properties: (which of A/B/C/... it links or names, verbatim)
- proof: (client names, numbers, case studies, years)
- confusing_to_stranger: (anything contradictory or unclear, max 2 items)
Then one final line: SAME_PERSON_OBVIOUS: for each pair say yes/no and the evidence a stranger would use.
No preamble, no advice. Facts only.
```

## Feeding it

Per property, send the homepage plus the pages a buyer reads before contacting: about, services/pricing, contact. Trim each to about 1,500–3,500 words of visible text (the `text` field from `scripts/extract.py`). For a GitHub profile, send the profile README, the bio/company/blog fields and the pinned repo names. About 20k characters for 3–4 properties is enough.

## After it answers

Spot-check every quote that will drive a finding (`grep` the extracted text). Workers read footers and nav as page content and sometimes attribute a phrase to the wrong page. A finding you cannot trace to a line in the crawl does not go in the report.
