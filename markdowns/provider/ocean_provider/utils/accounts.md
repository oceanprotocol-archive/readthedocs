---
title: accounts
slug: ocean_provider/utils/accounts
app: provider
module: ocean_provider.utils.accounts
source: https://github.com/oceanprotocol/provider/blob/v0.4.19/ocean_provider/utils/accounts.py
version: 0.4.19
---
#### verify\_signature

```python
def verify_signature(signer_address, signature, original_msg, nonce: int = None)
```

**Returns**:

True if signature is valid

#### get\_private\_key

```python
def get_private_key(wallet)
```

Returns private key of the given wallet

#### is\_auth\_token\_valid

```python
def is_auth_token_valid(token)
```

**Arguments**:

- `token`: str

**Returns**:

`True` if token is valid else `False`

#### check\_auth\_token

```python
def check_auth_token(token)
```

**Arguments**:

- `token`: str

**Returns**:

String

#### generate\_auth\_token

```python
def generate_auth_token(wallet)
```

**Arguments**:

- `wallet`: Wallet instance

**Returns**:

`str`

#### sign\_message

```python
def sign_message(message, wallet)
```

**Arguments**:

- `message`: str
- `wallet`: Wallet instance

**Returns**:

`hex` value of the signed message

