---
title: aquarius
slug: ocean_lib/common/aquarius/aquarius
app: ocean.py
module: ocean_lib.common.aquarius.aquarius
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/common/aquarius/aquarius.py
version: 0.8.1
---
Aquarius module.
Help to communicate with the metadata store.

## Aquarius

```python
class Aquarius()
```

Aquarius wrapper to call different endpoint of aquarius component.

#### \_\_init\_\_

```python
 | @enforce_types
 | def __init__(aquarius_url: str) -> None
```

The Metadata class is a wrapper on the Metadata Store, which has exposed a REST API.

**Arguments**:

- `aquarius_url`: Url of the aquarius instance.

#### get\_service\_endpoint

```python
 | @enforce_types
 | def get_service_endpoint() -> str
```

Retrieve the endpoint with the ddo for a given did.

**Returns**:

Return the url of the the ddo location

#### get\_encrypt\_endpoint

```python
 | @enforce_types
 | def get_encrypt_endpoint() -> str
```

Retrieve the endpoint for DDO encrption

**Returns**:

Return the url of the the Aquarius ddo encryption endpoint

#### get\_asset\_ddo

```python
 | @enforce_types
 | def get_asset_ddo(did: str) -> Optional[DDO]
```

Retrieve asset ddo for a given did.

**Arguments**:

- `did`: Asset DID string

**Returns**:

DDO instance

#### ddo\_exists

```python
 | @enforce_types
 | def ddo_exists(did: str) -> bool
```

Return whether the DDO with this did exists in Aqua

**Arguments**:

- `did`: Asset DID string

**Returns**:

bool

#### get\_asset\_metadata

```python
 | @enforce_types
 | def get_asset_metadata(did: str) -> list
```

Retrieve asset metadata for a given did.

**Arguments**:

- `did`: Asset DID string

**Returns**:

metadata key of the DDO instance

#### query\_search

```python
 | @enforce_types
 | def query_search(search_query: dict) -> list
```

Search using a query.

Currently implemented is the MongoDB query model to search for documents according to:
https://docs.mongodb.com/manual/tutorial/query-documents/

And an Elastic Search driver, which implements a basic parser to convert the query into
elastic search format.

Example: query_search({"price":[0,10]})

**Arguments**:

- `search_query`: Python dictionary, query following elasticsearch syntax

**Returns**:

List of DDO instance

#### validate\_metadata

```python
 | @enforce_types
 | def validate_metadata(metadata: dict) -> Tuple[bool, Union[list, dict]]
```

Validate that the metadata of your ddo is valid.

**Arguments**:

- `metadata`: conforming to the Metadata accepted by Ocean Protocol, dict

**Returns**:

bool

#### encrypt

```python
 | @enforce_types
 | def encrypt(text: str) -> bytes
```

Encrypt the contents of an asset.

**Returns**:

Return the encrypted asset string.

