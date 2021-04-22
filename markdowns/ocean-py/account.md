---
title: account
slug: /read-the-docs/ocean-py/account
app: ocean.py
module: ocean_lib.web3_internal.account
---
Accounts module.

## Account

```python
class Account()
```

Class representing an account.

#### \_\_init\_\_

```python
 | def __init__(address=None, password=None, key_file=None, encrypted_key=None, private_key=None)
```

Hold account address, password and either keyfile path, encrypted key or private key.

**Arguments**:

- `address`: The address of this account
- `password`: account's password. This is necessary for decrypting the private key
to be able to sign transactions locally
- `key_file`: str path to the encrypted private key file
- `encrypted_key`: 
- `private_key`: 

