# Table of Contents

* [web3\_internal.account](#web3_internal.account)
  * [Account](#web3_internal.account.Account)
    * [\_\_init\_\_](#web3_internal.account.Account.__init__)

<a name="web3_internal.account"></a>
# web3\_internal.account

Accounts module.

<a name="web3_internal.account.Account"></a>
## Account Objects

```python
class Account()
```

Class representing an account.

<a name="web3_internal.account.Account.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(address=None, password=None, key_file=None, encrypted_key=None, private_key=None)
```

Hold account address, password and either keyfile path, encrypted key or private key.

**Arguments**:

- `address`: The address of this account
- `password`: account's password. This is necessary for decrypting the private key
to be able to sign transactions locally
- `key_file`: str path to the encrypted private key file
- `encrypted_key`: 
- `private_key`: 

