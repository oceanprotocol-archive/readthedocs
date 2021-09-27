---
title: did
slug: ocean_lib/common/did
app: ocean.py
module: ocean_lib.common.did
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/common/did.py
version: 0.8.1
---
DID Lib to do DID's and DDO's.

## DID

```python
class DID()
```

Class representing an asset DID.

#### did

```python
 | @staticmethod
 | @enforce_types
 | def did(seed: Dict[str, str]) -> str
```

Create a did.

Format of the did:
did:op:cb36cf78d87f4ce4a784f17c2a4a694f19f3fbf05b814ac6b0b7197163888865

**Arguments**:

- `seed`: The list of checksums that is allocated in the proof, dict

**Returns**:

Asset did, str.

#### did\_parse

```python
@enforce_types
def did_parse(did: str) -> Dict[str, str]
```

Parse a DID into it's parts.

**Arguments**:

- `did`: Asset did, str.

**Returns**:

Python dictionary with the method and the id.

#### id\_to\_did

```python
@enforce_types
def id_to_did(did_id: Union[bytes, str], method: str = "op") -> str
```

Return an Ocean DID from given a hex id.

#### did\_to\_id

```python
@enforce_types
def did_to_id(did: str) -> str
```

Return an id extracted from a DID string.

#### did\_to\_id\_bytes

```python
@enforce_types
def did_to_id_bytes(did: Union[bytes, str]) -> bytes
```

Return an Ocean DID to it's correspondng hex id in bytes.

So did:op:<hex>, will return <hex> in byte format

