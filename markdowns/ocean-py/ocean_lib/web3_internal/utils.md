---
title: utils
slug: ocean_lib/web3_internal/utils
app: ocean.py
module: ocean_lib.web3_internal.utils
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.2-1-g9fb6083/ocean_lib/web3_internal/utils.py
version: 1.0.0-alpha.2
---
#### generate\_multi\_value\_hash

```python
@enforce_types
def generate_multi_value_hash(types: List[str], values: List[str]) -> HexBytes
```

Return the hash of the given list of values.
This is equivalent to packing and hashing values in a solidity smart contract
hence the use of `soliditySha3`.

**Arguments**:

- `types`: list of solidity types expressed as strings
- `values`: list of values matching the `types` list

**Returns**:

bytes

#### prepare\_prefixed\_hash

```python
@enforce_types
def prepare_prefixed_hash(msg_hash: str) -> HexBytes
```

**Arguments**:

- `msg_hash`: 

**Returns**:



#### to\_32byte\_hex

```python
@enforce_types
def to_32byte_hex(val: int) -> str
```

**Arguments**:

- `val`: 

**Returns**:



#### split\_signature

```python
@enforce_types
def split_signature(signature: Any) -> Signature
```

**Arguments**:

- `web3`: 
- `signature`: signed message hash, hex str

**Returns**:



#### get\_network\_name

```python
@enforce_types
def get_network_name(chain_id: Optional[int] = None, web3: Optional[Web3] = None) -> str
```

Return the network name based on the current ethereum chain id.

Return `ganache` for every chain id that is not mapped.

**Arguments**:

- `chain_id`: Chain id, int
- `web3`: Web3 instance

#### get\_chain\_id

```python
@enforce_types
def get_chain_id(web3: Web3) -> int
```

Return the ethereum chain id calling the `web3.eth.chain_id` method.

**Arguments**:

- `web3`: Web3 instance

**Returns**:

Chain id, int

#### get\_ether\_balance

```python
@enforce_types
def get_ether_balance(web3: Web3, address: str) -> int
```

Get balance of an ethereum address.

**Arguments**:

- `address`: address, bytes32

**Returns**:

balance, int

