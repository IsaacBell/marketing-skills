---
name: generate-fal-image
description: "Generate a marketing image with the fal API from an agent session. Use when a task needs an original image created and saved to disk (hero art, social card, illustration, product mock) and no suitable existing asset is available."
---

# Generate an image with fal

Create one or more images from a text prompt by POSTing to the fal synchronous endpoint, then download the result to a path the caller chooses. The bundled `scripts/fal_image.py` does the whole round trip; this skill says when and how to run it and what to check afterwards.

## Inputs

Three inputs decide the run:

- **Prompt** - a plain text description of the image the caller wants.
- **Output path** - where the image is written. Pick a real folder in the project; the file lands there.
- **Model** - the fal model id. The default is `fal-ai/flux/schnell`, a fast text-to-image model good enough for drafts and social cards. Pass another id for higher fidelity or a different style.

## Run the script

```
uv run --no-project python scripts/fal_image.py "a flat illustration of a desk with a laptop, warm palette, generous negative space at the top" -o assets/hero.png
```

Flags:

- `-o, --out` - output file path (default `fal-output.png`). With more than one image, the script appends `-0`, `-1`, ... before the extension.
- `--model` - fal model id (default `fal-ai/flux/schnell`).
- `--image-size` - fal `image_size` value, e.g. `square_hd`, `landscape_16_9`, `portrait_4_3` (default `square_hd`).
- `--num-images` - how many images to generate (default 1).
- `--json` - print the raw API response instead of downloading; use it to inspect sizes and URLs before saving.

On success the script prints the path of each saved file, one per line, and exits 0.

## The API key

The script reads the fal key from an environment variable the user provides, `FAL_API_KEY`, and sends it as an `Authorization: Key <value>` header. Never hard-code the key, put it in a committed file, or print it. If `FAL_API_KEY` is unset the script exits 2 with a message; ask the user to supply the variable in the session and re-run.

## Prompt tips for marketing imagery

- Lead with the subject and what it is doing, then composition, lighting, palette and style. A short ordered sentence beats a keyword pile.
- Name the aspect ratio in words and match `--image-size` to it, so the framing the model draws matches the crop you will use.
- Leave negative space and say where ("clear area on the left") if copy, a logo or a headline will sit over the image.
- Do not ask the model to render words, logos or numbers: text-to-image models garble them. Generate the picture, add the type in the layout.
- Be specific about brand-adjacent cues such as colour names, mood, era and materials. Vague prompts return stock-looking output.
- Generate several candidates (`--num-images 3`) and pick. On a cheap model, iterating beats over-tuning one prompt.

## Check the result before using it

1. The file exists and is not empty: `ls -l <path>`. A zero-byte or missing file means the download failed even if the API call succeeded.
2. Dimensions are what was asked: `file <path>` prints the pixel size. Confirm the aspect ratio matches `--image-size`.
3. No garbled text: open the image and look. If the prompt asked for words, they will be misspelled; treat that as expected and add the type in the layout.
4. The image depicts the subject. Models drop requested elements; re-prompt rather than shipping a wrong picture.

Report the saved path and its dimensions to the caller, and flag any check that failed.
