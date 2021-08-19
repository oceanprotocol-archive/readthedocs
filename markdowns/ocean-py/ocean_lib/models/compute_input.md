---
title: compute_input
slug: ocean_lib/models/compute_input
app: ocean.py
module: ocean_lib.models.compute_input
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/models/compute_input.py
version: 0.5.30
---
## ComputeInput

```python
@enforce_types
class ComputeInput()
```

#### \_\_init\_\_

```python
 | def __init__(did: Optional[str], transfer_tx_id: str, service_id: Union[str, int], userdata: Optional[Dict] = None) -> None
```

Initialise and validate arguments.

