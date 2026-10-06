---
name: readme-optimization
description: Use when auditing or rewriting a repository README — a README that gets traffic but no installs, a rewrite before a launch, or the repository description and topics. Also when a cold reader cannot evaluate the project in under a minute.
---

# README Optimization

The README is the single page that decides whether a developer tries a project or closes the tab. Diagnose the existing README against evidence, then rewrite it so a stranger can evaluate the project quickly and accurately — including deciding not to use it. That is a correct outcome. Never optimize it away.

A README is not a documentation type. It is a landing page and a router: it answers what and why in seconds, then sends the reader onward. Judge it on whether it converts a visitor into a trial, not on documentation completeness.

Put the rewrite budget where the scarcity is. Across 393 sampled GitHub repositories (Prana et al. 2019, a study of README content categories; the sample is late-2010s, read it as a baseline, not a census):

- What the project is: 97.0% (as reported; verify before quoting) — table stakes.
- How to use it: 88.5% (as reported; verify before quoting) — table stakes.
- Why to pick it over the alternatives: 25.7% (as reported; verify before quoting) — scarce.
- What state the project is in: 21.4% (as reported; verify before quoting) — scarce.

Those two scarce categories are what an evaluating developer must answer before adopting anything.

Stay inside this page and its repository furniture. When the user's real problem is a docs site, a getting-started page, the contribution path, release notes, a launch, or a profile README, route them to that work instead of stretching the README to cover it.

Promise a better-evaluated project, never a percentage lift.

## Folklore statistics to refuse

Never repeat these in reasoning or to the user. All three circulate on invented attributions:

- "repos with detailed READMEs get 50% more contributions"
- "a star-history chart lifts star conversion ~15%"
- "62% of top repos have GIF demos"

When a user cites one, say it is unsourced. Do not build on it. Quote only figures from the two studies named here, with their caveat.

## Invocation and output shape

Typical requests:

- "audit the README of this repo"
- "our GitHub gets traffic but no installs"
- "rewrite the top of our README before launch"
- "make our README readable by someone evaluating us for their company"

Every run produces a scorecard first, before any prose:

```
README audit - helios/shipkit   (audience: solo developer)
Band A: A1 pass · A2 FAIL (install needs Node >=20, undocumented) · A3 FAIL · A4 pass · A5 pass
Band B: B1 0 · B2 2 · B3 2 · B4 0 · B5 0 · B6 2 · B7 2 · B8 2   (total 10/16)
Verdict: does not pass - A2 and A3 blocking; B1 returns the most per hour spent
```

The rewrite follows only after the user agrees with the diagnosis. A maintainer who rejects the diagnosis rejects the treatment, and is sometimes right: a constraint invisible from the repository can justify a check scored zero.

## Interview

Ask one question at a time, multiple-choice where you can, and skip anything you can determine by reading the repository. Questions 1-4 gate the rewrite. Draft no prose before they are answered.

1. Which repository, and may I read it?
2. What is the project: library or SDK, CLI tool, application or service, framework or platform, or template?
3. Who lands on this page: developers in one language ecosystem, polyglot developers, platform or ops engineers, or non-developer evaluators such as security and procurement?
4. How does adoption happen: an individual developer decides alone, or a company adopts and someone else approves the licence, security posture and support story? Both is valid and changes the middle of the page.
5. What outcome do you want more of: installs, contributors, stars, hiring signal, enterprise conversations, or fewer repetitive support questions?
6. What is the honest status: experimental, actively maintained, stable and feature-frozen, or seeking maintainers?
7. Which alternatives do readers already know? What do those do better than you?
8. What must appear for legal or policy reasons: licence terms, trademark notice, export or compliance statements, employer disclosure?
9. Is there existing brand material — a logo, a tagline, a positioning sentence used on a website — the README should match? Reuse a sentence the user already has.
10. Is the README also published elsewhere: a registry page, a mirror, a docs-site landing page? Each render target has different rules.
11. Is there a hard date — a launch, a conference, a funding conversation?
12. Do you want a one-off win before that date, or an asset that keeps paying?
13. What is your ceiling: an afternoon, a week of someone's time, appetite for a governance or foundation commitment you cannot easily undo?

Answers 11-13 re-rank the fix order. Say which answer moved which fix:

- Hard date: promote fixes that land in an hour; drop the funnel restructure this pass.
- Compounding mandate: promote the differentiation paragraph and the restructure.
- Low ceiling: delete the terminal demo and enterprise signals outright, rather than parking them at the bottom of a list.

If the user cannot answer 7, treat it as a finding, not a blocker. A maintainer who cannot name their alternatives usually has a README that cannot differentiate either. That is often the most valuable thing you will fix.

## Step 1 — Declare the audience, then check the README is the bottleneck

