# UnWeb

**Convert any HTML to clean Markdown.** API, CLI, browser extensions, and integrations for automation workflows.

[![CLI Release](https://img.shields.io/github/v/release/mbsoft-systems/unweb-community?label=CLI&style=flat-square)](https://github.com/mbsoft-systems/unweb-community/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

## What is UnWeb?

UnWeb converts HTML to clean [CommonMark](https://commonmark.org/) markdown. It automatically extracts the main content from full webpages — stripping navigation, footers, and boilerplate — giving you just the content you need.

**Use cases:**
- Convert web pages to markdown for LLM context
- Archive articles and documentation in a readable format
- Build content pipelines with n8n, Make, or custom scripts
- Feed web content into AI agents and workflows

## Quick Links

| Resource | Link |
|----------|------|
| Dashboard | [app.unweb.info](https://app.unweb.info) |
| API Reference | [docs.unweb.info](https://docs.unweb.info) |
| CLI Releases | [GitHub Releases](https://github.com/mbsoft-systems/unweb-community/releases) |
| Browser Extensions | [Chrome](https://chromewebstore.google.com/detail/unweb-html-to-markdown/belfnjbbagbongfjandjecgpfkeabnjn) · [Firefox](https://addons.mozilla.org/en-US/firefox/addon/unweb-html-to-markdown/) |
| Landing Page | [unweb.info](https://unweb.info) |

## Getting Started

1. **Sign up** at [app.unweb.info](https://app.unweb.info) and create an API key
2. **Pick your tool** — CLI, API, browser extension, or an integration
3. **Convert** — pass HTML or a URL, get clean markdown back

See the full [Getting Started Guide](guides/getting-started.md) for a detailed walkthrough.

## Guides

| Guide | Description |
|-------|-------------|
| [Getting Started](guides/getting-started.md) | Sign up, get an API key, make your first conversion |
| [CLI Quickstart](guides/cli-quickstart.md) | Install the CLI, configure it, and convert pages |
| [API Usage](guides/api-usage.md) | Use the API directly with cURL, Python, or JavaScript |
| [Batch Processing](guides/batch-processing.md) | Convert multiple files or URLs in bulk |
| [Browser Extensions](guides/browser-extensions.md) | Install and use the Chrome/Firefox extensions |

## Integration Examples

Ready-to-use examples for connecting UnWeb to your tools.

| Integration | Description | Status |
|-------------|-------------|--------|
| [n8n](examples/n8n/) | Automate conversions in n8n workflows | Available |
| [Python](examples/python/) | Python scripts for common conversion tasks | Available |
| [JavaScript](examples/javascript/) | Node.js conversion examples | Available |
| [cURL / Shell](examples/curl/) | Shell scripts for API calls | Available |
| [Make](examples/make/) | Integromat/Make scenarios | Coming soon |
| [Zapier](examples/zapier/) | Zapier zap templates | Coming soon |

## Browser Extensions

Convert any webpage to markdown with one click.

- **Chrome** — [Install from Chrome Web Store](https://chromewebstore.google.com/detail/unweb-html-to-markdown/belfnjbbagbongfjandjecgpfkeabnjn)
- **Firefox** — [Install from Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/unweb-html-to-markdown/)

See the [Browser Extensions Guide](guides/browser-extensions.md) for setup and usage.

## Announcements

See [ANNOUNCEMENTS.md](ANNOUNCEMENTS.md) for major updates and breaking changes.

**Latest:**
- **2026-03-25** — Browser extensions published on Chrome Web Store and Firefox Add-ons.
- **2026-03-12** — UnWeb launched! API, dashboard, and CLI now available.

## Support & Contributing

- **Bug reports:** [Open an issue](https://github.com/mbsoft-systems/unweb-community/issues/new?template=bug_report.md)
- **Feature requests:** [Open an issue](https://github.com/mbsoft-systems/unweb-community/issues/new?template=feature_request.md)
- **Integration examples:** PRs welcome to the `examples/` directory
- **API reference:** [docs.unweb.info](https://docs.unweb.info)

## License

MIT — see [LICENSE](LICENSE).
