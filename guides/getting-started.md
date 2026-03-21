# Getting Started with UnWeb

This guide walks you through signing up, getting an API key, and making your first HTML-to-Markdown conversion.

## 1. Create an Account

Go to [app.unweb.info](https://app.unweb.info) and register with your email address.

## 2. Create an API Key

1. Log in to the dashboard
2. Navigate to **API Keys**
3. Click **Create New API Key**
4. Copy the key — it starts with `unweb_` and is only shown once

## 3. Make Your First Conversion

Pick whichever method suits you best:

### Option A: CLI

```bash
# Install (Linux/macOS)
curl -L https://github.com/mbsoft-systems/unweb-community/releases/latest/download/unweb-cli-linux-amd64 -o unweb-cli
chmod +x unweb-cli
sudo mv unweb-cli /usr/local/bin/

# Configure
unweb-cli init --api-key unweb_your_key_here

# Convert
unweb-cli convert url https://example.com
```

See the [CLI Quickstart](cli-quickstart.md) for full details.

### Option B: API with cURL

```bash
curl -X POST https://api.unweb.info/api/convert/url \
  -H "X-API-Key: unweb_your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

See the [API Usage Guide](api-usage.md) for Python, JavaScript, and more examples.

### Option C: Browser Extension

Install the Chrome or Firefox extension and click the UnWeb icon on any page. See the [Browser Extensions Guide](browser-extensions.md).

## What Happens During Conversion

UnWeb doesn't just dump raw HTML into markdown. It:

1. **Extracts main content** — finds the article/main element and ignores navigation, footers, sidebars
2. **Converts to CommonMark** — produces clean, standard markdown
3. **Cleans up** — removes excessive whitespace and formatting artifacts

## Next Steps

- [CLI Quickstart](cli-quickstart.md) — full CLI reference and configuration
- [API Usage](api-usage.md) — direct API integration
- [Batch Processing](batch-processing.md) — convert multiple pages at once
- [Integration Examples](../examples/) — ready-to-use code for n8n, Python, and more
