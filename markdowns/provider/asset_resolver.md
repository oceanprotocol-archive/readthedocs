---
title: asset_resolver
slug: /read-the-docs/provider/asset_resolver
app: provider
module: assets.asset_resolver
---
DID Resolver module.

#### resolve\_asset

```python
def resolve_asset(did, metadata_cache_uri=None, token_address=None)
```

Resolve a DID to an URL/DDO or later an internal/external DID.

**Arguments**:

- `did`: the asset id to resolve, this is part of the ocean
DID did:op:<32 byte value>
- `metadata_cache_uri`: str the url of the metadata store
- `token_address`: str the address of the DataToken smart contract

:return string: DDO of the resolved DID
:return None: if the DID cannot be resolved

