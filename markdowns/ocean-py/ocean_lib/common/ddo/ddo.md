---
title: ddo
slug: ocean_lib/common/ddo/ddo
app: ocean.py
module: ocean_lib.common.ddo.ddo
source: https://github.com/oceanprotocol/ocean.py/blob/issue497-update-docs/ocean_lib/common/ddo/ddo.py
version: 0.6.1
---
## DDO

```python
class DDO()
```

DDO class to create, import, export, validate DDO objects.

#### \_\_init\_\_

```python
 | @enforce_types
 | def __init__(did: Optional[str] = None, json_text: Optional[str] = None, json_filename: Optional[Path] = None, created: Optional[Any] = None, dictionary: Optional[dict] = None) -> None
```

Clear the DDO data values.

#### is\_disabled

```python
 | @property
 | @enforce_types
 | def is_disabled() -> bool
```

Returns whether the asset is disabled.

#### is\_enabled

```python
 | @property
 | @enforce_types
 | def is_enabled() -> bool
```

Returns the opposite of is_disabled, for convenience.

#### is\_retired

```python
 | @property
 | @enforce_types
 | def is_retired() -> bool
```

Returns whether the asset is retired.

#### is\_listed

```python
 | @property
 | @enforce_types
 | def is_listed() -> bool
```

Returns whether the asset is listed.

#### asset\_id

```python
 | @property
 | @enforce_types
 | def asset_id() -> Optional[str]
```

The asset id part of the DID

#### metadata

```python
 | @property
 | @enforce_types
 | def metadata() -> Optional[dict]
```

Get the metadata service.

#### encrypted\_files

```python
 | @property
 | @enforce_types
 | def encrypted_files() -> Optional[dict]
```

Return encryptedFiles field in the base metadata.

#### add\_service

```python
 | @enforce_types
 | def add_service(service_type: Union[str, Service], service_endpoint: Optional[str] = None, values: Optional[dict] = None, index: Optional[int] = None) -> None
```

Add a service to the list of services on the DDO.

**Arguments**:

- `service_type`: Service
- `service_endpoint`: Service endpoint, str
- `values`: Python dict with index, templateId, serviceAgreementContract,
list of conditions and purchase endpoint.

#### as\_text

```python
 | @enforce_types
 | def as_text(is_proof: bool = True, is_pretty: bool = False) -> str
```

Return the DDO as a JSON text.

:param if is_proof: if False then do not include the 'proof' element.

**Arguments**:

- `is_pretty`: If True return dictionary in a prettier way, bool

**Returns**:

str

#### as\_dictionary

```python
 | @enforce_types
 | def as_dictionary(is_proof: bool = True) -> dict
```

Return the DDO as a JSON dict.

:param if is_proof: if False then do not include the 'proof' element.

**Returns**:

dict

#### add\_proof

```python
 | @enforce_types
 | def add_proof(checksums: dict, publisher_account: Union[Account, Wallet]) -> None
```

Add a proof to the DDO, based on the public_key id/index and signed with the private key
add a static proof to the DDO, based on one of the public keys.

**Arguments**:

- `checksums`: dict with the checksum of the main attributes of each service, dict
- `publisher_account`: account of the publisher, account

#### get\_service

```python
 | @enforce_types
 | def get_service(service_type: str) -> Optional[Service]
```

Return a service using.

#### get\_service\_by\_index

```python
 | @enforce_types
 | def get_service_by_index(index: int) -> Optional[Service]
```

Get service for a given index.

**Arguments**:

- `index`: Service id, str

**Returns**:

Service

#### enable

```python
 | @enforce_types
 | def enable() -> None
```

Enables asset for ordering.

#### disable

```python
 | @enforce_types
 | def disable() -> None
```

Disables asset from ordering.

#### retire

```python
 | @enforce_types
 | def retire() -> None
```

Retires an asset.

#### unretire

```python
 | @enforce_types
 | def unretire() -> None
```

Unretires an asset.

#### list

```python
 | @enforce_types
 | def list() -> None
```

Lists a previously unlisted asset.

#### unlist

```python
 | @enforce_types
 | def unlist() -> None
```

Unlists an asset.

#### requires\_address\_credential

```python
 | @property
 | @enforce_types
 | def requires_address_credential() -> bool
```

Checks if an address credential is required on this asset.

#### allowed\_addresses

```python
 | @property
 | @enforce_types
 | def allowed_addresses() -> list
```

Lists addresses that are explicitly allowed in credentials.

#### denied\_addresses

```python
 | @property
 | @enforce_types
 | def denied_addresses() -> list
```

Lists addresesses that are explicitly denied in credentials.

#### add\_address\_to\_allow\_list

```python
 | @enforce_types
 | def add_address_to_allow_list(address: str) -> None
```

Adds an address to allowed addresses list.

#### add\_address\_to\_deny\_list

```python
 | @enforce_types
 | def add_address_to_deny_list(address: str) -> None
```

Adds an address to the denied addresses list.

#### remove\_address\_from\_allow\_list

```python
 | @enforce_types
 | def remove_address_from_allow_list(address: str) -> None
```

Removes address from allow list (if it exists).

#### remove\_address\_from\_deny\_list

```python
 | @enforce_types
 | def remove_address_from_deny_list(address: str) -> None
```

Removes address from deny list (if it exists).

#### is\_consumable

```python
 | @enforce_types
 | def is_consumable(credential: Optional[dict] = None, with_connectivity_check: bool = True, provider_uri: Optional[str] = None) -> bool
```

Checks whether an asset is consumable and returns a ConsumableCode.

#### enable\_flag

```python
 | @enforce_types
 | def enable_flag(flag_name: str) -> None
```

**Returns**:

None

#### disable\_flag

```python
 | @enforce_types
 | def disable_flag(flag_name: str) -> None
```

**Returns**:

None

#### is\_flag\_enabled

```python
 | @enforce_types
 | def is_flag_enabled(flag_name: str) -> bool
```

**Returns**:

`isListed` or `bool` in metadata_service.attributes["status"]

