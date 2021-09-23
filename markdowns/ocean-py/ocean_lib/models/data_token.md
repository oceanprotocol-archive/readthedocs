---
title: data_token
slug: ocean_lib/models/data_token
app: ocean.py
module: ocean_lib.models.data_token
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/models/data_token.py
version: 0.7.0
---
## DataToken

```python
class DataToken(ContractBase)
```

#### calculate\_token\_holders

```python
 | @enforce_types
 | def calculate_token_holders(from_block: Optional[int], to_block: Optional[int], min_token_amount: int) -> List[Tuple[str, int]]
```

Returns a list of addresses with token balances above a minimum token
amount. Calculated from the transactions between `from_block` and `to_block`.

