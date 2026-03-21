"""Basic UnWeb conversion examples."""

import os
import requests

API_KEY = os.environ.get("UNWEB_API_KEY", "unweb_your_key_here")
BASE_URL = "https://api.unweb.info"
HEADERS = {"X-API-Key": API_KEY, "Content-Type": "application/json"}


def convert_html(html: str) -> str:
    """Convert an HTML string to markdown."""
    response = requests.post(
        f"{BASE_URL}/api/convert/paste",
        headers=HEADERS,
        json={"html": html},
    )
    response.raise_for_status()
    return response.json()["markdown"]


def convert_url(url: str) -> str:
    """Convert a webpage URL to markdown."""
    response = requests.post(
        f"{BASE_URL}/api/convert/url",
        headers=HEADERS,
        json={"url": url},
    )
    response.raise_for_status()
    return response.json()["markdown"]


if __name__ == "__main__":
    # Convert inline HTML
    md = convert_html("<h1>Hello</h1><p>World</p>")
    print("=== HTML conversion ===")
    print(md)

    # Convert from URL
    md = convert_url("https://example.com")
    print("\n=== URL conversion ===")
    print(md)
