---
title: utils
slug: /read-the-docs/aquarius/utils
section: aquarius
sub_section: web3_internal
module: web3_internal.utils
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



