# AI Marketing Toolkit

An open-source toolkit for agentic marketing - for those who like to experiment with the latest tools.

Built for SEO, positioning, competitive research, and content ops.

[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](./LICENSE.md)
![Skills: 22](https://img.shields.io/badge/skills-22-6f42c1)
![Format: SKILL.md](https://img.shields.io/badge/format-SKILL.md-2ea44f)
![Tools: mise](https://img.shields.io/badge/tools-mise-6E4C13)

> **New here?** [Subscribe to The Agentic Marketer](https://the-agentic-marketer.beehiiv.com/subscribe) — new trends and tools, early access to LeadsDB, and reporting on what's actually working in agentic marketing.

## Quick start

```bash
git clone https://github.com/IsaacBell/ai-marketing-toolkit

# drop a single skill into Claude Code
cp -R ai-marketing-toolkit/skills/keyword-research ~/.claude/skills/

# or link the whole collection into a Kilo/agent skills dir
ln -s "$PWD/ai-marketing-toolkit/skills" ~/.agents/skills/ai-marketing-toolkit
```

The `pexels` skill needs a free API key:

```bash
export PEXELS_API_KEY="..."   # https://www.pexels.com/api/
```

## Skills

### SEO & marketing

| Skill | Does |
| --- | --- |
| `seo-project-setup` | Sets up a durable local SEO workspace with context, goals, and data intake. |
| `seo-audit` | Produces a one-page, plain-language SEO report with one action to take this week. |
| `seo-coach` | Friendly coach mode that explains workflows and recommends next steps. |
| `keyword-research` | Finds keyword opportunities, evaluates metrics/SERPs, saves promising terms. |
| `keyword-clustering` | Clusters keywords by intent and maps them to pages. |
| `competitor-analysis` | Analyzes one competitor's organic footprint, keywords, and gaps. |
| `competitive-landscape` | Maps market leaders, winning themes, coverage, and strategic gaps. |
| `openseo-review-web-content` | Writes and reviews on-brand web/blog/feature copy. |
| `openseo-release-notes` | Cuts a release: version bump, notes from commits, review pass, PR. |

### Positioning & voice

| Skill | Does |
| --- | --- |
| `Voice and Positioning` | Builds a Voice Constraint System to keep a consistent writing voice across many runs. |
| `Social Signal` | Template for social posts and getting a recommended next action. |

### Engineering workflow

| Skill | Does |
| --- | --- |
| `safe-refactor` | Restructures code while preserving behavior, bracketed by verification. |
| `surgical-patch` | Fixes bugs at the narrowest responsible layer. |
| `verify-and-stop` | Proves work meets acceptance criteria without expanding scope. |
| `migration` | Reversible, compatibility-safe schema/data/API/dependency migrations. |
| `modern-css` | Authors and reviews modern, responsive, accessible CSS. |
| `neon` | Works with Neon Postgres (branching, claims, env handling). |
| `wp-plugin-development` | WordPress plugin architecture, hooks, security, and packaging. |
| `mermaid` | Authors Mermaid diagrams across the full diagram catalog. |

### Communication & utilities

| Skill | Does |
| --- | --- |
| `caveman` | Ultra-compressed output mode that reduces AI costs, often by over half. |
| `caveman-commit` | Caveman-style commit messages. |
| `pexels` | Searches and fetches royalty-free stock photos from Pexels. |

## Stay in the loop

[**The Agentic Marketer**](https://the-agentic-marketer.beehiiv.com/subscribe) — This is also where LeadsDB early access previews go out.

## Repo layout

```
skills/       SKILL.md definitions, references, and helper scripts
mise.toml     pinned tool versions and repo tasks
.github/      CI, security scans, dependabot, funding
```

## Tasks

[mise](https://mise.jdx.dev/) manages the toolchain and repo tasks:

```bash
mise install                             # install pinned tools
mise run check                           # validate mise config, shell scripts, skill frontmatter
mise run gate                            # security gate (dependency compromise scan)
mise run img-search-pexels "sunset" --count 30   # requires PEXELS_API_KEY
```

## License

[ISC](./LICENSE.md).

Vendored skills keep their upstream terms: `mermaid` is MIT (see [LICENSE.md](./LICENSE.md)), and `pexels` is inspired by [amalshehu/pexels-skill](https://github.com/amalshehu/pexels-skill).
