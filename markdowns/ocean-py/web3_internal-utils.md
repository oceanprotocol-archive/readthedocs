---
title: web3_internal-utils
slug: /read-the-docs/ocean-py/web3_internal-utils
section: ocean-py
---
<a name="web3_internal.utils"></a>
# web3\_internal.utils

<a name="web3_internal.utils.generate_multi_value_hash"></a>
#### generate\_multi\_value\_hash

```python
generate_multi_value_hash(types, values)
```

Return the hash of the given list of values.
This is equivalent to packing and hashing values in a solidity smart contract
hence the use of `soliditySha3`.

**Arguments**:

- `types`: list of solidity types expressed as strings
- `values`: list of values matching the `types` list

**Returns**:

bytes

<a name="web3_internal.utils.prepare_prefixed_hash"></a>
#### prepare\_prefixed\_hash

```python
prepare_prefixed_hash(msg_hash)
```

**Arguments**:

- `msg_hash`: 

**Returns**:



<a name="web3_internal.utils.add_ethereum_prefix_and_hash_msg"></a>
#### add\_ethereum\_prefix\_and\_hash\_msg

```python
add_ethereum_prefix_and_hash_msg(text)
```

This method of adding the ethereum prefix seems to be used in web3.personal.sign/ecRecover.

**Arguments**:

- `text`: str any str to be signed / used in recovering address from a signature

**Returns**:

hash of prefixed text according to the recommended ethereum prefix

<a name="web3_internal.utils.to_32byte_hex"></a>
#### to\_32byte\_hex

```python
to_32byte_hex(web3, val)
```

**Arguments**:

- `web3`: 
- `val`: 

**Returns**:



<a name="web3_internal.utils.split_signature"></a>
#### split\_signature

```python
split_signature(web3, signature)
```

**Arguments**:

- `web3`: 
- `signature`: signed message hash, hex str

**Returns**:



