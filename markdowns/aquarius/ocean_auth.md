<<<<<<< HEAD:markdowns/ocean-py/ocean-ocean_auth.md
<a name="ocean.ocean_auth"></a>
# ocean.ocean\_auth

=======
---
title: ocean_auth
slug: /read-the-docs/aquarius/ocean_auth
section: aquarius
sub_section: ocean
---
>>>>>>> gatsby:markdowns/aquarius/ocean_auth.md
Ocean module.

## OceanAuth

```python
class OceanAuth()
```

Ocean auth class.

Provide basic management of a user auth token. This token can be used to emulate
sign-in behaviour. The token can be stored and associated with an expiry time.
This is useful in front-end applications that interact with a 3rd-party wallet
apps. The advantage of using the auth token is to reduce the number of confirmation
prompts requiring user action.

The auth token works with a provider service such as Ocean provider-py which also uses this
ocean module to handle auth tokens.

Token format is "signature-timestamp".

#### \_\_init\_\_

```python
 | def __init__(storage_path)
```

Initialises OceanAuth object.

#### get

```python
 | def get(wallet)
```

**Arguments**:

- `wallet`: Wallet instance signing the token

**Returns**:

hex str the token generated/signed by the users wallet

#### check

```python
 | def check(token)
```

**Arguments**:

- `token`: hex str consist of signature and timestamp

**Returns**:

hex str ethereum address

#### store

```python
 | def store(wallet)
```

**Arguments**:

- `wallet`: Wallet instance signing the token

**Returns**:


token that was generated and stored for this users wallet

#### restore

```python
 | def restore(wallet)
```

**Arguments**:

- `wallet`: Wallet instance to fetch the saved token

**Returns**:


hex str the token retreived from storage
None if no token found for this users wallet

#### is\_stored

```python
 | def is_stored(wallet)
```

**Arguments**:

- `wallet`: Wallet instance

**Returns**:

bool whether this wallet has a stored token

