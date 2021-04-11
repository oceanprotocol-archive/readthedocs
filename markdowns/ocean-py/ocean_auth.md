---
title: ocean_auth
slug: /read-the-docs/ocean-py/ocean_auth
section: ocean.py
sub_section: ocean
---
<a name="ocean.ocean_auth"></a>
# ocean.ocean\_auth

Ocean module.

<a name="ocean.ocean_auth.OceanAuth"></a>
## OceanAuth Objects

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

<a name="ocean.ocean_auth.OceanAuth.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(storage_path)
```

Initialises OceanAuth object.

<a name="ocean.ocean_auth.OceanAuth.get"></a>
#### get

```python
 | get(wallet)
```

**Arguments**:

- `wallet`: Wallet instance signing the token

**Returns**:

hex str the token generated/signed by the users wallet

<a name="ocean.ocean_auth.OceanAuth.check"></a>
#### check

```python
 | check(token)
```

**Arguments**:

- `token`: hex str consist of signature and timestamp

**Returns**:

hex str ethereum address

<a name="ocean.ocean_auth.OceanAuth.store"></a>
#### store

```python
 | store(wallet)
```

**Arguments**:

- `wallet`: Wallet instance signing the token

**Returns**:


token that was generated and stored for this users wallet

<a name="ocean.ocean_auth.OceanAuth.restore"></a>
#### restore

```python
 | restore(wallet)
```

**Arguments**:

- `wallet`: Wallet instance to fetch the saved token

**Returns**:


hex str the token retreived from storage
None if no token found for this users wallet

<a name="ocean.ocean_auth.OceanAuth.is_stored"></a>
#### is\_stored

```python
 | is_stored(wallet)
```

**Arguments**:

- `wallet`: Wallet instance

**Returns**:

bool whether this wallet has a stored token

