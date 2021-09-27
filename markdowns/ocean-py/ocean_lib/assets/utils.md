---
title: utils
slug: ocean_lib/assets/utils
app: ocean.py
module: ocean_lib.assets.utils
source: https://github.com/oceanprotocol/ocean.py/blob/HEAD/ocean_lib/assets/utils.py
version: 0.8.1
---
#### create\_checksum

```python
@enforce_types
def create_checksum(text: str) -> str
```

**Returns**:

str

#### generate\_trusted\_algo\_dict

```python
@enforce_types
def generate_trusted_algo_dict(asset_or_did: Union[str, Asset] = None, metadata_cache_uri: Optional[str] = None) -> dict
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
def create_publisher_trusted_algorithms(ddos_or_dids: list, metadata_cache_uri: str) -> list
```

**Returns**:

List of objects returned by `generate_trusted_algo_dict` method.

#### add\_publisher\_trusted\_algorithm

```python
@enforce_types
def add_publisher_trusted_algorithm(asset_or_did: Union[str, Asset], algo_did: str, metadata_cache_uri: str) -> list
```

**Returns**:

List of trusted algos

#### add\_publisher\_trusted\_algorithm\_publisher

```python
@enforce_types
def add_publisher_trusted_algorithm_publisher(asset_or_did: Union[str, Asset], publisher_address: str, metadata_cache_uri: str) -> list
```

**Returns**:

List of trusted algo publishers

#### remove\_publisher\_trusted\_algorithm

```python
@enforce_types
def remove_publisher_trusted_algorithm(asset_or_did: Union[str, Asset], algo_did: str, metadata_cache_uri: str) -> list
```

**Returns**:

List of trusted algos not containing `algo_did`.

#### remove\_publisher\_trusted\_algorithm\_publisher

```python
@enforce_types
def remove_publisher_trusted_algorithm_publisher(asset_or_did: Union[str, Asset], publisher_address: str, metadata_cache_uri: str) -> list
```

**Returns**:

List of trusted algo publishers not containing `publisher_address`.

