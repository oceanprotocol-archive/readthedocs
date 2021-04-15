<<<<<<< HEAD:markdowns/ocean-py/ocean-ocean_pool.md
<a name="ocean.ocean_pool"></a>
# ocean.ocean\_pool

<a name="ocean.ocean_pool.OceanPool"></a>
## OceanPool Objects
=======
---
title: ocean_pool
slug: /read-the-docs/aquarius/ocean_pool
section: aquarius
sub_section: ocean
---
## OceanPool
>>>>>>> gatsby:markdowns/aquarius/ocean_pool.md

```python
@enforce_types_shim
class OceanPool()
```

This pool is based on the Balancer protocol contracts with slight
modifications (https://github.com/balancer-labs). This class wraps the main
functionality needed to support publishing Data Tokens trading pools.

A pool here always has OCEAN tokens on one end and some DataToken on the other end.
This allows the DataToken owner or any DataToken holder to create a pool for trading
the data token vs. OCEAN tokens. As a result all functions here assume the pool
has only two tokens and one of the tokens is always the OCEAN token.

Note that the OCEAN token address is supplied to the init method. The Ocean instance
reads the OCEAN token address from the `address_file` config option (see Config.py).

#### \_\_init\_\_

```python
 | def __init__(ocean_token_address: str, bfactory_address: str)
```

Initialises Ocean Pool.

#### create

```python
 | def create(data_token_address: str, data_token_amount: float, OCEAN_amount: float, from_wallet: Wallet, data_token_weight: float = balancer_constants.INIT_WEIGHT_DT, swap_fee: float = balancer_constants.DEFAULT_SWAP_FEE) -> BPool
```

Create a new pool with bound datatoken and OCEAN token then finalize it.
The pool will have publicSwap enabled and swap fee is set
to `balancer_constants.DEFAULT_SWAP_FEE`.
Balances of both data tokens and OCEAN tokens must be sufficient in the
`from_wallet`, otherwise this will fail.

**Arguments**:

- `data_token_address`: str address of the DataToken contract
- `data_token_amount`: float amount of initial liquidity of data tokens
- `OCEAN_amount`: float amount of initial liquidity of OCEAN tokens
- `from_wallet`: Wallet instance of pool owner
- `data_token_weight`: float weight of the data token to be set in the new pool must be >= 1 & <= 9
- `swap_fee`: float the fee taken by the pool on each swap transaction

**Returns**:

BPool instance

#### get\_token\_address

```python
 | def get_token_address(pool_address: str, pool: BPool = None, validate=True) -> str
```

Returns the address of this pool's datatoken.

#### add\_data\_token\_liquidity

```python
 | def add_data_token_liquidity(pool_address: str, amount_base: int, from_wallet: Wallet) -> str
```

Add `amount_base` number of data tokens to the pool `pool_address`. In return the wallet owner
will get a number of pool shares/tokens

The pool has a datatoken and OCEAN token. This function can be used to add liquidity of only
the datatoken. To add liquidity of the OCEAN token, use the `add_OCEAN_liquidity` function.

**Arguments**:

- `pool_address`: str address of pool contract
- `amount_base`: number of data tokens to add to this pool
- `from_wallet`: Wallet instance of the owner of data tokens

**Returns**:

str transaction id/hash

#### add\_OCEAN\_liquidity

```python
 | def add_OCEAN_liquidity(pool_address: str, amount_base: int, from_wallet: Wallet) -> str
```

Add `amount_base` number of OCEAN tokens to the pool `pool_address`. In return the wallet owner
will get a number of pool shares/tokens

**Arguments**:

- `pool_address`: str address of pool contract
- `amount_base`: number of data tokens to add to this pool
- `from_wallet`: Wallet instance of the owner of data tokens

**Returns**:

str transaction id/hash

#### remove\_data\_token\_liquidity

```python
 | def remove_data_token_liquidity(pool_address: str, amount_base: int, max_pool_shares_base: int, from_wallet: Wallet) -> str
```

Remove `amount_base` number of data tokens from the pool `pool_address`. The wallet owner
will get that amount of data tokens. At the same time a number of pool shares/tokens up to
`max_pool_shares_base` will be taken from the caller's wallet and given back to the pool.

**Arguments**:

- `pool_address`: str address of pool contract
- `amount_base`: int number of data tokens to add to this pool in *base*
- `max_pool_shares_base`: int maximum number of pool shares as a cost for the withdrawn data tokens
- `from_wallet`: Wallet instance of the owner of data tokens

**Returns**:

str transaction id/hash

#### remove\_OCEAN\_liquidity

```python
 | def remove_OCEAN_liquidity(pool_address: str, amount_base: int, max_pool_shares_base: int, from_wallet: Wallet) -> str
```

Remove `amount_base` number of OCEAN tokens from the pool `pool_address`. The wallet owner
will get that amount of OCEAN tokens. At the same time a number of pool shares/tokens up to
`max_pool_shares_base` will be taken from the caller's wallet and given back to the pool.

**Arguments**:

- `pool_address`: str address of pool contract
- `amount_base`: int number of data tokens to add to this pool in *base*
- `max_pool_shares_base`: int maximum number of pool shares as a cost for the withdrawn data tokens
- `from_wallet`: Wallet instance of the owner of data tokens

**Returns**:

str transaction id/hash

#### buy\_data\_tokens

```python
 | def buy_data_tokens(pool_address: str, amount: float, max_OCEAN_amount: float, from_wallet: Wallet) -> str
```

Buy data tokens from this pool, paying `max_OCEAN_amount_base` of OCEAN tokens.
If total spent <= max_OCEAN_amount_base.
- Caller is spending OCEAN tokens, and receiving `amount_base` DataTokens
- OCEAN tokens are going into pool, DataTokens are going out of pool

The transaction fails if total spent exceeds `max_OCEAN_amount_base`.

**Arguments**:

- `pool_address`: str address of pool contract
- `amount`: int number of data tokens to add to this pool in *base*
- `max_OCEAN_amount`: 
- `from_wallet`: 

**Returns**:

str transaction id/hash

#### sell\_data\_tokens

```python
 | def sell_data_tokens(pool_address: str, amount_base: int, min_OCEAN_amount_base: int, from_wallet: Wallet) -> str
```

Sell data tokens into this pool, receive `min_OCEAN_amount_base` of OCEAN tokens.
If total income >= min_OCEAN_amount_base
- Caller is spending DataTokens, and receiving OCEAN tokens
- DataTokens are going into pool, OCEAN tokens are going out of pool

The transaction fails if total income does not reach `min_OCEAN_amount_base`

**Arguments**:

- `pool_address`: str address of pool contract
- `amount_base`: int number of data tokens to add to this pool in *base*
- `min_OCEAN_amount_base`: 
- `from_wallet`: 

**Returns**:

str transaction id/hash

#### get\_token\_price

```python
 | def get_token_price(pool_address: str) -> float
```

**Arguments**:

- `pool_address`: str the address of the pool contract

**Returns**:

int price of data token in terms of OCEAN tokens

#### add\_liquidity\_finalized

```python
 | def add_liquidity_finalized(pool_address: str, bpt_amount_base: int, max_data_token_amount_base: int, max_OCEAN_amount_base: int, from_wallet: Wallet) -> str
```

Add liquidity to a pool that's been finalized.
Buy bpt_amount_base tokens from the pool, spending DataTokens and OCEAN tokens
as needed and up to the specified maximum amounts.

**Arguments**:

- `pool_address`: str address of pool contract
- `bpt_amount_base`: int number of pool shares to receive for adding the liquidity
- `max_data_token_amount_base`: int maximum amount of Data tokens to go into the pool
- `max_OCEAN_amount_base`: int maximum amount of OCEAN tokens to go into the pool
- `from_wallet`: Wallet instance

**Returns**:

str transaction id/hash

