---
title: utils
slug: ocean_lib/assets/utils
app: ocean.py
module: ocean_lib.assets.utils
source: https://github.com/oceanprotocol/ocean.py/blob/issue-384-improve-docs/ocean_lib/assets/utils.py
version: 0.5.26
---
#### create\_checksum

```python
def create_checksum(text)
```

:return str:

#### generate\_trusted\_algo\_dict

```python
@enforce_types
def generate_trusted_algo_dict(did: Optional[str] = None, metadata_cache_uri: Optional[str] = None, ddo: Optional[Asset] = None)
```

**Returns**:

Object as follows:
```
{
"did": <did>,
"filesChecksum": <str>,
"containerSectionChecksum": <str>
}
```

#### create\_publisher\_trusted\_algorithms

```python
@enforce_types
def create_publisher_trusted_algorithms(dids: list, metadata_cache_uri: str) -> list
```

**Returns**:

List of objects returned by `generate_trusted_algo_dict` method.

#### add\_publisher\_trusted\_algorithm

```python
@enforce_types
def add_publisher_trusted_algorithm(dataset_did: str, algo_did: str, metadata_cache_uri: str) -> list
```

**Returns**:

List of trusted algos

#### remove\_publisher\_trusted\_algorithm

```python
@enforce_types
def remove_publisher_trusted_algorithm(dataset_did: str, algo_did: str, metadata_cache_uri: str) -> list
```

**Returns**:

List of trusted algos not containing `algo_did`.

