---
title: requests_session
slug: ocean_lib/common/http_requests/requests_session
app: ocean.py
module: ocean_lib.common.http_requests.requests_session
source: https://github.com/oceanprotocol/ocean.py/blob/v0.8.6/ocean_lib/common/http_requests/requests_session.py
version: 0.8.6
---
#### get\_requests\_session

```python
@enforce_types
def get_requests_session() -> Session
```

Set connection pool maxsize and block value to avoid `connection pool full` warnings.

**Returns**:

requests session

