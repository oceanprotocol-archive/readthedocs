---
title: service
slug: ocean_lib/common/ddo/service
app: ocean.py
module: ocean_lib.common.ddo.service
source: https://github.com/oceanprotocol/ocean.py/blob/HEAD/ocean_lib/common/ddo/service.py
version: 0.5.26
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
 | def __init__(service_endpoint, service_type, attributes, other_values=None, index=None)
```

Initialize Service instance.

#### type

```python
 | @property
 | def type()
```

Type of the service.

**Returns**:

str

#### index

```python
 | @property
 | def index()
```

Identifier of the service inside the asset DDO

**Returns**:

str

#### service\_endpoint

```python
 | @property
 | def service_endpoint()
```

Service endpoint.

**Returns**:

String

#### set\_service\_endpoint

```python
 | def set_service_endpoint(service_endpoint)
```

Update service endpoint. Needed to update after create did.

**Arguments**:

- `service_endpoint`: Service endpoint, str

#### values

```python
 | def values()
```

**Returns**:

array of values

#### update\_value

```python
 | def update_value(name, value)
```

Update value in the array of values.

**Arguments**:

- `name`: Key of the value, str
- `value`: New value, str

**Returns**:

None

#### as\_dictionary

```python
 | def as_dictionary()
```

Return the service as a python dictionary.

#### from\_json

```python
 | @classmethod
 | def from_json(cls, service_dict)
```

Create a service object from a JSON string.

