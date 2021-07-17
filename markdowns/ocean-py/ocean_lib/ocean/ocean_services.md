---
title: ocean_services
slug: ocean_lib/ocean/ocean_services
app: ocean.py
module: ocean_lib.ocean.ocean_services
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/ocean/ocean_services.py
version: 0.5.24
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
 | def create_access_service(attributes, provider_uri)
```

Publish an asset with an `Access` service according to the supplied attributes.

**Arguments**:

- `attributes`: attributes of the access service, dict
- `provider_uri`: str URL of service provider. This will be used as base to
construct the serviceEndpoint for the `access` (download) service

**Returns**:

Service instance or None

