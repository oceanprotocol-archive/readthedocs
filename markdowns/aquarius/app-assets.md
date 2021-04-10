---
title: app-assets
slug: /read-the-docs/aquarius/app-assets
section: aquarius
---
<a name="app.assets"></a>
# app.assets

<a name="app.assets.get_assets_ids"></a>
#### get\_assets\_ids

```python
@assets.route("", methods=["GET"])
get_assets_ids()
```

Get all asset IDs.
---
tags:
  - ddo
responses:
  200:
    description: successful action

<a name="app.assets.get_ddo"></a>
#### get\_ddo

```python
@assets.route("/ddo/<did>", methods=["GET"])
get_ddo(did)
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

<a name="app.assets.get_asset_ddos"></a>
#### get\_asset\_ddos

```python
@assets.route("/ddo", methods=["GET"])
get_asset_ddos()
```

Get DDO of all assets.
---
tags:
  - ddo
responses:
  200:
    description: successful action

<a name="app.assets.get_metadata"></a>
#### get\_metadata

```python
@assets.route("/metadata/<did>", methods=["GET"])
get_metadata(did)
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

<a name="app.assets.get_assets_names"></a>
#### get\_assets\_names

```python
@assets.route("/names", methods=["POST"])
get_assets_names()
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

<a name="app.assets.query_ddo"></a>
#### query\_ddo

```python
@assets.route("/ddo/query", methods=["POST"])
query_ddo()
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

<a name="app.assets.validate"></a>
#### validate

```python
@assets.route("/ddo/validate", methods=["POST"])
validate()
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

<a name="app.assets.validate_remote"></a>
#### validate\_remote

```python
@assets.route("/ddo/validate-remote", methods=["POST"])
validate_remote()
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

<a name="app.assets.encrypt_ddo"></a>
#### encrypt\_ddo

```python
@assets.route("/ddo/encrypt", methods=["POST"])
encrypt_ddo()
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

