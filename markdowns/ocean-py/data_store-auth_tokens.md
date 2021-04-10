---
title:data_store-auth_tokens
slug:/read-the-docs/ocean-py/data_store-auth_tokens
section:ocean-py
---
<a name="data_store.auth_tokens"></a>
# data\_store.auth\_tokens

<a name="data_store.auth_tokens.AuthTokensStorage"></a>
## AuthTokensStorage Objects

```python
class AuthTokensStorage(StorageBase)
```

<a name="data_store.auth_tokens.AuthTokensStorage.write_token"></a>
#### write\_token

```python
 | write_token(address, signed_token, created_at)
```

Store signed token for session management.

**Arguments**:

- `address`: hex str the ethereum address that signed the token
- `signed_token`: hex str the signed token
- `created_at`: date-time of token creation

<a name="data_store.auth_tokens.AuthTokensStorage.update_token"></a>
#### update\_token

```python
 | update_token(address, signed_token, created_at)
```

Update/replace the stored signed token for the given ethereum address.

**Arguments**:

- `address`: hex str the ethereum address that signed the token
- `signed_token`: hex str the signed token
- `created_at`: date-time of token creation

<a name="data_store.auth_tokens.AuthTokensStorage.read_token"></a>
#### read\_token

```python
 | read_token(address)
```

Retrieve stored signed token for the given ethereum address

**Arguments**:

- `address`: hex str the ethereum address that signed the token

**Returns**:

tuple (signed_token, created_at)

