"""Batch convert multiple URLs to markdown files."""

import os
import sys
import time
import requests

API_KEY = os.environ.get("UNWEB_API_KEY", "unweb_your_key_here")
BASE_URL = "https://api.unweb.info"
HEADERS = {"X-API-Key": API_KEY, "Content-Type": "application/json"}

# Edit this list or load from a file
URLS = [
    "https://example.com",
    # Add more URLs here
]

OUTPUT_DIR = "output"


def convert_url(url: str) -> dict:
    """Convert a URL and return the response data."""
    response = requests.post(
        f"{BASE_URL}/api/convert/url",
        headers=HEADERS,
        json={"url": url},
    )
    return {"status": response.status_code, "data": response.json()}


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    success = 0
    failed = 0

    for url in URLS:
        print(f"Converting: {url}")
        result = convert_url(url)

        if result["status"] == 200:
            # Generate filename from URL
            filename = url.split("//")[-1].replace("/", "_").strip("_") + ".md"
            filepath = os.path.join(OUTPUT_DIR, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(result["data"]["markdown"])

            print(f"  Saved: {filepath}")
            success += 1
        elif result["status"] == 429:
            print("  Quota exceeded. Stopping.")
            break
        else:
            print(f"  Error: {result['status']}")
            failed += 1

        time.sleep(0.5)  # rate limiting

    print(f"\nDone: {success} converted, {failed} failed")


if __name__ == "__main__":
    main()
