---
title: auth_tokens
slug: /read-the-docs/aquarius/auth_tokens
app: aquarius
module: data_store.auth_tokens
---
## AuthTokensStorage

```python
class AuthTokensStorage(StorageBase)
```

#### write\_token

```python
 | def write_token(address, signed_token, created_at)
```

Store signed token for session management.

**Arguments**:

- `address`: hex str the ethereum address that signed the token
- `signed_token`: hex str the signed token
- `created_at`: date-time of token creation

#### update\_token

```python
 | def update_token(address, signed_token, created_at)
```

Update/replace the stored signed token for the given ethereum address.

**Arguments**:

- `address`: hex str the ethereum address that signed the token
- `signed_token`: hex str the signed token
- `created_at`: date-time of token creation

#### read\_token

```python
 | def read_token(address)
```

Retrieve stored signed token for the given ethereum address

**Arguments**:

- `address`: hex str the ethereum address that signed the token

**Returns**:

tuple (signed_token, created_at)

