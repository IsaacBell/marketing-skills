#!/usr/bin/env python3
# fal.ai synchronous image generation (https://fal.run/{model}).
# Set FAL_API_KEY in the environment, then:
#   uv run --no-project python fal_image.py "prompt" -o out.png
#
# Auth: Authorization: Key $FAL_API_KEY
# Response shape (image models): {"images": [{"url": ..., "width":.., "height":..}], ...}

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_MODEL = "fal-ai/flux/schnell"
TIMEOUT_SECONDS = 120


MODEL_ID = re.compile(r"^[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*$")


def run_model(api_key, model, payload):
    if not MODEL_ID.match(model) or ".." in model:
        print("Invalid model id: {}".format(model), file=sys.stderr)
        return 1, None
    url = "https://fal.run/{}".format(model)
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Authorization": "Key {}".format(api_key),
            "Content-Type": "application/json",
        },
    )

    try:
        # url is the fixed https://fal.run host plus a model id validated by MODEL_ID
        # nosemgrep
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            response_body = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        response_body = exc.read().decode("utf-8", errors="replace")
        print("HTTP error {}: {}".format(exc.code, response_body), file=sys.stderr)
        return 1, None
    except urllib.error.URLError as exc:
        print("Request failed: {}".format(exc), file=sys.stderr)
        return 1, None

    try:
        return 0, json.loads(response_body)
    except json.JSONDecodeError as exc:
        print("Invalid JSON response: {}".format(exc), file=sys.stderr)
        return 1, None


def download(url, dest):
    """Save one image. Returns True on success; never follows a non-https URL."""
    if urllib.parse.urlparse(str(url)).scheme != "https":
        print("Refusing to download a non-https URL: {}".format(url), file=sys.stderr)
        return False
    try:
        # the scheme is checked as https above, so file:// is refused
        # nosemgrep
        urllib.request.urlretrieve(url, dest)
    except (urllib.error.URLError, OSError) as exc:
        print("Download failed for {}: {}".format(dest, exc), file=sys.stderr)
        return False
    return True


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Generate an image with fal.ai and save it to disk."
    )
    parser.add_argument("prompt", help="Text prompt")
    parser.add_argument("-o", "--out", default="fal-output.png", help="Output file path")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="fal model id")
    parser.add_argument(
        "--image-size",
        default="square_hd",
        help="fal image_size value (e.g. square_hd, landscape_16_9, portrait_4_3)",
    )
    parser.add_argument("--num-images", type=int, default=1)
    parser.add_argument("--json", action="store_true", help="Print raw API JSON instead of saving")
    return parser.parse_args(argv)


def main(argv):
    args = parse_args(argv)

    api_key = os.environ.get("FAL_API_KEY", "").strip()
    if not api_key:
        print(
            "FAL_API_KEY is not set. Export FAL_API_KEY before running.",
            file=sys.stderr,
        )
        return 2

    payload = {
        "prompt": args.prompt,
        "image_size": args.image_size,
        "num_images": args.num_images,
    }

    code, data = run_model(api_key, args.model, payload)
    if code:
        return code

    if args.json:
        print(json.dumps(data, ensure_ascii=False, sort_keys=True))
        return 0

    images = data.get("images") or []
    if not images:
        print("No images in response: {}".format(json.dumps(data)), file=sys.stderr)
        return 1

    if len(images) == 1:
        if not download(images[0].get("url"), args.out):
            return 1
        print(args.out)
    else:
        root, ext = os.path.splitext(args.out)
        for i, img in enumerate(images):
            dest = "{}-{}{}".format(root, i, ext or ".png")
            if not download(img.get("url"), dest):
                return 1
            print(dest)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
