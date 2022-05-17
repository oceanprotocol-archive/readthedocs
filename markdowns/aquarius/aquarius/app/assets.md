---
title: assets
slug: aquarius/app/assets
app: aquarius
module: aquarius.app.assets
source: https://github.com/oceanprotocol/aquarius/blob/v3.1.4/aquarius/app/assets.py
version: 3.1.4
---
#### get\_ddo

```python
@assets.route("/ddo/<did>", methods=["GET"])
def get_ddo(did)
```

Get DDO of a particular asset.
---
tags:
  - ddo
parameters:
  - name: did
    in: path
    description: DID of the asset.
    required: true
    type: string
responses:
  200:
    description: On successful operation returns DDO information.
    example:
      application/json: {
          "@context": "https://w3id.org/did/v1",
          "id": "did:op:00018b5b84eA05930f9D0dB8FFbb3B93EF86983b",
          "publicKey": [
              {
                  "id": "did:op:00018b5b84eA05930f9D0dB8FFbb3B93EF86983b",
                  "type": "EthereumECDSAKey",
                  "owner": "0x8aa92201E19E4930d4D25c0f7a245c1dCdD5A242"
              }
          ],
          "authentication": [
              {
                  "type": "RsaSignatureAuthentication2018",
                  "publicKey": "did:op:00018b5b84eA05930f9D0dB8FFbb3B93EF86983b"
              }
          ],
          "service": [
              {
                  "type": "metadata",
                  "attributes": {
                      "curation": {
                          "rating": 0.0,
                          "numVotes": 0,
                          "isListed": true
                      },
                      "main": {
                          "type": "dataset",
                          "name": "Nu nl",
                          "dateCreated": "2021-04-02T17:59:32Z",
                          "author": "ab",
                          "license": "MIT",
                          "files": [
                              {
                                  "index": 0,
                                  "contentType": "application/json"
                              }
                          ],
                          "datePublished": "2021-04-20T22:56:01Z"
                      },
                      "encryptedFiles": "0x047c992274f3fa2bf9c5cc57d0e0852f7b3ec22d7ab4e798e3e73e77e7f97"
                  },
                  "index": 0
              },
              {
                  "type": "access",
                  "index": 1,
                  "serviceEndpoint": "https://provider.datatunnel.allianceblock.io",
                  "attributes": {
                      "main": {
                          "creator": "0x8aa92201E19E4930d4D25c0f7a245c1dCdD5A242",
                          "datePublished": "2021-04-02T17:57:57Z",
                          "cost": "1",
                          "timeout": 2592000000,
                          "name": "dataAssetAccess"
                      }
                  }
              }
          ],
          "dataToken": "0x00018b5b84eA05930f9D0dB8FFbb3B93EF86983b",
          "created": "2021-04-02T18:00:01Z",
          "proof": {
              "created": "2021-04-02T17:59:33Z",
              "creator": "0x8aa92201E19E4930d4D25c0f7a245c1dCdD5A242",
              "type": "AddressHash",
              "signatureValue": "0xd23d2f28fcf152347e5b5f1064422ba0288dd608f0ea6cf433a3717fb735a92d"
          },
          "dataTokenInfo": {
              "address": "0x00018b5b84eA05930f9D0dB8FFbb3B93EF86983b",
              "name": "Parsimonious Plankton Token",
              "symbol": "PARPLA-59",
              "decimals": 18,
              "totalSupply": 100.0,
              "cap": 1000.0,
              "minter": "0x8aa92201E19E4930d4D25c0f7a245c1dCdD5A242",
              "minterBalance": 99.999
          },
          "updated": "2021-04-02T18:00:01Z",
          "accessWhiteList": [],
          "price": {
              "datatoken": 0.0,
              "ocean": 0.0,
              "value": 0.0,
              "type": "",
              "exchange_id": "",
              "address": "",
              "pools": [],
              "isConsumable": ""
          },
          "isInPurgatory": "false"
        }
    content:
      application/json:
        schema:
          type: object
  404:
    description: This asset DID is not in ES.

