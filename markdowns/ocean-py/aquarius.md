---
title: aquarius
slug: /read-the-docs/ocean-py/aquarius
app: ocean.py
module: ocean_lib.common.aquarius.aquarius
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
 | def __init__(aquarius_url)
```

The Metadata class is a wrapper on the Metadata Store, which has exposed a REST API.

**Arguments**:

- `aquarius_url`: Url of the aquarius instance.

#### url

```python
 | @property
 | def url()
```

Base URL of the aquarius instance.

#### get\_service\_endpoint

```python
 | def get_service_endpoint()
```

Retrieve the endpoint with the ddo for a given did.

**Returns**:

Return the url of the the ddo location

#### list\_assets

```python
 | def list_assets()
```

List all the assets registered in the aquarius instance.

**Returns**:

List of DID string

#### get\_asset\_ddo

```python
 | def get_asset_ddo(did)
```

Retrieve asset ddo for a given did.

**Arguments**:

- `did`: Asset DID string

**Returns**:

DDO instance

#### get\_asset\_metadata

```python
 | def get_asset_metadata(did)
```

Retrieve asset metadata for a given did.

**Arguments**:

- `did`: Asset DID string

**Returns**:

metadata key of the DDO instance

#### list\_assets\_ddo

```python
 | def list_assets_ddo()
```

List all the ddos registered in the aquarius instance.

**Returns**:

List of DDO instance

#### text\_search

```python
 | def text_search(text, sort=None, offset=100, page=1)
```

Search in aquarius using text query.

Given the string aquarius will do a full-text query to search in all documents.

Currently implemented are the MongoDB and Elastic Search drivers.

For a detailed guide on how to search, see the MongoDB driver documentation:
mongodb driverCurrently implemented in:
https://docs.mongodb.com/manual/reference/operator/query/text/

And the Elastic Search documentation:
https://www.elastic.co/guide/en/elasticsearch/guide/current/full-text-search.html
Other drivers are possible according to each implementation.

**Arguments**:

- `text`: String to be search.
- `sort`: 1/-1 to sort ascending or descending.
- `offset`: Integer with the number of elements displayed per page.
- `page`: Integer with the number of page.

**Returns**:

List of DDO instance

#### query\_search

```python
 | def query_search(search_query, sort=None, offset=100, page=1)
```

Search using a query.

Currently implemented is the MongoDB query model to search for documents according to:
https://docs.mongodb.com/manual/tutorial/query-documents/

And an Elastic Search driver, which implements a basic parser to convert the query into
elastic search format.

Example: query_search({"price":[0,10]})

**Arguments**:

- `search_query`: Python dictionary, query following mongodb syntax
- `sort`: 1/-1 to sort ascending or descending.
- `offset`: Integer with the number of elements displayed per page.
- `page`: Integer with the number of page.

**Returns**:

List of DDO instance

#### validate\_metadata

```python
 | def validate_metadata(metadata)
```

Validate that the metadata of your ddo is valid.

**Arguments**:

- `metadata`: conforming to the Metadata accepted by Ocean Protocol, dict

**Returns**:

bool

