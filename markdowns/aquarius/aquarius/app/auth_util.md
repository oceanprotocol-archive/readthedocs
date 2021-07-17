---
title: auth_util
slug: aquarius/app/auth_util
app: aquarius
module: aquarius.app.auth_util
source: https://github.com/oceanprotocol/aquarius/blob/issue-517-add-docstrings/aquarius/app/auth_util.py
version: 2.2.12
---
#### get\_signer\_address

```python
def get_signer_address(message, signature, logger)
```

Get signer address of a previous signed message
:param str message: Message
:param str signature: Signature obtain with web3.eth.personal.sign

**Arguments**:

- `logger`: logging object

**Returns**:

Address or None in case of error

#### compare\_eth\_addresses

```python
def compare_eth_addresses(address, checker, logger)
```

Compare two addresses and return TRUE if there is a match
:param str address: Address
:param str checker: Address to compare with

**Arguments**:

- `logger`: instance of logging

**Returns**:

boolean

