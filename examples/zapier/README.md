# Zapier Integration

Use UnWeb in [Zapier](https://zapier.com) zaps to automate HTML-to-Markdown conversion.

## Status

Coming soon. Check back for zap templates and setup guides.

## Quick Approach

In the meantime, you can use Zapier's **Webhooks by Zapier** action:

1. Add a **Webhooks by Zapier - Custom Request** action
2. **Method:** POST
3. **URL:** `https://api.unweb.info/api/convert/url`
4. **Headers:** `X-API-Key: unweb_your_key_here`, `Content-Type: application/json`
5. **Data:** `{"url": "{{url_from_trigger}}"}`

## Contributing

Have a Zapier integration using UnWeb? Submit a PR with your setup guide.
