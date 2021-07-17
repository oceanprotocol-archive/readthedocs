---
title: pool_helper
slug: aquarius/app/pool_helper
app: aquarius
module: aquarius.app.pool_helper
source: https://github.com/oceanprotocol/aquarius/blob/issue-517-add-docstrings/aquarius/app/pool_helper.py
version: 2.2.12
---
#### get\_accumulative\_values

```python
def get_accumulative_values(values_list)
```

**Arguments**:

- `values_list`: List

**Returns**:

List of accumlated values

#### build\_liquidity\_and\_price\_history

```python
def build_liquidity_and_price_history(ocn_liquidity_changes, dt_liquidity_changes, ocn_weight, dt_weight, swap_fee)
```

Returns tuple as follows: (Ocean values, Datatoken values, prices)

