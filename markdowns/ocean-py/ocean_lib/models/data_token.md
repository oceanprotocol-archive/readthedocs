---
title: data_token
slug: ocean_lib/models/data_token
app: ocean.py
module: ocean_lib.models.data_token
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/models/data_token.py
version: 0.5.30
---
## DataToken

```python
@enforce_types
class DataToken(ContractBase)
```

#### calculate\_token\_holders

```python
 | def calculate_token_holders(from_block: Optional[BlockIdentifier], to_block: Optional[BlockIdentifier], min_token_amount: float) -> List[Tuple[str, float]]
```

Returns a list of addresses with token balances above a minimum token
amount. Calculated from the transactions between `from_block` and `to_block`.