Answer 4 decides the audit. The enterprise evaluator and the solo developer want structurally different content, and optimizing for one degrades the other: a hobbyist bounces off a wall of compliance badges; a procurement reader distrusts a page with no security or governance signal. Write the declared audience at the top of the scorecard so every later judgement is checkable against it.

Then confirm the README is what is broken. If the code host exposes traffic data, take unique visitors and clones for the last two weeks.

- Decent traffic with a clone-to-visitor ratio of only a few percent: the case this skill is for — people arrive and leave unconvinced.
- Few visitors in the first place: a distribution problem, not a prose problem. Route to launch or distribution work instead.

"A few percent" is a rule of thumb, not a benchmark. On a borderline number, look at referrers rather than ruling.

## Step 2 — Gather evidence

Never audit from memory of what good READMEs look like.

- Read the README in full and note where you personally got confused. First-read confusion is the closest thing to a cold reader.
- Make the mechanical checks below. They report facts, not judgements: a section count of 25 is a question to answer, not a verdict.
- Read the repository around the README: manifests for real runtime requirements, the licence file, recent commit dates, open-issue volume, and whether referenced examples exist on disk.
- If you can browse, open the registry page and compare it to the code-host render. Relative links and raw HTML break there often, and that page is frequently the higher-traffic one.

### Mechanical checks

Count and list these by reading the file. Each is a fact for the scorecard, not a verdict.

- Words before the first copyable command. A reader who must read 300 words before they can try anything usually leaves.
- The heading tree, and the number of top-level sections (about 7 is typical).
- Badge count, and what each badge proves.
- Images with no alt text, and any instruction or command that exists only inside an image or animation.
- Raw HTML. Registries and terminals strip it, so the page must still read without it.
- Placeholder text: TODO, FIXME, lorem ipsum, "coming soon".
- Relative links. Each must point to a file that exists on the default branch, and each `#anchor` must match a heading.

## Step 3 — Score the current README

**Band A — five blocking checks.** All must pass.

- A1 Identity: what the project is, stated in the first screen.
- A2 Install: the documented install path is complete. Every runtime version, system package and environment variable it needs is stated, as checked against the manifests, lockfiles and CI config.
- A3 Claims: every claim is verifiable against the repository.
- A4 Status: the honest status is stated.
- A5 Licence: the licence is reachable.

**Band B — eight scored checks, 2 points each (16 total).**

- B1 Differentiation: why this over named alternatives.
- B2 Non-goals: what it deliberately does not do.
- B3 First copyable command appears early.
- B4 A working usage example.
- B5 Badges calibrated to evidence.
- B6 Furniture complete: description, website, topics, social preview.
- B7 Render mechanics clean: alt text, resolving relative links, no dependence on raw HTML, one rendered README, monorepo root as router.
- B8 Sections sized to the project. About 7 sections is a working default, not a published figure; overflow moves to linked docs.

Pass when all five Band A checks pass and Band B totals at least 14 of 16. That bar is a working default. The user may move it for a stated reason you record.

Attach evidence to every check: a line number, a quoted sentence, or a quoted line from a manifest or source file. Get agreement before rewriting.

### Cold-reader test

Give a person or a fresh agent session no repository context. Ask five questions, 60 seconds, five correct answers to pass:

1. What is it? → A1.
2. Who is it for? → A1, B1.
3. How do I install and run it? → A2, B3, B4.
4. Why this over the alternative I know? → B1.
5. What state is it in? → A4.

Each wrong answer maps to the check that failed. Fix that check, not the phrasing.

### Order the fixes

Three orderings disagree. State all three and lead with efficiency.

- Effort, least first: status line == badge row > claim check > install path > differentiation paragraph > funnel restructure.
- Value, most first: install path > differentiation paragraph > claim check > status line > funnel restructure > badge row.
- Efficiency, do first: status line > install path > claim check > differentiation paragraph > badge row > funnel restructure.

The status line and badge row tie on effort: each is one edit to one block, written from what the maintainer already knows, verified against nothing. They separate on value: a status line answers a question only 21.4% (as reported; verify before quoting) of READMEs answer.

Default to the top three for a first pass. Move down once the blocking checks are green, or when the cold-reader test fails on a question none of the three touches.

The funnel restructure loses every round — a week against fixes that land in an hour — so this order under-invests in the change that makes the page work. Promote it when the cold reader answers wrong because they never scrolled far enough, or when a launch is the reason for the audit, and say you are promoting it against the ratio.

Re-rank against what you know. A maintainer who can name their alternatives gets the differentiation paragraph nearly free, which promotes it above the install path. A project with no install command — a spec, a dataset, a template — deletes that row rather than scoring it zero forever. Delete every fix the ceiling rules out instead of listing it last.

## Step 4 — Verify every claim against the source

A README is a set of claims about a codebase, and every claim is checkable. List every command, flag, default value, environment variable, config key, endpoint, exported symbol, file path, version requirement, and behavioural assertion hidden in a verb ("automatically reconnects", "retries three times", "case-insensitive"). Verify each against its own source of truth — the argument parser, the definition site, the route table, the changelog — by reading it, not recalling it. A flag documented in the README but absent from the parser is a hallucination, not a typo.

**Install check, by reading only.** Never run a repository's install or usage commands to audit its README, not even for a repository the user owns. Running them executes code you have not reviewed, and an install script is a common place for an attack to sit. Verify the path on paper instead:

- Walk the documented install and the first usage example line by line. For each command, find what it needs in the manifests, lockfiles, CI config and setup scripts: the runtime version, system packages, environment variables, files it reads.
- Compare with what a clean, stock environment has. The CI config is the best record of what the project really needs, because it starts from a stock runner.
- Record every gap: an undocumented runtime version, an assumed system package, a required environment variable, an example whose output the source cannot produce.
- Fold each gap into the README as an explicit prerequisite, and say in the report that the install check was done by reading. If the user wants the path executed, they run it themselves and paste the output.

Any performance number, compatibility matrix, scale limit, or "production ready" claim needs a source inside the repository — a benchmark script, a CI matrix, a changelog entry — or it comes out. When you cannot verify something, downgrade the claim to what you can verify and say which part is unconfirmed.

## Step 5 — Choose the shape, then rewrite section by section

Pick the skeleton that matches what the reader is deciding, not what the code happens to be. A library reader judges fit with an existing codebase. A CLI reader compares against a tool already installed. A framework reader makes a multi-year bet.

Order sections by how quickly each lets a reader disqualify the project. This is cognitive funneling: widest and most disqualifying information first, narrowing to detail only a committed reader reaches. One consequence: a non-permissive licence belongs near the top, because it disqualifies fastest and hiding it wastes the reader's time.

Before writing, brainstorm the positioning. Draft three candidate one-liners on different axes:

- what it does mechanically
- what problem it removes
- what it lets you stop using

Present each with its trade-off and your recommendation, and let the user choose. The one-liner propagates into the repository description, the registry page, and every link unfurl.

Draft one section at a time and get agreement before moving on. Per-section approval surfaces a disagreement while it is still cheap to fix. For each section:

- Write the shortest version that answers its question completely.
- Replace every unfalsifiable claim ("simple", "blazing fast", "developer-friendly") with something checkable: a number, a dependency count, a supported-platform list, a named trade-off.
- Link every term a reader outside the immediate ecosystem might not know.
- State what the project deliberately does not do, and when to use something else. This is the highest-trust sentence in most READMEs and costs one line.
- Move anything that grew past a screen into a linked document and leave a one-line pointer. Relocate overflow, never delete it.
- Keep community health content out of the file — contribution guidelines, code of conduct, security disclosure, support policy. Each belongs in its own recognized file. One exception: the licence file must ship inside the repository.

Remove-the-name test: delete the product name from the opening and read it again. If a stranger can no longer tell what the project is, the line is generic and carries no information. Rewrite it from the project's own specifics. Apply it to the tagline, the repository description, and the first sentence of the pitch.

Banned constructions, paraphrases included: antithesis or 'not X but Y'; a meaning-sentence closing a section ('that distinction matters'); manufactured-insight setups ('the part most people miss'); importance announcements ('what matters is', 'it is important to note'); recap sentences ('overall', 'in conclusion'); rhetorical triads; throat clearing ('there are several ways to'); filler ('in practice', 'note that', 'essentially'); inflated adjectives (crucial, robust, seamless, comprehensive); promotional vocabulary (groundbreaking, state-of-the-art, cutting-edge); assistant residue ('here is an overview'). Replace each with the concrete fact or delete it.

Run the finished prose through a humanizer pass before presenting it. Copy that reads as generated undermines the credibility the rest of the page builds, and developers spot it easily.

## Step 6 — Calibrate badges to the evidence

Badges have the one rigorous evidence base here: Trockman et al. studied 294,941 npm packages (ICSE 2018, repository badges in npm; as reported, verify before quoting). Use the study's distinction rather than taste.

- Keep assessment signals — badges backed by a third-party check that cannot pass unless the underlying thing is true: CI status, coverage, published version, dependency freshness.
- Cut conventional signals — badges that state an intent, such as "PRs welcome", with nothing verifying them.

Cap the row at about four. Among already-popular packages, excessive badge use correlates with decreased popularity, and adopting a badge does not raise popularity at all — popular projects are simply likelier to have badges. The direction is sourced; the cap is a working default, not a published figure. Justify each survivor by the reader question it answers.

