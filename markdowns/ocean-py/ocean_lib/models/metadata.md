---
title: metadata
slug: ocean_lib/models/metadata
app: ocean.py
module: ocean_lib.models.metadata
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/models/metadata.py
version: 0.8.1
---
## MetadataContract

```python
class MetadataContract(ContractBase)
```

#### get\_event\_log

```python
 | def get_event_log(event_name: str, block: int, did: str, timeout: int = 45) -> Optional[AttributeDict]
```

**Returns**:

Log if event is found else None

#### verify\_tx

```python
 | @enforce_types
 | def verify_tx(tx_hash: str) -> bool
```

:return bool:

#### create

```python
 | @enforce_types
 | def create(did: str, flags: bytes, data: bytes, from_wallet: Wallet) -> str
```

:return str: hex str transaction hash

#### update

```python
 | @enforce_types
 | def update(did: str, flags: bytes, data: bytes, from_wallet: Wallet) -> str
```

:return str: hex str transaction hash

