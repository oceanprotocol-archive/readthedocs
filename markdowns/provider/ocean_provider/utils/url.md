---
title: url
slug: ocean_provider/utils/url
app: provider
module: ocean_provider.utils.url
source: https://github.com/oceanprotocol/provider/blob/issue-182-improve-docs/ocean_provider/utils/url.py
version: 0.4.12
---
#### validate\_dns\_records

```python
def validate_dns_records(domain, records, record_type)
```

Verify if all DNS records resolve to public IP addresses.
Return True if they do, False if any error has been detected.

#### check\_url\_details

```python
def check_url_details(url, with_checksum=False)
```

If the url argument is invalid, returns False and empty dictionary.
Otherwise it returns True and a dictionary containing contentType and
contentLength. If the with_checksum flag is set to True, it also returns
the file checksum and the checksumType (currently hardcoded to sha256)

