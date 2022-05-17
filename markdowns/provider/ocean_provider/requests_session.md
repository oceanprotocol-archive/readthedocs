---
title: requests_session
slug: ocean_provider/requests_session
app: provider
module: ocean_provider.requests_session
source: https://github.com/oceanprotocol/provider/blob/v1.0.9/ocean_provider/requests_session.py
version: 1.0.9
---
#### get\_requests\_session

```python
def get_requests_session() -> Session
```

Set connection pool maxsize and block value to avoid `connection pool full` warnings.

**Returns**:

requests session

