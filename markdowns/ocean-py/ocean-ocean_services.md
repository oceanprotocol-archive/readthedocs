---
title:ocean-ocean_services
slug:/docs/ocean-py/ocean-ocean_services
section:ocean-py
---
<a name="ocean.ocean_services"></a>
# ocean.ocean\_services

Ocean module.

<a name="ocean.ocean_services.OceanServices"></a>
## OceanServices Objects

```python
class OceanServices()
```

Ocean services class.

<a name="ocean.ocean_services.OceanServices.create_access_service"></a>
#### create\_access\_service

```python
 | @staticmethod
 | create_access_service(attributes, provider_uri=None)
```

Publish an asset with an `Access` service according to the supplied attributes.

**Arguments**:

- `attributes`: attributes of the access service, dict
- `provider_uri`: str URL of service provider. This will be used as base to
construct the serviceEndpoint for the `access` (download) service

**Returns**:

Service instance or None

