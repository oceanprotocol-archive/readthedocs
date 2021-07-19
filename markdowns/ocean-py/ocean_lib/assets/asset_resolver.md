---
title: asset_resolver
slug: ocean_lib/assets/asset_resolver
app: ocean.py
module: ocean_lib.assets.asset_resolver
source: https://github.com/oceanprotocol/ocean.py/blob/issue-384-improve-docs/ocean_lib/assets/asset_resolver.py
version: 0.5.26
---
DID Resolver module.

#### resolve\_asset

```python
@enforce_types
def resolve_asset(did, metadata_cache_uri=None, web3: Optional[Web3] = None, token_address=None)
```

Resolve a DID to an URL/DDO or later an internal/external DID.

**Arguments**:

- `did`: the asset id to resolve, this is part of the ocean
DID did:op:<32 byte value>
- `metadata_cache_uri`: str the url of the metadata store
- `web3`: Web3 instance
- `token_address`: str the address of the DataToken smart contract

:return string: DDO of the resolved DID

