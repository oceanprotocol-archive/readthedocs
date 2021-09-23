---
title: ocean_services
slug: ocean_lib/ocean/ocean_services
app: ocean.py
module: ocean_lib.ocean.ocean_services
source: https://github.com/oceanprotocol/ocean.py/blob/issue497-update-docs/ocean_lib/ocean/ocean_services.py
version: 0.6.1
---
Ocean module.

## OceanServices

```python
class OceanServices()
```

Ocean services class.

#### create\_access\_service

```python
 | @staticmethod
 | @enforce_types
 | def create_access_service(attributes: Dict[str, Any], provider_uri: str) -> Tuple[str, Dict[str, Any]]
```

Publish an asset with an `Access` service according to the supplied attributes.

**Arguments**:

- `attributes`: attributes of the access service, dict
- `provider_uri`: str URL of service provider. This will be used as base to
construct the serviceEndpoint for the `access` (download) service

**Returns**:

Service instance or None

