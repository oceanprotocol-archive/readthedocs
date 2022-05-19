---
title: util
slug: ocean_provider/utils/util
app: provider
module: ocean_provider.utils.util
source: https://github.com/oceanprotocol/provider/blob/v0.4.24/ocean_provider/utils/util.py
version: 0.4.24
---
#### checksum

```python
def checksum(seed) -> str
```

Calculate the hash3_256.

#### get\_asset\_urls

```python
def get_asset_urls(asset, wallet)
```

Returns list of urls of the files included in this `asset` in order.

#### filter\_dictionary

```python
def filter_dictionary(dictionary, keys)
```

Filters a dictionary from a list of keys.

#### filter\_dictionary\_starts\_with

```python
def filter_dictionary_starts_with(dictionary, prefix)
```

Filters a dictionary from a key prefix.

#### decode\_from\_data

```python
def decode_from_data(data, key, dec_type="list")
```

Retrieves a dictionary key as a decoded dictionary or list.

