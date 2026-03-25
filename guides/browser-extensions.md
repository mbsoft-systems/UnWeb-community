# Browser Extensions

Convert any webpage to markdown with one click using the UnWeb browser extension.

## Install

- **Chrome** — [Install from Chrome Web Store](https://chromewebstore.google.com/detail/unweb-html-to-markdown/belfnjbbagbongfjandjecgpfkeabnjn)
- **Firefox** — [Install from Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/unweb-html-to-markdown/)

## Features

- One-click conversion of the current page
- Automatic main content extraction
- Copy markdown to clipboard
- Download as `.md` file
- API key authentication
- Usage tracking display

## Setup

1. Install the extension from the link above
2. Click the UnWeb extension icon in your browser toolbar
3. Enter your API key (get one from [app.unweb.info](https://app.unweb.info))
4. Click **Save**

## Usage

1. Navigate to any webpage
2. Click the UnWeb icon
3. Click **Convert**
4. Copy the markdown or download as a `.md` file

## Manual Installation (Developer Mode)

If you prefer to load the extension from source:

### Chrome

1. Open `chrome://extensions/`
2. Enable **Developer mode** (toggle in top-right)
3. Click **Load unpacked**
4. Select the `browser-extensions/src/chrome` directory

### Firefox

1. Open `about:debugging#/runtime/this-firefox`
2. Click **Load Temporary Add-on**
3. Select `manifest.json` from the `browser-extensions/src/firefox` directory

**Note:** Temporary add-ons in Firefox are removed when the browser closes.

## Next Steps

- [Getting Started](getting-started.md) — full setup walkthrough
- [API Usage](api-usage.md) — use the API directly from code
