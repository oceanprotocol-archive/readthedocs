---
title: utils
slug: ocean_lib/web3_internal/utils
app: ocean.py
module: ocean_lib.web3_internal.utils
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/web3_internal/utils.py
version: 0.5.22
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



#### add\_ethereum\_prefix\_and\_hash\_msg

```python
def add_ethereum_prefix_and_hash_msg(text)
```

This method of adding the ethereum prefix seems to be used in web3.personal.sign/ecRecover.

**Arguments**:

- `text`: str any str to be signed / used in recovering address from a signature

**Returns**:

hash of prefixed text according to the recommended ethereum prefix

#### to\_32byte\_hex

```python
def to_32byte_hex(web3, val)
```

**Arguments**:

- `web3`: 
- `val`: 

**Returns**:



#### split\_signature

```python
def split_signature(web3, signature)
```

**Arguments**:

- `web3`: 
- `signature`: signed message hash, hex str

**Returns**:



#### get\_network\_name

```python
@enforce_types_shim
def get_network_name(network_id: int = None) -> str
```

Return the network name based on the current ethereum network id.

Return `ganache` for every network id that is not mapped.

**Arguments**:

- `network_id`: Network id, int

**Returns**:

Network name, str

#### get\_network\_id

```python
@enforce_types_shim
def get_network_id() -> int
```

Return the ethereum network id calling the `web3.version.network` method.

**Returns**:

Network id, int

#### ec\_recover

```python
@enforce_types_shim
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
@enforce_types_shim
def get_ether_balance(address: str) -> int
```

Get balance of an ethereum address.

**Arguments**:

- `address`: address, bytes32

**Returns**:

balance, int