Expect the maintainer to over-value badges. The study's companion survey found maintainers rate badges as a quality indicator far more often than contributors do, and most contributors say badges do not influence them at all. Quote the direction, not a spin, when a maintainer resists cutting the row.

## Step 7 — Fix repository furniture and render mechanics

Three things compete for this budget, and they are not close:

Efficiency, do first: furniture > render mechanics > terminal demo.

- Furniture is near-zero effort and buys the only text a reader sees before opening the repository: the description, website link and topics are what search listings carry, and the social preview is what unfurls when someone pastes the link into a chat.
- Render mechanics cost about an hour and buy the page working for readers who never see the code host's render — registry pages, terminals, screen readers.
- Terminal demo costs a week to produce well and then becomes a standing job, going stale whenever the output changes.

The demo is what this order starves, and it is the highest-value element for a CLI or a visual tool, where the output is the product. Promote it above render mechanics in exactly that case, and generate it from a script rather than hand-recording it, so re-rendering stays cheap. Delete it for a library with no visible output rather than leaving scope behind.

Then fix how the file renders:

- Give every image alt text, and move any instruction, command or decision-relevant fact out of screenshots and animated demos into text. Readers meet READMEs in terminals, on registries that strip HTML, and through screen readers.
- Delete a hand-written table of contents. Code hosts generate an outline from headings, and the manual copy goes stale.
- Check relative links resolve from the repository root on the default branch, and that the page still reads where raw HTML is stripped.
- Keep only one rendered README. Where a host renders a `.github/` copy in preference to the root file, the root copy is what registries and mirrors publish, so the two silently diverge.
- In a monorepo, make the root README a router to the per-package READMEs rather than covering every package inline.
- When the demo earns its place, keep it short, high-contrast and legible at embed scale, and place it right after the tagline. Treat its benefit as practitioner consensus, not a measured result.

## Step 8 — Add enterprise trust signals, only if the audience calls for them

Run this step only when Step 1 declared a company or procurement audience. An enterprise decision-maker optimizes for defensibility, not best technical fit, so recognizable third-party signals — a foundation tier, an audit, an attestation, a well-known adopter — outperform novel claims. Published evaluation checklists weight maintenance activity, licence clarity and security posture above presentation quality.

Efficiency, do first: support expectation == release cadence > security policy > named adopters > governance and maintainer depth > supply-chain attestation > foundation affiliation.

- Support expectation and release cadence tie: each is one sentence stating something already true, needing nobody's permission.
- A security policy commits you publicly to a response window you then have to honour.
- Named adopters need each company's own marketing approval, revocable only by asking again.
- Foundation affiliation is the strongest signal on the page and a quarter or more of work, so it never wins on ratio. Promote it when the project is adopted as infrastructure rather than a dependency, or when a foundation tier is the objection you keep losing to — then hand that decision to the user, because its reversibility cost is not a documentation cost.

Default to the first three, an afternoon between them. Delete every signal the ceiling rules out. No legal appetite means no foundation row; a solo maintainer writes an honest support expectation rather than an empty governance heading.

## What to track afterwards

Attribution on a README is weak. Record the ship date, compare a full period before against a full period after, and annotate confounders instead of claiming the delta. Re-measure four to six weeks out; shorter windows are noise.

Efficiency, track first: support load > conversion rate > contributor conversion.

- Support load costs nothing and moves within weeks: count the "how do I install this" and "what does this do" issues per month.
- Conversion rate — clones or downloads divided by unique visitors — is the truest single number available, but says nothing until a full period has passed either side.
- Contributor conversion is slowest and most confounded; read it a quarter out.

Drop stars from the tracking plan entirely, even when the user named them as the goal. They only go up, so the metric cannot show a regression and reports success for a change that made the page worse. Offer the conversion rate instead.

If clones rise but contributor count does not, the contribution path is broken, not the README.

## Common failure modes

- Rewriting before diagnosing. A rewrite that fixes the prose and preserves the broken install has fixed nothing. Do not rewrite in audit mode unless asked.
- Padding to look serious. A four-section README for a single-purpose project is complete; adding architecture and roadmap sections to a 200-line utility makes it look abandoned, not mature.
- Marketing voice. Superlatives without evidence read as noise and lower trust.
- Auditing only one render target. The registry page often has more traffic and different rules.
- Fabricated status. Never write "production ready", "battle-tested", or a user count you did not get from the user. One glance at the commit history disproves it.
- Leading with the cheapest fix. The badge row is the fastest thing on the list and nearly the least valuable. Present the efficiency order, not the order you could finish first.

Related: this skill pairs with launch posts and announcement writing, docs-site and getting-started pages, and profile READMEs. When the real problem is one of those, do that work instead of stretching this page to cover it.

