---
title: public_key_base
slug: /read-the-docs/ocean-py/public_key_base
section: ocean.py
sub_section: ddo
module: ocean_lib.common.ddo.public_key_base
---
Public key base

Currently this class stores the public keys in the same form as in the JSON
text data.

## PublicKeyBase

```python
class PublicKeyBase()
```

Base Public Key class, to allow to perfom basic key storage and validation using DDO keys.

#### get\_id

```python
 | def get_id()
```

Get the key id.

#### assign\_did

```python
 | def assign_did(did)
```

assign the DID as the key id, if the DID does not have a '`value`'
at the end, then automatically add a new key value

#### get\_owner

```python
 | def get_owner()
```

Get the owner of this key.

#### get\_type

```python
 | def get_type()
```

Get the type of key.

#### get\_store\_type

```python
 | def get_store_type()
```

Get the type of key storage.

#### set\_key\_value

```python
 | def set_key_value(value, store_type=PUBLIC_KEY_STORE_TYPE_BASE64)
```

Set the key value based on it's storage type.

#### set\_encode\_key\_value

```python
 | def set_encode_key_value(value, store_type)
```

Save the key value base on it's storage type.

#### get\_decode\_value

```python
 | def get_decode_value()
```

Return the key value based on it's storage type.

#### get\_value

```python
 | def get_value()
```

Get the key value.

#### as\_text

```python
 | def as_text(is_pretty=False)
```

Return the key as JSON text.

#### as\_dictionary

```python
 | def as_dictionary()
```

Return the key as a python dictionary.

#### is\_valid

```python
 | def is_valid()
```

Return True if the key structure is valid.

#### get\_authentication\_type

```python
 | def get_authentication_type()
```

Base overloaded method to return the authentication type to use for this key.

