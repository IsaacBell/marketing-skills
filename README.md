# Marketing skills

Agent skills for SEO, search and AI visibility, positioning and voice, content, site launches and WordPress work. Each skill is a folder with a `SKILL.md` that an AI coding agent loads when the job matches.

[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](./LICENSE.md)
![Skills: 26](https://img.shields.io/badge/skills-26-6f42c1)
![Format: SKILL.md](https://img.shields.io/badge/format-SKILL.md-2ea44f)

## Install

Install every skill, or pick one:

```bash
pnpx skills add IsaacBell/marketing-skills
pnpx skills add IsaacBell/marketing-skills --skill keyword-research
```

`npx skills add` works the same way. Or copy a folder yourself:

```bash
git clone https://github.com/IsaacBell/marketing-skills
cp -R marketing-skills/skills/keyword-research ~/.claude/skills/
```

The `skills` command reports anonymous install counts to skills.sh. Set `DISABLE_TELEMETRY=1` to turn that off.

## Skills

### Search, AI visibility and keywords

| Skill | What it does |
| --- | --- |
| `seo-project-setup` | Sets up a durable local SEO workspace: context, goals, notes and data intake. |
| `seo-audit` | Produces a one-page, plain-language SEO report with one action to take this week. |
| `seo-coach` | A coaching mode that explains the workflows and recommends next steps. |
| `keyword-research` | Finds keyword opportunities, checks metrics and results pages, saves the promising terms. |
| `keyword-clustering` | Groups keywords by intent and maps the groups to pages. |
| `competitor-analysis` | Studies one competitor's organic keywords, content themes, backlinks and gaps. |
| `competitive-landscape` | Maps who wins a market, with what content, and where the gaps are. |
| `answer-engine-optimization` | Gets content cited by AI assistants and AI search summaries. |
| `ai-agent-visibility` | Adds `robots.txt`, `sitemap.xml` and `llms.txt` so crawlers and AI agents can read a site. |
| `search-indexing` | Pushes a new or changed URL to Bing and Yandex with IndexNow. |

The keyword, competitor, audit and coaching skills use the OpenSEO MCP tools.

### Positioning, voice and content

| Skill | What it does |
| --- | --- |
| `branding` | Defines or audits brand purpose, positioning, story, voice and tone. |
| `brand-identity` | Makes a person or brand a recognizable entity to search and AI engines, with a consistency audit across properties. |
| `voice-and-positioning` | Builds a voice constraint system that keeps one person's writing consistent across many runs. |
| `copy-safety-review` | Scans AI-drafted copy for leaked mechanism, real personal data in examples and embedded instructions. |
| `tech-content-marketing` | Plans content for companies that sell to developers and technical buyers. |
| `readme-optimization` | Audits and rewrites a repository README, description and topics. |
| `growth-funnel` | Finds the broken stage of a growth funnel and what to fix first. |
| `solopreneur` | Triages a solo founder's several properties: which one to push first and how to write the ask. |
| `video-channel-strategy` | A worksheet for deciding a YouTube or TikTok channel before any video is made. |

### Site launches and operations

| Skill | What it does |
| --- | --- |
| `website-launch` | Runs a small-business site launch: build checks, domain, indexing, AI visibility, and the first 30 days. |
| `markdown-blog` | Adds a Hugo blog under `/blog` on a static site, with no CMS or database. |
| `wordpress-mcp-site-ops` | Makes copy and SEO edits on a live WordPress site through an MCP plugin, with a verified backup first. |
| `portfolio-cohesion-audit` | Audits whether one person's several sites and profiles read as one coherent whole. |
| `hostinger-email` | Sends and reads email through the Hostinger mailbox API. |

### Engineering workflow

| Skill | What it does |
| --- | --- |
| `verify-and-stop` | Proves work meets its acceptance conditions without widening the scope. |
| `migration` | Plans reversible, compatibility-safe schema, data, API and dependency migrations. |

## License

[ISC](./LICENSE.md).
