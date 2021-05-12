---
title: assets
slug: /read-the-docs/aquarius/assets
app: aquarius
module: app.assets
---
#### get\_assets\_ids

```python
@assets.route("", methods=["GET"])
def get_assets_ids()
```

Get all asset IDs.
---
tags:
  - ddo
responses:
  200:
    description: successful action

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
    description: successful operation
  404:
    description: This asset DID is not in OceanDB

#### get\_asset\_ddos

```python
@assets.route("/ddo", methods=["GET"])
def get_asset_ddos()
```

Get DDO of all assets.
---
tags:
  - ddo
responses:
  200:
    description: successful action

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
  404:
    description: This asset DID is not in OceanDB.

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
  404:
    description: assets not found

#### query\_ddo

```python
@assets.route("/ddo/query", methods=["POST"])
def query_ddo()
```

Get a list of DDOs that match with the executed query.
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
      properties:
        query:
          type: string
          description: Query to realize
          example: {"value":1}
        sort:
          type: object
          description: Key or list of keys to sort the result
          example: {"value":1}
        offset:
          type: int
          description: Number of records per page
          example: 100
        page:
          type: int
          description: Page showed
          example: 1
responses:
  200:
    description: successful action

example:
    {"query": {"query_string": {"query": "(covid) -isInPurgatory:true"}}, "offset":1, "page": 1}

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
    description: successfully request. data is converted to hex
  400:
    description: Invalid format
  500:
    description: Error

