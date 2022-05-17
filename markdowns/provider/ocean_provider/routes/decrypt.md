---
title: decrypt
slug: ocean_provider/routes/decrypt
app: provider
module: ocean_provider.routes.decrypt
source: https://github.com/oceanprotocol/provider/blob/v1.0.9/ocean_provider/routes/decrypt.py
version: 1.0.9
---
#### decrypt

```python
@services.route("/decrypt", methods=["POST"])
@validate(DecryptRequest)
def decrypt()
```

Decrypts an encrypted document based on transaction Id or dataNftAddress.

---
consumes:
  - application/json
parameters:
  - name: decrypterAddress
    description: address of agent requesting decrypt
    type: string
    required: true
  - name: chainId
    description: chainId of the chain on which the encrypted document is stored
    type: int
    required: true
  - name: transactionId
    description: transaction Id where the document was created or last updated,
        required if dataNftAddress, encryptedDocument and flags parameters missing
    required: false
    type: string
  - name: dataNftAddress
    description: NFT address of the document,
        required if the transactionId parameter is missing
    required: false
    type: string
  - name: encryptedDocument
    description: encrypted document contents,
        required if the transactionId parameter is missing
    required: false
    type: string
  - name: flags
    description: encryption and compression flags,
        required if the transactionId parameter is missing
    required: false
    type: int
  - name: documentHash
    description: hash of the original document used for integrity check,
        required if the transactionId parameter is missing
    required: false
    type: int
  - name: nonce
    description: user nonce (timestamp)
    required: true
    type: decimal
  - name: signature
    description: user signature based on
        transactionId+dataNftAddress+decrypterAddress+chainId+nonce
    required: true
    type: string
responses:
  201:
    description: decrypted document
  400:
    description: One or more of the required attributes are missing or invalid.
  503:
    description: Service Unavailable

