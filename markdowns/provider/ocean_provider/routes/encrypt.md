---
title: encrypt
slug: ocean_provider/routes/encrypt
app: provider
module: ocean_provider.routes.encrypt
source: https://github.com/oceanprotocol/provider/blob/v0.4.17-69-g5a60369/ocean_provider/routes/encrypt.py
version: 0.4.17
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
  - application/json
parameters:
  - in: body
    name: body
    required: true
    description: Asset urls encryption.
    schema:
      type: object
      required:
        - documentId
        - document
        - publisherAddress:
      properties:
        documentId:
          description: Identifier of the asset to be registered in ocean.
          type: string
          example: 'did:op:08a429b8529856d59867503f8056903a680935a76950bb9649785cc97869a43d'
        ddo:
          description: document description object (DDO)
          type: string
          example: See https://github.com/oceanprotocol/docs/blob/feature/ddo_v4/content/concepts/did-ddo.md
        publisherAddress:
          description: Publisher address.
          type: string
          example: '0x00a329c0648769A73afAc7F9381E08FB43dBEA72'
responses:
  201:
    description: DDO successfully encrypted.
  503:
    description: Service Unavailable

return: the encrypted DDO (hex str)

