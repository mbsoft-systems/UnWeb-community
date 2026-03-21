/**
 * Basic UnWeb conversion examples.
 * Requires Node.js 18+ (uses built-in fetch).
 */

const API_KEY = process.env.UNWEB_API_KEY || "unweb_your_key_here";
const BASE_URL = "https://api.unweb.info";

async function convertHtml(html) {
  const response = await fetch(`${BASE_URL}/api/convert/paste`, {
    method: "POST",
    headers: {
      "X-API-Key": API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ html }),
  });

  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const data = await response.json();
  return data.markdown;
}

async function convertUrl(url) {
  const response = await fetch(`${BASE_URL}/api/convert/url`, {
    method: "POST",
    headers: {
      "X-API-Key": API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url }),
  });

  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const data = await response.json();
  return data.markdown;
}

async function main() {
  // Convert inline HTML
  const md1 = await convertHtml("<h1>Hello</h1><p>World</p>");
  console.log("=== HTML conversion ===");
  console.log(md1);

  // Convert from URL
  const md2 = await convertUrl("https://example.com");
  console.log("\n=== URL conversion ===");
  console.log(md2);
}

main().catch(console.error);
