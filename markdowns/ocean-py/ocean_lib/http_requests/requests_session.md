---
title: requests_session
slug: ocean_lib/http_requests/requests_session
app: ocean.py
module: ocean_lib.http_requests.requests_session
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/http_requests/requests_session.py
version: 1.0.0-alpha.1
---
#### get\_requests\_session

```python
@enforce_types
def get_requests_session() -> Session
```

Set connection pool maxsize and block value to avoid `connection pool full` warnings.

**Returns**:

requests session

