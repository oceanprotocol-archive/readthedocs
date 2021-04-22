---
title: public_key_rsa
slug: /read-the-docs/provider/public_key_rsa
app: provider
module: common.ddo.public_key_rsa
---
Public key RSA

## PublicKeyRSA

```python
class PublicKeyRSA(PublicKeyBase)
```

Encode key value using RSA.

#### get\_authentication\_type

```python
 | def get_authentication_type()
```

Return the type of authentication supported by this class.

#### set\_encode\_key\_value

```python
 | def set_encode_key_value(value, store_type=PUBLIC_KEY_STORE_TYPE_BASE64)
```

Set the value based on the type of encoding supported by RSA.

