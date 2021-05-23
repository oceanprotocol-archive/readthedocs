---
title: account
slug: None
app: ocean.py
module: ocean_lib.web3_internal.account
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/web3_internal/account.py
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

#### key\_file

```python
 | @property
 | def key_file()
```

Holds the key file path

#### private\_key

```python
 | @property
 | def private_key()
```

Holds the private key

#### key

```python
 | @property
 | def key()
```

Returns the private key (if defined) or the encrypted key.

