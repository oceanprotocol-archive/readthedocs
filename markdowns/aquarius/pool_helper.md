---
title: pool_helper
slug: /read-the-docs/aquarius/pool_helper
app: aquarius
module: aquarius.app.pool_helper
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

