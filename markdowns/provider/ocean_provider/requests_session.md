---
title: requests_session
slug: ocean_provider/requests_session
app: provider
module: ocean_provider.requests_session
source: https://github.com/oceanprotocol/provider/blob/v0.4.24/ocean_provider/requests_session.py
version: 0.4.24
---
#### get\_requests\_session

```python
def get_requests_session() -> Session
```

Set connection pool maxsize and block value to avoid `connection pool full` warnings.

**Returns**:

requests session

