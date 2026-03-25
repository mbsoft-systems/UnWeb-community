# Browser Extensions

Convert any webpage to markdown with one click using the UnWeb browser extension.

## Availability

- **Chrome** (Manifest V3) — [Install from Chrome Web Store](https://chromewebstore.google.com/detail/unweb-html-to-markdown/belfnjbbagbongfjandjecgpfkeabnjn)
- **Firefox** (Manifest V2) — [Install from Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/unweb-html-to-markdown/)

## Features

- One-click conversion of the current page
- Automatic main content extraction
- Copy markdown to clipboard
- Download as `.md` file
- API key authentication
- Usage tracking display

## Manual Installation (Developer Mode)

Until the extensions are published to the stores, you can install them manually.

### Chrome

1. Download the Chrome extension files from the project
2. Open `chrome://extensions/` in Chrome
3. Enable **Developer mode** (toggle in top-right)
4. Click **Load unpacked**
5. Select the Chrome extension directory

### Firefox

1. Download the Firefox extension files from the project
2. Open `about:debugging#/runtime/this-firefox` in Firefox
3. Click **Load Temporary Add-on**
4. Select `manifest.json` from the Firefox extension directory

**Note:** Temporary add-ons in Firefox are removed when the browser closes.

## Setup

1. Click the UnWeb extension icon in your browser toolbar
2. Enter your API key (get one from [app.unweb.info](https://app.unweb.info))
3. Click **Save**

## Usage

1. Navigate to any webpage
2. Click the UnWeb icon
3. Click **Convert**
4. Copy the markdown or download as a `.md` file

## Next Steps

- [Getting Started](getting-started.md) — full setup walkthrough
- [API Usage](api-usage.md) — use the API directly from code
