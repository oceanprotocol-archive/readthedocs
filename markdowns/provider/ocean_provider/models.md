---
title: models
slug: ocean_provider/models
app: provider
module: ocean_provider.models
source: https://github.com/oceanprotocol/provider/blob/issue-182-improve-docs/ocean_provider/models.py
version: 0.4.12
---
## UserNonce

```python
class UserNonce(Base)
```

Table for storing the nonce values for the Eth account addresses.
Also, defines `FIRST_NONCE = 0` as default value.

