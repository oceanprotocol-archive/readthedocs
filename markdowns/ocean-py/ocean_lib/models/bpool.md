---
title: bpool
slug: ocean_lib/models/bpool
app: ocean.py
module: ocean_lib.models.bpool
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.2-1-g9fb6083/ocean_lib/models/bpool.py
version: 1.0.0-alpha.2
---
## BPool

```python
class BPool(BTokenBase)
```

#### is\_initialized

```python
 | @enforce_types
 | def is_initialized() -> bool
```

Returns true if state is initialized.

#### is\_finalized

```python
 | @enforce_types
 | def is_finalized() -> bool
```

Returns true if state is finalized.

The `finalized` state lets users know that the weights, balances, and
fees of this pool are immutable. In the `finalized` state, `SWAP`,
`JOIN`, and `EXIT` are public. `CONTROL` capabilities are disabled.

#### is\_bound

```python
 | @enforce_types
 | def is_bound(token_address: str) -> bool
```

Returns True if the token is bound.

A bound token has a valid balance and weight. A token cannot be bound
without valid parameters which will enable e.g. `getSpotPrice` in terms
of other tokens. However, disabling `isSwapPublic` will disable any
interaction with this token in practice (assuming there are no existing
tokens in the pool, which can always `exitPool`).

#### get\_num\_tokens

```python
 | @enforce_types
 | def get_num_tokens() -> int
```

How many tokens are bound to this pool.

#### get\_current\_tokens

```python
 | @enforce_types
 | def get_current_tokens() -> List[str]
```

@return -- list of [token_addr:str]

#### get\_final\_tokens

```python
 | @enforce_types
 | def get_final_tokens() -> List[str]
```

@return -- list of [token_addr:str]

#### get\_normalized\_weight

```python
 | @enforce_types
 | def get_normalized_weight(token_address: str) -> int
```

The normalized weight of a token. The combined normalized weights of
all tokens will sum up to 1. (Note: the actual sum may be 1 plus or
minus a few wei due to division precision loss)

#### get\_controller

```python
 | @enforce_types
 | def get_controller() -> str
```

Get the "controller" address, which can call `CONTROL` functions like
`rebind`, `setSwapFee`, or `finalize`.

#### set\_swap\_fee

```python
 | @enforce_types
 | def set_swap_fee(lp_swap_fee_amount: int, from_wallet: Wallet) -> str
```

Caller must be controller. Pool must NOT be finalized.

#### finalize

```python
 | @enforce_types
 | def finalize(from_wallet: Wallet) -> str
```

This makes the pool **finalized**. This is a one-way transition. `bind`,
`rebind`, `unbind`, `setSwapFee` and `setPublicSwap` will all throw
`ERR_IS_FINALIZED` after pool is finalized. This also switches
`isSwapPublic` to true.

#### bind

```python
 | @enforce_types
 | def bind(token_address: str, balance: int, weight: int, from_wallet: Wallet) -> str
```

Binds the token with address `token`. Tokens will be pushed/pulled from
caller to adjust match new balance. Token must not already be bound.
`balance` must be a valid balance and denorm must be a valid denormalized
weight. `bind` creates the token record and then calls `rebind` for
updating pool weights and token transfers.

Possible errors:
-`ERR_NOT_CONTROLLER` -- caller is not the controller
-`ERR_IS_BOUND` -- T is already bound
-`ERR_IS_FINALIZED` -- isFinalized() is true
-`ERR_ERC20_FALSE` -- ERC20 token returned false
-`ERR_MAX_TOKENS` -- Only 8 tokens are allowed per pool
-unspecified error thrown by token

#### rebind

```python
 | @enforce_types
 | def rebind(token_address: str, balance: int, weight: int, from_wallet: Wallet) -> str
```

Changes the parameters of an already-bound token. Performs the same
validation on the parameters.

#### join\_pool

```python
 | @enforce_types
 | def join_pool(pool_amount_out: int, max_amounts_in: List[int], from_wallet: Wallet) -> str
```

Join the pool, getting `poolAmountOut` pool tokens. This will pull some
of each of the currently trading tokens in the pool, meaning you must
have called `approve` for each token for this pool. These values are
limited by the array of `maxAmountsIn` in the order of the pool tokens.

#### exit\_pool

```python
 | @enforce_types
 | def exit_pool(pool_amount_in: int, min_amounts_out: List[int], from_wallet: Wallet) -> str
```

Exit the pool, paying `poolAmountIn` pool tokens and getting some of
each of the currently trading tokens in return. These values are
limited by the array of `minAmountsOut` in the order of the pool tokens.

#### swap\_exact\_amount\_in

```python
 | @enforce_types
 | def swap_exact_amount_in(token_in: str, token_out: str, consume_market_swap_fee_address: str, token_amount_in: int, min_amount_out: int, max_price: int, consume_market_swap_fee_amount: int, from_wallet: Wallet) -> str
```

Trades an exact `tokenAmountIn` of `tokenIn` taken from the caller by
the pool, in exchange for at least `minAmountOut` of `tokenOut` given
to the caller from the pool, with a maximum marginal price of
`maxPrice`.

The return values are what are limited by the arguments; you are
guaranteed `tokenAmountOut >= minAmountOut` and
`spotPriceAfter <= maxPrice)`.

**Arguments**:

  token_in (str),
  token_out (str),
  consume_market_swap_fee_address (str),
  token_amount_in (int),
  min_amount_out (int),
  max_price (int),
  consume_market_swap_fee_amount (int),
- `from_wallet` _Wallet_ - wallet to sign the transaction with
  

**Returns**:

- `tokenAmountIn` _int_ - amount of `tokenIn` sent to the pool
- `spotPriceAfter` _int_ - the new marginal spot price, ie, the result of `getSpotPrice` after the call

#### swap\_exact\_amount\_out

```python
 | @enforce_types
 | def swap_exact_amount_out(token_in: str, token_out: str, consume_market_swap_fee_address: str, max_amount_in: int, token_amount_out: int, max_price: int, consume_market_swap_fee_amount: int, from_wallet: Wallet) -> str
```

Swaps as little as possible limited of `tokenIn` for `tokenAmountOut` of `tokenOut`.
with a maximum amount of `tokenIn` of `maxAmountIn` and a maximum marginal price of
`maxPrice`.

The return values are what are limited by the arguments; you are
guaranteed `tokenAmountOut >= minAmountOut` and
`spotPriceAfter <= maxPrice)`.

**Arguments**:

  token_in (str),
  token_out (str),
  consume_market_swap_fee_address (str),
  max_amount_in (int),
  token_amount_out (int),
  max_price (int),
  consume_market_swap_fee_amount (int),
- `from_wallet` _Wallet_ - wallet to sign the transaction with
  

**Returns**:

- `tokenAmountOut` _int_ - amount of token that came out of the pool
- `spotPriceAfter` _int_ - the new marginal spot price, ie, the result of `getSpotPrice` after the call

#### join\_swap\_extern\_amount\_in

```python
 | @enforce_types
 | def join_swap_extern_amount_in(token_amount_in: int, min_pool_amount_out: int, from_wallet: Wallet) -> str
```

Pay `tokenAmountIn` of token `tokenIn` to join the pool, getting
`poolAmountOut` of the pool shares.

#### exit\_swap\_pool\_amount\_in

```python
 | @enforce_types
 | def exit_swap_pool_amount_in(pool_amount_in: int, min_amount_out: int, from_wallet: Wallet) -> str
```

Pay `poolAmountIn` pool shares into the pool, getting `tokenAmountOut`
of the given token `tokenOut` out of the pool.

