# CLI Quickstart

Install and use the UnWeb CLI to convert HTML to markdown from the command line.

## Installation

Download the latest binary for your platform from [Releases](https://github.com/mbsoft-systems/unweb-community/releases).

### Linux

```bash
curl -L https://github.com/mbsoft-systems/unweb-community/releases/latest/download/unweb-cli-linux-amd64 -o unweb-cli
chmod +x unweb-cli
sudo mv unweb-cli /usr/local/bin/
```

### macOS

```bash
# Intel
curl -L https://github.com/mbsoft-systems/unweb-community/releases/latest/download/unweb-cli-darwin-amd64 -o unweb-cli

# Apple Silicon
curl -L https://github.com/mbsoft-systems/unweb-community/releases/latest/download/unweb-cli-darwin-arm64 -o unweb-cli

chmod +x unweb-cli
sudo mv unweb-cli /usr/local/bin/
```

### Windows

Download `unweb-cli-windows-amd64.exe` from [Releases](https://github.com/mbsoft-systems/unweb-community/releases), rename to `unweb-cli.exe`, and add the folder to your PATH.

## Configuration

### Initialize with API Key

```bash
unweb-cli init --api-key unweb_your_key_here
```

This saves your key to `~/.unweb/config.yaml`.

### Environment Variables

Alternatively, set environment variables:

```bash
export UNWEB_API_KEY="unweb_your_key_here"
export UNWEB_BASE_URL="https://api.unweb.info"  # optional, this is the default
```

### Priority Order

Settings are applied in this order (highest wins):

1. Command-line flags (`--api-key`)
2. Environment variables (`UNWEB_API_KEY`)
3. Config file (`~/.unweb/config.yaml`)
4. Defaults

## Commands

### Convert from URL

```bash
unweb-cli convert url https://example.com/article
unweb-cli convert url https://example.com/article --output article.md
```

### Convert Inline HTML

```bash
unweb-cli convert paste "<h1>Hello</h1><p>World</p>"
unweb-cli convert paste --file input.html
```

### Upload HTML File

```bash
unweb-cli convert upload document.html
unweb-cli convert upload document.html --output result.md
```

Requirements: file must be `.html` or `.htm`, under 5MB.

### Show Version

```bash
unweb-cli version
```

## Flags

| Flag | Description |
|------|-------------|
| `--api-key` | API key (overrides config/env) |
| `--base-url` | API URL (default: `https://api.unweb.info`) |
| `--output` | Save to file instead of stdout |
| `--format` | Output format: `markdown` (default) or `json` |
| `--verbose` | Show detailed request/response info |
| `--no-color` | Disable colored output |

## JSON Output

Use `--format json` for scripting:

```bash
unweb-cli convert url https://example.com --format json
```

```json
{
  "markdown": "# Page Title\n\nContent here...",
  "warnings": []
}
```

## Error Messages

### Quota Exceeded (429)

```
Error: Quota exceeded
You have used 100 out of 100 conversions this month.
```

Upgrade your plan at [app.unweb.info](https://app.unweb.info) or wait for your quota to reset.

### Invalid API Key (401)

```
Error: Invalid API key
```

Check your key at [app.unweb.info](https://app.unweb.info) → API Keys, or run `unweb-cli init` again.

## Next Steps

- [Batch Processing](batch-processing.md) — convert multiple files or URLs
- [API Usage](api-usage.md) — use the API directly from code
