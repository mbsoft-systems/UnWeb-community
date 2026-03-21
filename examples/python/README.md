# Python Examples

Python scripts for using the UnWeb API.

## Examples

| Script | Description |
|--------|-------------|
| [basic-convert.py](basic-convert.py) | Convert HTML or a URL to markdown |
| [batch-convert.py](batch-convert.py) | Convert multiple URLs with rate limiting |

## Requirements

```bash
pip install requests
```

## Usage

Set your API key as an environment variable:

```bash
export UNWEB_API_KEY="unweb_your_key_here"
```

Then run any script:

```bash
python basic-convert.py
python batch-convert.py
```
