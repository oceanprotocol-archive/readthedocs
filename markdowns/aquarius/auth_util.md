---
title: auth_util
slug: /read-the-docs/aquarius/auth_util
section: aquarius
sub_section: app
---
<a name="app.auth_util"></a>
# app.auth\_util

<a name="app.auth_util.get_signer_address"></a>
#### get\_signer\_address

```python
get_signer_address(message, signature, logger)
```

Get signer address of a previous signed message
:param str message: Message
:param str signature: Signature obtain with web3.eth.personal.sign

**Arguments**:

- `logger`: logging object

**Returns**:

Address or None in case of error

<a name="app.auth_util.compare_eth_addresses"></a>
#### compare\_eth\_addresses

```python
compare_eth_addresses(address, checker, logger)
```

Compare two addresses and return TRUE if there is a match
:param str address: Address
:param str checker: Address to compare with

**Arguments**:

- `logger`: instance of logging

**Returns**:

boolean

