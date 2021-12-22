---
title: services
slug: ocean_provider/utils/services
app: provider
module: ocean_provider.utils.services
source: https://github.com/oceanprotocol/provider/blob/v0.4.19/ocean_provider/utils/services.py
version: 0.4.19
---
## Service

```python
class Service()
```

#### \_\_init\_\_

```python
 | def __init__(service_endpoint, service_type, index, attributes=None) -> None
```

Initialize Service instance.

#### as\_dictionary

```python
 | def as_dictionary()
```

Return the service as a python dictionary.

#### from\_json

```python
 | @staticmethod
 | def from_json(service_dict)
```

Create a service object from a JSON string.

