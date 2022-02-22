---
title: consume
slug: ocean_provider/routes/consume
app: provider
module: ocean_provider.routes.consume
source: https://github.com/oceanprotocol/provider/blob/v0.4.17-69-g5a60369/ocean_provider/routes/consume.py
version: 0.4.17
---
#### nonce

```python
@services.route("/nonce", methods=["GET"])
@validate(NonceRequest)
def nonce()
```

Returns a `nonce` for the given account address.

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
a number of datatokens to the provider as defined in the Asset's
service description in the Asset's DDO document.

The datatokens are transferred via the ethereum blockchain network
by requesting the user to sign an ERC20 `approveAndLock` transaction
where the approval is given to the provider's ethereum account for
the number of tokens required by the service.

**Returns**:


json object as follows:
```JSON
{
"datatoken": <data-token-contract-address>,
"nonce": <nonce-used-in-consumer-signature>,
"providerFee": <object containing provider fees
"computeAddress": <compute address>
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

