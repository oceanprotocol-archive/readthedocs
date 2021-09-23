---
title: compute_input
slug: ocean_lib/models/compute_input
app: ocean.py
module: ocean_lib.models.compute_input
source: https://github.com/oceanprotocol/ocean.py/blob/issue497-bumpversion-to-v0.7.0/ocean_lib/models/compute_input.py
version: 0.7.0
---
## ComputeInput

```python
class ComputeInput()
```

#### \_\_init\_\_

```python
 | @enforce_types
 | def __init__(did: Optional[str], transfer_tx_id: str, service_id: Union[str, int], userdata: Optional[Dict] = None) -> None
```

Initialise and validate arguments.

