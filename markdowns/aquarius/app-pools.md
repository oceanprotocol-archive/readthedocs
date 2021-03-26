# Table of Contents

* [app.pools](#app.pools)
  * [get\_liquidity\_history](#app.pools.get_liquidity_history)
  * [get\_current\_liquidity\_stats](#app.pools.get_current_liquidity_stats)
  * [get\_user\_balances](#app.pools.get_user_balances)

<a name="app.pools"></a>
# app.pools

<a name="app.pools.get_liquidity_history"></a>
#### get\_liquidity\_history

```python
@pools.route("/history/<poolAddress>", methods=["GET"])
get_liquidity_history(poolAddress)
```

**Arguments**:

- `poolAddress`: 

**Returns**:

json object with two keys: `ocean` and `datatoken`
each has a list of datapoints sampled at specific time intervals from the pools liquidity history.

<a name="app.pools.get_current_liquidity_stats"></a>
#### get\_current\_liquidity\_stats

```python
@pools.route("/liquidity/<poolAddress>", methods=["GET"])
get_current_liquidity_stats(poolAddress)
```

**Arguments**:

- `poolAddress`: 

**Returns**:



<a name="app.pools.get_user_balances"></a>
#### get\_user\_balances

```python
@pools.route("/user/<userAddress>", methods=["GET"])
get_user_balances(userAddress)
```

**Arguments**:

- `userAddress`: 

**Returns**:



