---
title: asset
slug: ocean_provider/utils/asset
app: provider
module: ocean_provider.utils.asset
source: https://github.com/oceanprotocol/provider/blob/v0.4.18-8-g361885d/ocean_provider/utils/asset.py
version: 0.4.19
---
## Asset

```python
class Asset()
```

#### \_\_init\_\_

```python
 | def __init__(dictionary: Optional[dict] = None) -> None
```

Clear the DDO data values.

#### is\_disabled

```python
 | @property
 | def is_disabled() -> bool
```

Returns whether the asset is disabled.

#### is\_retired

```python
 | @property
 | def is_retired() -> bool
```

Returns whether the asset is retired.

#### asset\_id

```python
 | @property
 | def asset_id() -> Optional[str]
```

The asset id part of the DID

#### metadata

```python
 | @property
 | def metadata() -> Optional[dict]
```

Get the metadata service.

#### encrypted\_files

```python
 | @property
 | def encrypted_files() -> Optional[dict]
```

Return encryptedFiles field in the base metadata.

#### get\_service

```python
 | def get_service(service_type: str)
```

Return a service using.

#### get\_service\_by\_index

```python
 | def get_service_by_index(index: int)
```

Get service for a given index.

**Arguments**:

- `index`: Service id, str

**Returns**:

Service

#### requires\_address\_credential

```python
 | @property
 | def requires_address_credential() -> bool
```

Checks if an address credential is required on this asset.

#### allowed\_addresses

```python
 | @property
 | def allowed_addresses() -> list
```

Lists addresses that are explicitly allowed in credentials.

#### denied\_addresses

```python
 | @property
 | def denied_addresses() -> list
```

Lists addresesses that are explicitly denied in credentials.

#### is\_consumable

```python
 | def is_consumable(credential: Optional[dict] = None, with_connectivity_check: bool = True, provider_uri: Optional[str] = None) -> ConsumableCodes
```

Checks whether an asset is consumable and returns a ConsumableCode.

#### is\_flag\_enabled

```python
 | def is_flag_enabled(flag_name: str) -> bool
```

**Returns**:

`isListed` or `bool` in metadata_service.attributes["status"]

