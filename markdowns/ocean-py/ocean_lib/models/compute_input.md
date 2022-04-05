---
title: compute_input
slug: ocean_lib/models/compute_input
app: ocean.py
module: ocean_lib.models.compute_input
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.2-1-g9fb6083/ocean_lib/models/compute_input.py
version: 1.0.0-alpha.2
---
## ComputeInput

```python
class ComputeInput()
```

#### \_\_init\_\_

```python
 | @enforce_types
 | def __init__(did: str, transfer_tx_id: Union[str, bytes], service_id: Union[str, int], userdata: Optional[Dict] = None) -> None
```

Initialise and validate arguments.

