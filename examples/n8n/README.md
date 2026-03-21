# n8n Integration Examples

Use UnWeb in [n8n](https://n8n.io) workflows to automate HTML-to-Markdown conversion.

## Workflows

| Workflow | Description | File |
|----------|-------------|------|
| URL to Markdown | Convert a single URL to markdown | Coming soon |
| Batch Convert | Convert URLs from a spreadsheet or RSS feed | Coming soon |

## Setup

1. Get an API key from [app.unweb.info](https://app.unweb.info)
2. In n8n, use an **HTTP Request** node to call the UnWeb API
3. Configure the node:
   - **Method:** POST
   - **URL:** `https://api.unweb.info/api/convert/url`
   - **Headers:** `X-API-Key: unweb_your_key_here`
   - **Body (JSON):** `{"url": "{{ $json.url }}"}`

## Quick Example

Use an HTTP Request node with these settings:

```json
{
  "method": "POST",
  "url": "https://api.unweb.info/api/convert/url",
  "headers": {
    "X-API-Key": "unweb_your_key_here",
    "Content-Type": "application/json"
  },
  "body": {
    "url": "https://example.com/article"
  }
}
```

The response `{{ $json.markdown }}` contains the converted markdown.

## Contributing

Have an n8n workflow using UnWeb? Submit a PR with your `.json` workflow export.
