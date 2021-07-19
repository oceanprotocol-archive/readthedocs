---
title: utils
slug: ocean_lib/web3_internal/utils
app: ocean.py
module: ocean_lib.web3_internal.utils
source: https://github.com/oceanprotocol/ocean.py/blob/issue-384-improve-docs/ocean_lib/web3_internal/utils.py
version: 0.5.26
---
#### generate\_multi\_value\_hash

```python
def generate_multi_value_hash(types, values)
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
def prepare_prefixed_hash(msg_hash)
```

**Arguments**:

- `msg_hash`: 

**Returns**:



#### to\_32byte\_hex

```python
def to_32byte_hex(val)
```

**Arguments**:

- `val`: 

**Returns**:



#### split\_signature

```python
def split_signature(signature)
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

#### ec\_recover

```python
@enforce_types
def ec_recover(message, signed_message)
```

This method does not prepend the message with the prefix `\x19Ethereum Signed Message:\n32`.
The caller should add the prefix to the msg/hash before calling this if the signature was
produced for an ethereum-prefixed message.

**Arguments**:

- `message`: 
- `signed_message`: 

**Returns**:



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

