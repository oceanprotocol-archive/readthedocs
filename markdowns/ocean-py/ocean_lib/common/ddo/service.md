---
title: service
slug: ocean_lib/common/ddo/service
app: ocean.py
module: ocean_lib.common.ddo.service
source: https://github.com/oceanprotocol/ocean.py/blob/issue497-update-docs/ocean_lib/common/ddo/service.py
version: 0.6.1
---
Service Class
To handle service items in a DDO record

## Service

```python
class Service()
```

Service class to create validate service in a DDO.

#### \_\_init\_\_

```python
 | def __init__(service_endpoint: Optional[str], service_type: str, attributes: Optional[Dict], other_values: Optional[Dict[str, Any]] = None, index: Optional[int] = None) -> None
```

Initialize Service instance.

#### values

```python
 | @enforce_types
 | def values() -> Dict[str, Any]
```

**Returns**:

array of values

#### update\_value

```python
 | @enforce_types
 | def update_value(name: str, value: Any) -> None
```

Update value in the array of values.

**Arguments**:

- `name`: Key of the value, str
- `value`: New value, str

**Returns**:

None

#### as\_dictionary

```python
 | @enforce_types
 | def as_dictionary() -> Dict[str, Any]
```

Return the service as a python dictionary.

#### from\_json

```python
 | @classmethod
 | @enforce_types
 | def from_json(cls, service_dict: Dict[str, Any]) -> "Service"
```

Create a service object from a JSON string.

