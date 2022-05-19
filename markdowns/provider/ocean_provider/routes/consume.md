---
title: consume
slug: ocean_provider/routes/consume
app: provider
module: ocean_provider.routes.consume
source: https://github.com/oceanprotocol/provider/blob/v0.4.24/ocean_provider/routes/consume.py
version: 0.4.24
---
#### nonce

```python
@services.route("/nonce", methods=["GET"])
@validate(NonceRequest)
def nonce()
```

Returns a `nonce` for the given account address.

#### encrypt

```python
@services.route("/encrypt", methods=["POST"])
@validate(EncryptRequest)
def encrypt()
```

Encrypt document using the Provider's own symmetric key (symmetric encryption).
This can be used by the publisher of an asset to encrypt the urls of the
asset data files before publishing the asset ddo. The publisher to use this
service is one that is using a front-end with a wallet app such as MetaMask.
The `urls` are encrypted by the provider so that the provider will be able
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
        document:
          description: document
          type: string
          example: '/some-url'
        publisherAddress:
          description: Publisher address.
          type: string
          example: '0x00a329c0648769A73afAc7F9381E08FB43dBEA72'
responses:
  201:
    description: document successfully encrypted.
  503:
    description: Service Unavailable

return: the encrypted document (hex str)

#### fileinfo

```python
@services.route("/fileinfo", methods=["POST"])
@validate(FileInfoRequest)
def fileinfo()
```

Retrieves Content-Type and Content-Length from the given URL or asset. Supports a payload of either url or did.
This can be used by the publisher of an asset to check basic information
about the URL(s). For now, this information consists of the Content-Type
and Content-Length of the request, using primarily OPTIONS, with fallback
to GET. In the future, we will add a hash to make sure that the file was
not tampered with at consumption time.

---
tags:
  - services

responses:
  200:
    description: the URL(s) could be analysed (returns the result).
  400:
    description: the URL(s) could not be analysed (bad request).

return: list of file info (index, valid, contentLength, contentType)

#### initialize

```python
@services.route("/initialize", methods=["GET"])
@validate(InitializeRequest)
def initialize()
```

Initialize a service request.
In order to consume a data service the user is required to send
a number of data tokens to the provider as defined in the Asset's
service description in the Asset's DDO document.

The data tokens are transferred via the ethereum blockchain network
by requesting the user to sign an ERC20 `approveAndLock` transaction
where the approval is given to the provider's ethereum account for
the number of tokens required by the service.

**Returns**:


json object as follows:
```JSON
{
"from": <consumer-address>,
"to": <receiver-address>,
"numTokens": <tokens-amount-in-base>
"dataToken": <data-token-contract-address>,
"nonce": <nonce-used-in-consumer-signature>
}
```

#### download

```python
@services.route("/download", methods=["GET"])
@validate(DownloadRequest)
def download()
```

Allows download of asset data file.

---
tags:
  - services
consumes:
  - application/json
parameters:
  - name: consumerAddress
    in: query
    description: The consumer address.
    required: true
    type: string
  - name: documentId
    in: query
    description: The ID of the asset/document (the DID).
    required: true
    type: string
  - name: url
    in: query
    description: This URL is only valid if Provider acts as a proxy.
                 Consumer can't download using the URL if it's not through the Provider.
    required: true
    type: string
  - name: signature
    in: query
    description: Signature of the documentId to verify that the consumer has rights to download the asset.
  - name: index
    in: query
    description: Index of the file in the array of files.
responses:
  200:
    description: Redirect to valid asset url.
  400:
    description: One of the required attributes is missing.
  401:
    description: Invalid asset data.
  503:
    description: Service Unavailable

#### asset\_urls

```python
@services.route("/assetUrls", methods=["GET"])
@validate(AssetUrlsRequest)
def asset_urls()
```

Lists files from an asset

---
tags:
  - services
consumes:
  - application/json
parameters:
  - name: documentId
    in: query
    description: The ID of the asset/document (the DID).
    required: true
    type: string
  - name: signature
    in: query
    description: Signature of the documentId to verify that the consumer has rights to download the asset.
  - name: serviceId
    in: string
    description: ServiceId for the asset access service.
  - name: nonce
    in: string
    description: User nonce.
  - name: publisherAddress
    in: query
    description: The publisher address.
    required: true
    type: string
responses:
  200:
    description: lists asset files
  400:
    description: One of the required attributes is missing.
  503:
    description: Service Unavailable