#### get\_metadata

```python
@assets.route("/metadata/<did>", methods=["GET"])
def get_metadata(did)
```

Get metadata of a particular asset
---
tags:
  - metadata
parameters:
  - name: did
    in: path
    description: DID of the asset.
    required: true
    type: string
responses:
  200:
    description: successful operation.
    example:
      application/json: {
        "curation": {
            "rating": 0.0,
            "numVotes": 0,
            "isListed": true
        },
        "main": {
            "type": "dataset",
            "name": "Nu nl",
            "dateCreated": "2021-04-02T17:59:32Z",
            "author": "ab",
            "license": "MIT",
            "files": [
                {
                    "index": 0,
                    "contentType": "application/json"
                }
            ],
            "datePublished": "2021-04-20T22:56:01Z"
        },
        "encryptedFiles": "0x047c992274f3fa2bf9c5cc57d0e0852f7b3ec22d7ab4e798e3e73e77e7f971ff04896129c9f58deac"
      }
  404:
    description: This asset DID is not in ES.

#### get\_assets\_names

```python
@assets.route("/names", methods=["POST"])
def get_assets_names()
```

Get names of assets as specified in the payload
---
tags:
  - name
consumes:
  - application/json
parameters:
  - in: body
    name: body
    required: true
    description: list of asset DIDs
    schema:
      type: object
      properties:
        didList:
          type: list
          description: list of dids
          example: ["did:op:123455644356", "did:op:533443322223344"]
responses:
  200:
    description: successful operation.
    example:
      application/json: {
        "did:op:03115a5Dc5fC8Ff8DA0270E61F87EEB3ed2b3798": "SVM Classifier v2.0",
        "did:op:01738AA29Ce1D4028C0719F7A0fd497a1BFBe918": "Wine dataset 1.0"
      }
  404:
    description: assets not found

#### query\_ddo

```python
@assets.route("/query", methods=["POST"])
def query_ddo()
```

Runs a native ES query.
---
tags:
  - ddo
consumes:
  - application/json
responses:
  200:
    description: successful action
  500:
    description: elasticsearch exception

#### validate

```python
@assets.route("/ddo/validate", methods=["POST"])
def validate()
```

Validate metadata content.
---
tags:
  - ddo
consumes:
  - application/json
parameters:
  - in: body
    name: body
    required: true
    description: Asset metadata.
    schema:
      type: object
responses:
  200:
    description: successfully request.
    example:
      application/json: true
  500:
    description: Error

#### validate\_remote

```python
@assets.route("/ddo/validate-remote", methods=["POST"])
def validate_remote()
```

Validate DDO content.
---
tags:
  - ddo
consumes:
  - application/json
parameters:
  - in: body
    name: body
    required: true
    description: Asset DDO.
    schema:
      type: object
responses:
  200:
    description: successfully request.
    example:
      application/json: true
  400:
    description: Invalid DDO format
  500:
    description: Error

#### encrypt\_ddo

```python
@assets.route("/ddo/encrypt", methods=["POST"])
def encrypt_ddo()
```

Encrypt a DDO.
---
tags:
  - ddo
consumes:
  - application/octet-stream
parameters:
  - in: body
    name: body
    required: true
    description: data
    schema:
      type: object
responses:
  200:
    description: successfully request.
  400:
    description: Invalid format
  500:
    description: Error

#### encrypt\_ddo\_as\_hex

```python
@assets.route("/ddo/encryptashex", methods=["POST"])
def encrypt_ddo_as_hex()
```

Encrypt a DDO.
---
tags:
  - ddo
consumes:
  - application/octet-stream
parameters:
  - in: body
    name: body
    required: true
    description: data
    schema:
      type: object
responses:
  200:
    description: successfully request. data is converted to hex
    example:
      text/plain:
        "0x041a1953f19ca7410bcbef240a65246399d477765b966aef3553b3c89cc5837943706359e44f3b991"
  400:
    description: Invalid format
  500:
    description: Error

