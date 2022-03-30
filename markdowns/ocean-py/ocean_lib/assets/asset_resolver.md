---
title: asset_resolver
slug: ocean_lib/assets/asset_resolver
app: ocean.py
module: ocean_lib.assets.asset_resolver
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/assets/asset_resolver.py
version: 1.0.0-alpha.1
---
DID Resolver module.

#### resolve\_asset

```python
@enforce_types
def resolve_asset(did: str, metadata_cache_uri: str) -> Asset
```

Resolve a DID to an URL/DDO or later an internal/external DID.

**Arguments**:

- `did`: the asset id to resolve, this is part of the ocean
DID did:op:<32 byte value>
- `metadata_cache_uri`: str the url of the metadata store

:return Asset: the resolved DID

