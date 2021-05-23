---
title: data_token
slug: None
app: ocean.py
module: ocean_lib.models.data_token
---
## DataToken

```python
@enforce_types_shim
class DataToken(ContractBase)
```

#### calculate\_token\_holders

```python
 | def calculate_token_holders(from_block: int, to_block: int, min_token_amount: float) -> List[Tuple[str, float]]
```

Returns a list of addresses with token balances above a minimum token
amount. Calculated from the transactions between `from_block` and `to_block`.

