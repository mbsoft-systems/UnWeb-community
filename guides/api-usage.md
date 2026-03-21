# API Usage Guide

Use the UnWeb API directly to convert HTML to markdown from any language or tool.

## Base URL

```
https://api.unweb.info
```

## Authentication

Include your API key in the `X-API-Key` header with every request.

```
X-API-Key: unweb_your_key_here
```

Get an API key from [app.unweb.info](https://app.unweb.info) → API Keys.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/convert/paste` | Convert HTML from request body |
| `POST` | `/api/convert/upload` | Convert an uploaded HTML file |
| `POST` | `/api/convert/url` | Convert a webpage by URL |

## Convert HTML (paste)

Send HTML as a JSON string.

### cURL

```bash
curl -X POST https://api.unweb.info/api/convert/paste \
  -H "X-API-Key: unweb_your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"html": "<h1>Hello World</h1><p>This is a paragraph.</p>"}'
```

### Python

```python
import requests

response = requests.post(
    "https://api.unweb.info/api/convert/paste",
    headers={"X-API-Key": "unweb_your_key_here"},
    json={"html": "<h1>Hello World</h1><p>This is a paragraph.</p>"}
)

data = response.json()
print(data["markdown"])
```

### JavaScript

```javascript
const response = await fetch("https://api.unweb.info/api/convert/paste", {
  method: "POST",
  headers: {
    "X-API-Key": "unweb_your_key_here",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ html: "<h1>Hello World</h1><p>A paragraph.</p>" }),
});

const { markdown } = await response.json();
console.log(markdown);
```

## Convert from URL

Fetch a webpage and convert its main content to markdown.

### cURL

```bash
curl -X POST https://api.unweb.info/api/convert/url \
  -H "X-API-Key: unweb_your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/article"}'
```

### Python

```python
import requests

response = requests.post(
    "https://api.unweb.info/api/convert/url",
    headers={"X-API-Key": "unweb_your_key_here"},
    json={"url": "https://example.com/article"}
)

print(response.json()["markdown"])
```

### JavaScript

```javascript
const response = await fetch("https://api.unweb.info/api/convert/url", {
  method: "POST",
  headers: {
    "X-API-Key": "unweb_your_key_here",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ url: "https://example.com/article" }),
});

const { markdown } = await response.json();
console.log(markdown);
```

## Upload HTML File

Upload an `.html` or `.htm` file (max 5MB) as multipart form data.

### cURL

```bash
curl -X POST https://api.unweb.info/api/convert/upload \
  -H "X-API-Key: unweb_your_key_here" \
  -F "file=@document.html"
```

### Python

```python
import requests

with open("document.html", "rb") as f:
    response = requests.post(
        "https://api.unweb.info/api/convert/upload",
        headers={"X-API-Key": "unweb_your_key_here"},
        files={"file": ("document.html", f, "text/html")}
    )

print(response.json()["markdown"])
```

## Response Format

All endpoints return JSON:

```json
{
  "markdown": "# Hello World\n\nThis is a paragraph.",
  "warnings": []
}
```

The `warnings` array may contain messages about content extraction (e.g., fallback methods used).

## Error Responses

| Status | Meaning | Example |
|--------|---------|---------|
| 400 | Invalid request | Missing HTML, bad URL, wrong file type |
| 401 | Invalid API key | Key is wrong or revoked |
| 429 | Quota exceeded | Monthly conversion limit reached |
| 500 | Server error | Unexpected error during conversion |

Error response body:

```json
{
  "error": "Quota exceeded",
  "message": "You have used 100 out of 100 conversions this month."
}
```

## Next Steps

- [Batch Processing](batch-processing.md) — convert multiple pages programmatically
- [Integration Examples](../examples/) — ready-to-use scripts and workflows
