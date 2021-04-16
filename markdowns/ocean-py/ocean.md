---
title: ocean
slug: /read-the-docs/ocean-py/ocean
section: ocean.py
sub_section: ocean
module: ocean_lib.ocean.ocean
---
Ocean module.

## Ocean

```python
@enforce_types_shim
class Ocean()
```

The Ocean class is the entry point into Ocean Protocol.

#### \_\_init\_\_

```python
 | def __init__(config=None, data_provider=None)
```

Initialize Ocean class.

Usage: Make a new Ocean instance

`ocean = Ocean({...})`

This class provides the main top-level functions in ocean protocol:
* Publish assets metadata and associated services
* Each asset is assigned a unique DID and a DID Document (DDO)
* The DDO contains the asset's services including the metadata
* The DID is registered on-chain with a URL of the metadata store
to retrieve the DDO from

`asset = ocean.assets.create(metadata, publisher_wallet)`

* Discover/Search assets via the current configured metadata store (Aquarius)

`assets_list = ocean.assets.search('search text')`

An instance of Ocean is parameterized by a `Config` instance.

**Arguments**:

- `config`: `Config` instance
- `data_provider`: `DataServiceProvider` instance

