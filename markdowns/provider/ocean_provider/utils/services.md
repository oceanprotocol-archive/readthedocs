---
title: services
slug: ocean_provider/utils/services
app: provider
module: ocean_provider.utils.services
source: https://github.com/oceanprotocol/provider/blob/v1.0.9/ocean_provider/utils/services.py
version: 1.0.9
---
## Service

```python
class Service()
```

#### \_\_init\_\_

```python
 | def __init__(index: int, service_id: str, service_type: ServiceType, datatoken_address: HexAddress, service_endpoint: str, encrypted_files: HexStr, timeout: int, name: Optional[str] = None, description: Optional[str] = None, compute_dict: Optional[dict] = None) -> None
```

Initialize Service instance.
If service is type "compute", then, compute_dict should be set

#### from\_json

```python
 | @staticmethod
 | def from_json(index: int, service_dict: Dict[str, Any])
```

Create a Service object from a JSON string.

