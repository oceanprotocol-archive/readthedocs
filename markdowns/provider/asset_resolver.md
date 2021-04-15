---
title: asset_resolver
slug: /read-the-docs/provider/asset_resolver
section: provider
sub_section: assets
---
DID Resolver module.

#### resolve\_asset

```python
def resolve_asset(did, metadata_store_url=None, token_address=None)
```

Resolve a DID to an URL/DDO or later an internal/external DID.

**Arguments**:

- `did`: the asset id to resolve, this is part of the ocean
DID did:op:<32 byte value>
- `metadata_store_url`: str the url of the metadata store
- `token_address`: str the address of the DataToken smart contract

:return string: DDO of the resolved DID
:return None: if the DID cannot be resolved

**Raises**:

- `OceanDIDNotFound`: if no DID can be found to resolve.

