# Make (Integromat) Integration

Use UnWeb in [Make](https://www.make.com) scenarios to automate HTML-to-Markdown conversion.

## Status

Coming soon. Check back for scenario templates and setup guides.

## Quick Approach

In the meantime, you can use Make's **HTTP** module to call the UnWeb API:

1. Add an **HTTP - Make a request** module
2. **URL:** `https://api.unweb.info/api/convert/url`
3. **Method:** POST
4. **Headers:** `X-API-Key: unweb_your_key_here`, `Content-Type: application/json`
5. **Body:** `{"url": "{{your_url_variable}}"}`

## Contributing

Have a Make scenario using UnWeb? Submit a PR with your exported scenario.
