---
title: error_responses
slug: ocean_provider/utils/error_responses
app: provider
module: ocean_provider.utils.error_responses
source: https://github.com/oceanprotocol/provider/blob/v1.0.9/ocean_provider/utils/error_responses.py
version: 1.0.9
---
#### error\_response

```python
def error_response(err_str: str, status: int, custom_logger=None)
```

Logs error and returns an error response.

#### strip\_and\_replace\_urls

```python
def strip_and_replace_urls(err_str: str) -> str
```

Strips sensitive data from urls to be logged/returned.

