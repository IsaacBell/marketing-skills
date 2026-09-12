#!/usr/bin/env bash
# https://github.com/amalshehu/pexels-skill/blob/master/scripts/search.sh
# Search the Pexels API. Usage: search.sh "<query>" [count] [orientation]
set -euo pipefail

QUERY="${1:?Usage: search.sh <query> [count] [orientation]}"
COUNT="${2:-10}"
ORIENTATION="${3:-}"

PEXELS_API_KEY="${PEXELS_API_KEY:?Set PEXELS_API_KEY (get one free at https://www.pexels.com/api/)}"

ARGS=(-G "https://api.pexels.com/v1/search" --data-urlencode "query=${QUERY}" --data-urlencode "per_page=${COUNT}")
if [ -n "$ORIENTATION" ]; then
  ARGS+=(--data-urlencode "orientation=${ORIENTATION}")
fi

curl -s "${ARGS[@]}" -H "Authorization: ${PEXELS_API_KEY}" | jq '{
  total_results,
  photos: [.photos[] | {
    id,
    photographer,
    url,
    src: { large: .src.large, original: .src.original, medium: .src.medium }
  }]
}'
