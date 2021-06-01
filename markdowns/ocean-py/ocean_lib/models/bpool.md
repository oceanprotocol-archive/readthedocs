---
title: bpool
slug: ocean_lib/models/bpool
app: ocean.py
module: ocean_lib.models.bpool
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/models/bpool.py
version: 0.5.22
---
## BPool

```python
@enforce_types_shim
class BPool(BToken)
```

#### \_\_init\_\_

```python
 | def __init__(*args, **kwargs)
```

Initialises BPool object.

#### \_\_str\_\_

```python
 | def __str__()
```

Formats with attributes as key, value pairs.

#### isFinalized

```python
 | def isFinalized() -> bool
```

Returns true if state is finalized.

The `finalized` state lets users know that the weights, balances, and
fees of this pool are immutable. In the `finalized` state, `SWAP`,
`JOIN`, and `EXIT` are public. `CONTROL` capabilities are disabled.
(https://docs.balancer.finance/smart-contracts/api#access-control)

#### isBound

```python
 | def isBound(token_address: str) -> bool
```

Returns True if the token is bound.

A bound token has a valid balance and weight. A token cannot be bound
without valid parameters which will enable e.g. `getSpotPrice` in terms
of other tokens. However, disabling `isSwapPublic` will disable any
interaction with this token in practice (assuming there are no existing
tokens in the pool, which can always `exitPool`).

#### getNumTokens

```python
 | def getNumTokens() -> int
```

How many tokens are bound to this pool.

#### getCurrentTokens

```python
 | def getCurrentTokens() -> typing.List[str]
```

@return -- list of [token_addr:str]

#### getFinalTokens

```python
 | def getFinalTokens() -> typing.List[str]
```

@return -- list of [token_addr:str]

#### getNormalizedWeight

```python
 | def getNormalizedWeight(token_address: str) -> int
```

The normalized weight of a token. The combined normalized weights of
all tokens will sum up to 1. (Note: the actual sum may be 1 plus or
minus a few wei due to division precision loss)

#### getController

```python
 | def getController() -> str
```

Get the "controller" address, which can call `CONTROL` functions like
`rebind`, `setSwapFee`, or `finalize`.

#### setSwapFee

```python
 | def setSwapFee(swapFee_base: int, from_wallet: Wallet)
```

Caller must be controller. Pool must NOT be finalized.

#### setPublicSwap

```python
 | def setPublicSwap(public: bool, from_wallet: Wallet)
```

Makes `isPublicSwap` return `_publicSwap`. Requires caller to be
controller and pool not to be finalized. Finalized pools always have
public swap.

#### finalize

```python
 | def finalize(from_wallet: Wallet)
```

This makes the pool **finalized**. This is a one-way transition. `bind`,
`rebind`, `unbind`, `setSwapFee` and `setPublicSwap` will all throw
`ERR_IS_FINALIZED` after pool is finalized. This also switches
`isSwapPublic` to true.

#### bind

```python
 | def bind(token_address: str, balance_base: int, weight_base: int, from_wallet: Wallet)
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
 | def rebind(token_address: str, balance_base: int, weight_base: int, from_wallet: Wallet)
```

Changes the parameters of an already-bound token. Performs the same
validation on the parameters.

#### unbind

```python
 | def unbind(token_address: str, from_wallet: Wallet)
```

Unbinds a token, clearing all of its parameters. Exit fee is charged
and the remaining balance is sent to caller.

#### gulp

```python
 | def gulp(token_address: str, from_wallet: Wallet)
```

This syncs the internal `balance` of `token` within a pool with the
actual `balance` registered on the ERC20 contract. This is useful to
wallet for airdropped tokens or any tokens sent to the pool without
using the `join` or `joinSwap` methods.

As an example, pools that contain `COMP` tokens can have the `COMP`
balance updated with the rewards sent by Compound (https://etherscan.io/tx/0xeccd42bf2b8a180a561c026717707d9024a083059af2f22c197ee511d1010e23).
In order for any airdrop balance to be gulped, the token must be bound
to the pool. So if a shared pool (which is immutable) does not have a
given token, any airdrops in that token will be locked in the pool
forever.

#### joinPool

```python
 | def joinPool(poolAmountOut_base: int, maxAmountsIn_base: typing.List[int], from_wallet: Wallet)
```

Join the pool, getting `poolAmountOut` pool tokens. This will pull some
of each of the currently trading tokens in the pool, meaning you must
have called `approve` for each token for this pool. These values are
limited by the array of `maxAmountsIn` in the order of the pool tokens.

#### exitPool

```python
 | def exitPool(poolAmountIn_base: int, minAmountsOut_base: typing.List[int], from_wallet: Wallet)
```

Exit the pool, paying `poolAmountIn` pool tokens and getting some of
each of the currently trading tokens in return. These values are
limited by the array of `minAmountsOut` in the order of the pool tokens.

#### swapExactAmountIn

```python
 | def swapExactAmountIn(tokenIn_address: str, tokenAmountIn_base: int, tokenOut_address: str, minAmountOut_base: int, maxPrice_base: int, from_wallet: Wallet)
```

Trades an exact `tokenAmountIn` of `tokenIn` taken from the caller by
the pool, in exchange for at least `minAmountOut` of `tokenOut` given
to the caller from the pool, with a maximum marginal price of
`maxPrice`.

Returns `(tokenAmountOut`, `spotPriceAfter)`, where `tokenAmountOut`
is the amount of token that came out of the pool, and `spotPriceAfter`
is the new marginal spot price, ie, the result of `getSpotPrice` after
the call. (These values are what are limited by the arguments; you are
guaranteed `tokenAmountOut >= minAmountOut` and
`spotPriceAfter <= maxPrice)`.

#### joinswapExternAmountIn

```python
 | def joinswapExternAmountIn(tokenIn_address: str, tokenAmountIn_base: int, minPoolAmountOut_base: int, from_wallet: Wallet)
```

Pay `tokenAmountIn` of token `tokenIn` to join the pool, getting
`poolAmountOut` of the pool shares.

#### joinswapPoolAmountOut

```python
 | def joinswapPoolAmountOut(tokenIn_address: str, poolAmountOut_base: int, maxAmountIn_base: int, from_wallet: Wallet)
```

Specify `poolAmountOut` pool shares that you want to get, and a token
`tokenIn` to pay with. This costs `maxAmountIn` tokens (these went
into the pool).

#### exitswapPoolAmountIn

```python
 | def exitswapPoolAmountIn(tokenOut_address: str, poolAmountIn_base: int, minAmountOut_base: int, from_wallet: Wallet)
```

Pay `poolAmountIn` pool shares into the pool, getting `tokenAmountOut`
of the given token `tokenOut` out of the pool.

#### exitswapExternAmountOut

```python
 | def exitswapExternAmountOut(tokenOut_address: str, tokenAmountOut_base: int, maxPoolAmountIn_base: int, from_wallet: Wallet)
```

Specify `tokenAmountOut` of token `tokenOut` that you want to get out
of the pool. This costs `poolAmountIn` pool shares (these went into
the pool).

#### calcSpotPrice

```python
 | def calcSpotPrice(tokenBalanceIn_base: int, tokenWeightIn_base: int, tokenBalanceOut_base: int, tokenWeightOut_base: int, swapFee_base: int) -> int
```

Returns spotPrice_base.

#### calcOutGivenIn

```python
 | def calcOutGivenIn(tokenBalanceIn_base: int, tokenWeightIn_base: int, tokenBalanceOut: int, tokenWeightOut_base: int, tokenAmountIn_base: int, swapFee_base: int) -> int
```

Returns tokenAmountOut_base.

#### calcInGivenOut

```python
 | def calcInGivenOut(tokenBalanceIn_base: int, tokenWeightIn_base: int, tokenBalanceOut_base: int, tokenWeightOut_base: int, tokenAmountOut_base: int, swapFee_base: int) -> int
```

Returns tokenAmountIn_base.

#### calcPoolOutGivenSingleIn

```python
 | def calcPoolOutGivenSingleIn(tokenBalanceIn_base: int, tokenWeightIn_base: int, poolSupply_base: int, totalWeight_base: int, tokenAmountIn_base: int, swapFee_base: int) -> int
```

Returns poolAmountOut_base.

#### calcSingleInGivenPoolOut

```python
 | def calcSingleInGivenPoolOut(tokenBalanceIn_base: int, tokenWeightIn_base: int, poolSupply_base: int, totalWeight_base: int, poolAmountOut_base: int, swapFee_base: int) -> int
```

Returns tokenAmountIn_base.

#### calcSingleOutGivenPoolIn

```python
 | def calcSingleOutGivenPoolIn(tokenBalanceOut_base: int, tokenWeightOut_base: int, poolSupply_base: int, totalWeight_base: int, poolAmountIn_base: int, swapFee_base: int) -> int
```

Returns tokenAmountOut_base.

#### calcPoolInGivenSingleOut

```python
 | def calcPoolInGivenSingleOut(tokenBalanceOut_base: int, tokenWeightOut_base: int, poolSupply_base: int, totalWeight_base: int, tokenAmountOut_base: int, swapFee_base: int) -> int
```

Returns poolAmountIn_base.

#### get\_liquidity\_logs

```python
 | def get_liquidity_logs(event_name, web3, from_block, to_block=None, user_address=None, this_pool_only=True)
```

**Arguments**:

- `event_name`: str, one of LOG_JOIN, LOG_EXIT, LOG_SWAP

