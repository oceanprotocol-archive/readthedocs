---
title: web3helper
slug: /read-the-docs/aquarius/web3helper
section: aquarius
sub_section: web3_internal
---
Web3Helper module to provide convenient functions.

## Web3Helper

```python
class Web3Helper(object)
```

This class provides convenient web3 functions.

#### get\_network\_name

```python
 | @staticmethod
 | def get_network_name(network_id=None)
```

Return the network name based on the current ethereum network id.

Return `ganache` for every network id that is not mapped.

**Arguments**:

- `network_id`: Network id, int

**Returns**:

Network name, str

#### get\_network\_id

```python
 | @staticmethod
 | def get_network_id()
```

Return the ethereum network id calling the `web3.version.network` method.

**Returns**:

Network id, int

#### sign\_hash

```python
 | @staticmethod
 | def sign_hash(msg_hash, wallet: Wallet)
```

This method use `personal_sign`for signing a message. This will always prepend the
`\x19Ethereum Signed Message:\n32` prefix before signing.

**Arguments**:

- `msg_hash`: 
- `wallet`: Wallet instance

**Returns**:

signature

#### ec\_recover

```python
 | @staticmethod
 | def ec_recover(message, signed_message)
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
 | @staticmethod
 | def get_ether_balance(address)
```

Get balance of an ethereum address.

**Arguments**:

- `address`: address, bytes32

**Returns**:

balance, int

