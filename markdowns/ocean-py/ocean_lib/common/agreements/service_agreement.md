---
title: service_agreement
slug: ocean_lib/common/agreements/service_agreement
app: ocean.py
module: ocean_lib.common.agreements.service_agreement
source: https://github.com/oceanprotocol/ocean.py/blob/issue-384-improve-docs/ocean_lib/common/agreements/service_agreement.py
version: 0.5.26
---
## ServiceAgreement

```python
class ServiceAgreement(Service)
```

Class representing a Service Agreement.

#### \_\_init\_\_

```python
 | def __init__(attributes, service_endpoint=None, service_type=None, service_index=None, other_values=None)
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
 | def from_json(cls, service_dict)
```

**Arguments**:

- `service_dict`: 

**Returns**:



#### from\_ddo

```python
 | @classmethod
 | def from_ddo(cls, service_type, ddo)
```

**Arguments**:

- `service_type`: identifier of the service inside the asset DDO, str
- `ddo`: 

**Returns**:



#### get\_cost

```python
 | def get_cost()
```

Return the price from the conditions parameters.

**Returns**:

Float

