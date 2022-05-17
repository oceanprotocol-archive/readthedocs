---
title: encrypt
slug: ocean_provider/routes/encrypt
app: provider
module: ocean_provider.routes.encrypt
source: https://github.com/oceanprotocol/provider/blob/v1.0.9/ocean_provider/routes/encrypt.py
version: 1.0.9
---
#### encrypt

```python
@services.route("/encrypt", methods=["POST"])
def encrypt()
```

Encrypt data using the Provider's own symmetric key (symmetric encryption).
This can be used by the publisher of an asset to encrypt the DDO of the
asset data files before publishing the asset DDO. The publisher to use this
service is one that is using a front-end with a wallet app such as MetaMask.
The DDO is encrypted by the provider so that the provider will be able
to decrypt at time of providing the service later on.

---
tags:
  - services
consumes:
  - application/octet-stream
parameters:
  - in: body
    name: body
    required: true
    description: Binary document contents to encrypt.
responses:
  201:
    description: DDO successfully encrypted.
  400:
    description: Invalid request content type or failure to encrypt.
  503:
    description: Service Unavailable

return: the encrypted DDO (hex str)

