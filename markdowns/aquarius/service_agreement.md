---
title: service_agreement
slug: /read-the-docs/aquarius/service_agreement
app: aquarius
module: common.agreements.service_agreement
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

Int

#### create\_new\_agreement\_id

```python
 | @staticmethod
 | def create_new_agreement_id()
```

**Returns**:



