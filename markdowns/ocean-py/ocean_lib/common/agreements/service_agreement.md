---
title: service_agreement
slug: ocean_lib/common/agreements/service_agreement
app: ocean.py
module: ocean_lib.common.agreements.service_agreement
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/common/agreements/service_agreement.py
version: 0.5.30
---
## ServiceAgreement

```python
@enforce_types
class ServiceAgreement(Service)
```

Class representing a Service Agreement.

#### \_\_init\_\_

```python
 | def __init__(attributes: Optional[dict], service_endpoint: Optional[str], service_type: str = None, service_index: Optional[int] = None, other_values: Optional[dict] = None)
```

**Arguments**:

- `attributes`: dict of main attributes of the service. This should
include `main` and optionally the `additionalInformation` section
- `service_endpoint`: str URL to use for requesting service defined in this agreement
- `service_type`: str like ServiceTypes.ASSET_ACCESS
- `other_values`: dict of other key/value that maybe added and will be kept as is.

#### from\_json

```python
 | @classmethod
 | def from_json(cls, service_dict: dict) -> "ServiceAgreement"
```

**Arguments**:

- `service_dict`: 

**Returns**:



#### from\_ddo

```python
 | @classmethod
 | def from_ddo(cls, service_type: str, ddo: object) -> "ServiceAgreement"
```

**Arguments**:

- `service_type`: identifier of the service inside the asset DDO, str
- `ddo`: 

**Returns**:



#### get\_cost

```python
 | def get_cost() -> float
```

Return the price from the conditions parameters.

**Returns**:

Float

