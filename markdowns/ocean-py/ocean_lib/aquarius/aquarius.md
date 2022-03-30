---
title: aquarius
slug: ocean_lib/aquarius/aquarius
app: ocean.py
module: ocean_lib.aquarius.aquarius
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/aquarius/aquarius.py
version: 1.0.0-alpha.1
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

#### get\_asset\_ddo

```python
 | @enforce_types
 | def get_asset_ddo(did: str) -> Optional[Asset]
```

Retrieve asset ddo for a given did.

**Arguments**:

- `did`: Asset DID string

**Returns**:

Asset instance

#### ddo\_exists

```python
 | @enforce_types
 | def ddo_exists(did: str) -> bool
```

Return whether the Asset with this did exists in Aqua

**Arguments**:

- `did`: Asset DID string

**Returns**:

bool

#### get\_asset\_metadata

```python
 | @enforce_types
 | def get_asset_metadata(did: str) -> dict
```

Retrieve asset metadata for a given did.

**Arguments**:

- `did`: Asset DID string

**Returns**:

metadata key of the Asset instance

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

List of Asset instance

#### validate\_asset

```python
 | @enforce_types
 | def validate_asset(asset: Asset) -> Tuple[bool, Union[list, dict]]
```

Validate the asset.

**Arguments**:

- `asset`: conforming to the asset accepted by Ocean Protocol, Asset

**Returns**:

bool

