---
title: bpool
slug: ocean_lib/models/bpool
app: ocean.py
module: ocean_lib.models.bpool
source: https://github.com/oceanprotocol/ocean.py/blob/HEAD/ocean_lib/models/bpool.py
version: 0.8.1
---
## BPool

```python
class BPool(BToken)
```

#### \_\_str\_\_

```python
 | @enforce_types
 | def __str__() -> str
```

Formats with attributes as key, value pairs.

#### isFinalized

```python
 | @enforce_types
 | def isFinalized() -> bool
```

Returns true if state is finalized.

The `finalized` state lets users know that the weights, balances, and
fees of this pool are immutable. In the `finalized` state, `SWAP`,
`JOIN`, and `EXIT` are public. `CONTROL` capabilities are disabled.
(https://docs.balancer.finance/smart-contracts/api#access-control)

#### isBound

```python
 | @enforce_types
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
 | @enforce_types
 | def getNumTokens() -> int
```

How many tokens are bound to this pool.

#### getCurrentTokens

```python
 | @enforce_types
 | def getCurrentTokens() -> typing.List[str]
```

@return -- list of [token_addr:str]

#### getFinalTokens

```python
 | @enforce_types
 | def getFinalTokens() -> typing.List[str]
```

@return -- list of [token_addr:str]

#### getNormalizedWeight

```python
 | @enforce_types
 | def getNormalizedWeight(token_address: str) -> int
```

The normalized weight of a token. The combined normalized weights of
all tokens will sum up to 1. (Note: the actual sum may be 1 plus or
minus a few wei due to division precision loss)

#### getController

```python
 | @enforce_types
 | def getController() -> str
```

Get the "controller" address, which can call `CONTROL` functions like
`rebind`, `setSwapFee`, or `finalize`.

#### setSwapFee

```python
 | @enforce_types
 | def setSwapFee(swapFee: int, from_wallet: Wallet) -> str
```

Caller must be controller. Pool must NOT be finalized.

#### setPublicSwap

```python
 | @enforce_types
 | def setPublicSwap(public: bool, from_wallet: Wallet) -> str
```

Makes `isPublicSwap` return `_publicSwap`. Requires caller to be
controller and pool not to be finalized. Finalized pools always have
public swap.

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

#### unbind

```python
 | @enforce_types
 | def unbind(token_address: str, from_wallet: Wallet) -> str
```

Unbinds a token, clearing all of its parameters. Exit fee is charged
and the remaining balance is sent to caller.

#### gulp

```python
 | @enforce_types
 | def gulp(token_address: str, from_wallet: Wallet) -> str
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
 | @enforce_types
 | def joinPool(poolAmountOut: int, maxAmountsIn: typing.List[int], from_wallet: Wallet) -> str
```

Join the pool, getting `poolAmountOut` pool tokens. This will pull some
of each of the currently trading tokens in the pool, meaning you must
have called `approve` for each token for this pool. These values are
limited by the array of `maxAmountsIn` in the order of the pool tokens.

#### exitPool

```python
 | @enforce_types
 | def exitPool(poolAmountIn: int, minAmountsOut: typing.List[int], from_wallet: Wallet) -> str
```

Exit the pool, paying `poolAmountIn` pool tokens and getting some of
each of the currently trading tokens in return. These values are
limited by the array of `minAmountsOut` in the order of the pool tokens.

#### swapExactAmountIn

```python
 | @enforce_types
 | def swapExactAmountIn(tokenIn_address: str, tokenAmountIn: int, tokenOut_address: str, minAmountOut: int, maxPrice: int, from_wallet: Wallet) -> str
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
 | @enforce_types
 | def joinswapExternAmountIn(tokenIn_address: str, tokenAmountIn: int, minPoolAmountOut: int, from_wallet: Wallet) -> str
```

Pay `tokenAmountIn` of token `tokenIn` to join the pool, getting
`poolAmountOut` of the pool shares.

#### joinswapPoolAmountOut

```python
 | @enforce_types
 | def joinswapPoolAmountOut(tokenIn_address: str, poolAmountOut: int, maxAmountIn: int, from_wallet: Wallet) -> str
```

Specify `poolAmountOut` pool shares that you want to get, and a token
`tokenIn` to pay with. This costs `maxAmountIn` tokens (these went
into the pool).

#### exitswapPoolAmountIn

```python
 | @enforce_types
 | def exitswapPoolAmountIn(tokenOut_address: str, poolAmountIn: int, minAmountOut: int, from_wallet: Wallet) -> str
```

Pay `poolAmountIn` pool shares into the pool, getting `tokenAmountOut`
of the given token `tokenOut` out of the pool.

#### exitswapExternAmountOut

```python
 | @enforce_types
 | def exitswapExternAmountOut(tokenOut_address: str, tokenAmountOut: int, maxPoolAmountIn: int, from_wallet: Wallet) -> str
```

Specify `tokenAmountOut` of token `tokenOut` that you want to get out
of the pool. This costs `poolAmountIn` pool shares (these went into
the pool).

#### calcSpotPrice

```python
 | @enforce_types
 | def calcSpotPrice(tokenBalanceIn: int, tokenWeightIn: int, tokenBalanceOut: int, tokenWeightOut: int, swapFee: int) -> int
```

Returns spotPrice.

#### calcOutGivenIn

```python
 | @enforce_types
 | def calcOutGivenIn(tokenBalanceIn: int, tokenWeightIn: int, tokenBalanceOut: int, tokenWeightOut: int, tokenAmountIn: int, swapFee: int) -> int
```

Returns tokenAmountOut.

#### calcInGivenOut

```python
 | @enforce_types
 | def calcInGivenOut(tokenBalanceIn: int, tokenWeightIn: int, tokenBalanceOut: int, tokenWeightOut: int, tokenAmountOut: int, swapFee: int) -> int
```

Returns tokenAmountIn.

#### calcPoolOutGivenSingleIn

```python
 | @enforce_types
 | def calcPoolOutGivenSingleIn(tokenBalanceIn: int, tokenWeightIn: int, poolSupply: int, totalWeight: int, tokenAmountIn: int, swapFee: int) -> int
```

Returns poolAmountOut.

#### calcSingleInGivenPoolOut

```python
 | @enforce_types
 | def calcSingleInGivenPoolOut(tokenBalanceIn: int, tokenWeightIn: int, poolSupply: int, totalWeight: int, poolAmountOut: int, swapFee: int) -> int
```

Returns tokenAmountIn.

#### calcSingleOutGivenPoolIn

```python
 | @enforce_types
 | def calcSingleOutGivenPoolIn(tokenBalanceOut: int, tokenWeightOut: int, poolSupply: int, totalWeight: int, poolAmountIn: int, swapFee: int) -> int
```

Returns tokenAmountOut.

#### calcPoolInGivenSingleOut

```python
 | @enforce_types
 | def calcPoolInGivenSingleOut(tokenBalanceOut: int, tokenWeightOut: int, poolSupply: int, totalWeight: int, tokenAmountOut: int, swapFee: int) -> int
```

Returns poolAmountIn.

#### get\_liquidity\_logs

```python
 | @enforce_types
 | def get_liquidity_logs(event_name: str, from_block: int, to_block: Optional[int] = None, user_address: Optional[str] = None, this_pool_only: bool = True) -> Tuple
```

**Arguments**:

- `event_name`: str, one of LOG_JOIN, LOG_EXIT, LOG_SWAP

