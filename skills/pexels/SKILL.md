---
name: pexels
inspired by: https://github.com/amalshehu/pexels-skill
description: Search and fetch royalty-free stock photos from the Pexels API. Use when the user asks to find stock photos, seed placeholder/demo/seed images, populate a gallery, or needs real royalty-free imagery for a project (e.g. "find me 5 photos of X", "get stock images for the hero section", "seed images from Pexels").
---

# Pexels

Fetches real, royalty-free stock photos from the Pexels API for use as placeholder, demo, or seed content. Never fabricate photo URLs — always fetch from the live API via this skill.

## Usage

```bash
bash ~/.claude/skills/pexels/scripts/search.sh "search query" [count] [orientation]
```

- `query` (required): search term, e.g. `"surfing sunset beach"`.
- `count` (optional, default 10, max 80): number of results.
- `orientation` (optional): `landscape`, `portrait`, or `square`.

Returns JSON: `{ total_results, photos: [{ id, photographer, url, src: { large, original, medium } }] }`.

Run one search per distinct visual theme needed (e.g. separate calls for "yoga sunrise cliff" vs "surf sunset beach") rather than one broad query, so results stay relevant per use case.

## Notes

- `src.large` (~940px wide) is the right default for web use; `src.original` is full resolution, `src.medium` for thumbnails.
- Images are served from `images.pexels.com`. If hotlinking directly in a Next.js `<Image>` component, that hostname must be added to the project's `next.config`'s `images.remotePatterns` or rendering will fail.
- Attribution isn't legally required by Pexels but is appreciated — use `photographer` from the response if crediting in UI.
- Requires the `PEXELS_API_KEY` env var (free key: https://www.pexels.com/api/). Never hardcode it into this script.
