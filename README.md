# UnWeb

**Convert any HTML to clean Markdown.** UnWeb is an HTML-to-Markdown conversion API with a CLI, browser extensions, and integrations for automation workflows.

[![CLI Release](https://img.shields.io/github/v/release/mbsoft-systems/unweb-community?label=CLI&style=flat-square)](https://github.com/mbsoft-systems/unweb-community/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

## What is UnWeb?

UnWeb converts HTML content to clean [CommonMark](https://commonmark.org/) markdown. It automatically extracts main content from full webpages, stripping navigation, footers, and boilerplate — giving you just the content you need.

**Use cases:**
- Convert web pages to markdown for LLM context
- Archive articles and documentation in a readable format
- Build content pipelines with n8n, Make, or custom scripts
- Feed web content into AI agents and Claude skills

## Getting Started

### 1. Get an API Key

Sign up at [app.unweb.info](https://app.unweb.info) and create an API key from the dashboard.

**Pricing:**

| Plan | Conversions/month | Price |
|------|-------------------|-------|
| Free | 100 | $0 |
| Pro | 1,000 | $9/mo |
| Enterprise | 10,000 | $29/mo |

### 2. Install the CLI

Download the latest binary for your platform from [Releases](https://github.com/mbsoft-systems/unweb-community/releases).

**Linux / macOS:**
```bash
# Download (replace with your platform)
curl -L https://github.com/mbsoft-systems/unweb-community/releases/latest/download/unweb-cli-linux-amd64 -o unweb-cli
chmod +x unweb-cli
sudo mv unweb-cli /usr/local/bin/

# Initialize
unweb-cli init --api-key unweb_your_key_here
```

**Windows:**

Download `unweb-cli-windows-amd64.exe` from [Releases](https://github.com/mbsoft-systems/unweb-community/releases), rename to `unweb-cli.exe`, and add to your PATH.

### 3. Convert

```bash
# Convert a URL to markdown
unweb-cli convert url https://example.com/article

# Convert inline HTML
unweb-cli convert paste "<h1>Hello</h1><p>World</p>"

# Convert an HTML file
unweb-cli convert upload document.html

# Save to file
unweb-cli convert url https://example.com --output article.md

# JSON output (for scripting)
unweb-cli convert url https://example.com --format json
```

## API

The UnWeb API is available at `https://api.unweb.info`. Authenticate with your API key in the `X-API-Key` header.

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/convert/paste` | Convert HTML from request body |
| `POST` | `/api/convert/upload` | Convert an uploaded HTML file |
| `POST` | `/api/convert/url` | Convert HTML from a URL |

### Example: cURL

```bash
# Convert inline HTML
curl -X POST https://api.unweb.info/api/convert/paste \
  -H "X-API-Key: unweb_your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"html": "<h1>Hello World</h1><p>This is a test.</p>"}'

# Convert from URL
curl -X POST https://api.unweb.info/api/convert/url \
  -H "X-API-Key: unweb_your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/article"}'
```

### Example: Python

```python
import requests

response = requests.post(
    "https://api.unweb.info/api/convert/url",
    headers={"X-API-Key": "unweb_your_key_here"},
    json={"url": "https://example.com/article"}
)

markdown = response.json()["markdown"]
print(markdown)
```

### Example: JavaScript

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

## CLI Reference

### Commands

| Command | Description |
|---------|-------------|
| `unweb-cli init --api-key KEY` | Save API key to config |
| `unweb-cli convert paste "HTML"` | Convert inline HTML |
| `unweb-cli convert paste --file FILE` | Convert HTML from file |
| `unweb-cli convert upload FILE` | Upload and convert HTML file |
| `unweb-cli convert url URL` | Convert webpage from URL |
| `unweb-cli version` | Show version |

### Flags

| Flag | Environment Variable | Description |
|------|---------------------|-------------|
| `--api-key` | `UNWEB_API_KEY` | API key for authentication |
| `--base-url` | `UNWEB_BASE_URL` | API base URL (default: `https://api.unweb.info`) |
| `--output` | — | Output file path (default: stdout) |
| `--format` | — | Output format: `markdown`, `json` |
| `--verbose` | — | Enable verbose logging |
| `--no-color` | — | Disable colored output |

### Configuration

The CLI reads config from `~/.unweb/config.yaml`. Priority order:

1. Command-line flags
2. Environment variables
3. Config file
4. Defaults

### Batch Processing

```bash
# Convert multiple URLs
for url in https://example.com/page1 https://example.com/page2; do
  unweb-cli convert url "$url" --output "$(basename $url).md"
done

# Convert all HTML files in a directory
for file in *.html; do
  unweb-cli convert upload "$file" --output "${file%.html}.md"
done
```

## Integrations

Community-contributed examples for using UnWeb in automation workflows.

| Integration | Description | Status |
|------------|-------------|--------|
| n8n workflows | Automate HTML-to-Markdown conversion in n8n | Coming soon |
| Claude Code skills | Use UnWeb in Claude Code AI workflows | Coming soon |

See the [`examples/`](examples/) directory for integration guides and templates.

## Browser Extensions

Convert any webpage to markdown with one click.

- **Chrome** (Manifest V3) — Coming soon to Chrome Web Store
- **Firefox** (Manifest V2) — Coming soon to Firefox Add-ons

## Links

- **Landing page:** [unweb.info](https://unweb.info)
- **Dashboard:** [app.unweb.info](https://app.unweb.info)
- **API:** [api.unweb.info](https://api.unweb.info)
- **Documentation:** [docs.unweb.info](https://docs.unweb.info)

## Contributing

We welcome bug reports, feature requests, and integration examples.

- **Bug reports:** [Open an issue](https://github.com/mbsoft-systems/unweb-community/issues/new?template=bug_report.md)
- **Feature requests:** [Open an issue](https://github.com/mbsoft-systems/unweb-community/issues/new?template=feature_request.md)
- **Integration examples:** Submit a PR to the `examples/` directory

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
