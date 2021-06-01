---
title: pools
slug: aquarius/app/pools
app: aquarius
module: aquarius.app.pools
source: https://github.com/oceanprotocol/aquarius/blob/main/aquarius/app/pools.py
version: 2.2.11
---
#### get\_liquidity\_history

```python
@pools.route("/history/<poolAddress>", methods=["GET"])
def get_liquidity_history(poolAddress)
```

**Arguments**:

- `poolAddress`: 

**Returns**:

json object with two keys: `ocean` and `datatoken`
each has a list of datapoints sampled at specific time intervals from the pools liquidity history.

#### get\_current\_liquidity\_stats

```python
@pools.route("/liquidity/<poolAddress>", methods=["GET"])
def get_current_liquidity_stats(poolAddress)
```

**Arguments**:

- `poolAddress`: 

**Returns**:



#### get\_user\_balances

```python
@pools.route("/user/<userAddress>", methods=["GET"])
def get_user_balances(userAddress)
```

**Arguments**:

- `userAddress`: 

**Returns**:



