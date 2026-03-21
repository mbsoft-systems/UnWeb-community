# Batch Processing

Convert multiple HTML files or URLs to markdown in bulk.

## Shell Scripts

### Convert Multiple URLs

```bash
#!/bin/bash
API_KEY="unweb_your_key_here"
URLS=(
  "https://example.com/page1"
  "https://example.com/page2"
  "https://example.com/page3"
)

for url in "${URLS[@]}"; do
  filename=$(echo "$url" | sed 's|https\?://||; s|/|_|g').md
  echo "Converting: $url -> $filename"

  unweb-cli convert url "$url" --output "$filename"
done
```

### Convert All HTML Files in a Directory

```bash
#!/bin/bash
for file in *.html; do
  echo "Converting: $file"
  unweb-cli convert upload "$file" --output "${file%.html}.md"
done
```

### Convert URLs from a File

```bash
#!/bin/bash
# urls.txt — one URL per line
while IFS= read -r url; do
  [ -z "$url" ] && continue
  filename=$(basename "$url").md
  echo "Converting: $url"
  unweb-cli convert url "$url" --output "$filename"
done < urls.txt
```

## Python

### Batch Convert with Rate Limiting

```python
import requests
import time
import os

API_KEY = os.environ.get("UNWEB_API_KEY", "unweb_your_key_here")
BASE_URL = "https://api.unweb.info"

urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
]

for url in urls:
    response = requests.post(
        f"{BASE_URL}/api/convert/url",
        headers={"X-API-Key": API_KEY},
        json={"url": url}
    )

    if response.status_code == 200:
        filename = url.split("/")[-1] + ".md"
        with open(filename, "w") as f:
            f.write(response.json()["markdown"])
        print(f"Saved: {filename}")
    elif response.status_code == 429:
        print("Quota exceeded — stopping.")
        break
    else:
        print(f"Error converting {url}: {response.status_code}")

    time.sleep(0.5)  # be nice to the API
```

### Convert All HTML Files

```python
import requests
import glob
import os

API_KEY = os.environ.get("UNWEB_API_KEY", "unweb_your_key_here")

for filepath in glob.glob("*.html"):
    with open(filepath, "rb") as f:
        response = requests.post(
            "https://api.unweb.info/api/convert/upload",
            headers={"X-API-Key": API_KEY},
            files={"file": (filepath, f, "text/html")}
        )

    if response.status_code == 200:
        output = filepath.replace(".html", ".md")
        with open(output, "w") as f:
            f.write(response.json()["markdown"])
        print(f"{filepath} -> {output}")
    else:
        print(f"Error: {filepath} ({response.status_code})")
```

## Tips

- **Rate limiting:** Add a short delay between requests to avoid hitting rate limits.
- **Quota awareness:** Check for 429 responses and stop gracefully.
- **JSON output:** Use `--format json` (CLI) to get structured output for further processing.
- **Error handling:** Some URLs may fail (404, timeout). Log failures and continue.

## Next Steps

- [API Usage](api-usage.md) — full API reference
- [Integration Examples](../examples/) — n8n workflows and more
