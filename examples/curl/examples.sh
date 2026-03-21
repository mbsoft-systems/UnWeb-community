#!/bin/bash
# UnWeb API examples using cURL.
# Set UNWEB_API_KEY environment variable before running.

API_KEY="${UNWEB_API_KEY:-unweb_your_key_here}"
BASE_URL="https://api.unweb.info"

echo "=== Convert inline HTML ==="
curl -s -X POST "$BASE_URL/api/convert/paste" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"html": "<h1>Hello World</h1><p>This is a paragraph.</p>"}'

echo -e "\n\n=== Convert from URL ==="
curl -s -X POST "$BASE_URL/api/convert/url" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'

echo -e "\n\n=== Upload HTML file ==="
echo "<h1>Test</h1><p>Uploaded content.</p>" > /tmp/test.html
curl -s -X POST "$BASE_URL/api/convert/upload" \
  -H "X-API-Key: $API_KEY" \
  -F "file=@/tmp/test.html"
rm -f /tmp/test.html

echo -e "\n\n=== Convert URL and save to file ==="
curl -s -X POST "$BASE_URL/api/convert/url" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}' | jq -r '.markdown' > output.md
echo "Saved to output.md"
