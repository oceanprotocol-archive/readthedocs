# Table of Contents

* [models.bpool](#models.bpool)
  * [BPool](#models.bpool.BPool)
    * [\_\_init\_\_](#models.bpool.BPool.__init__)
    * [\_\_str\_\_](#models.bpool.BPool.__str__)
    * [isFinalized](#models.bpool.BPool.isFinalized)
    * [isBound](#models.bpool.BPool.isBound)
    * [getNumTokens](#models.bpool.BPool.getNumTokens)
    * [getCurrentTokens](#models.bpool.BPool.getCurrentTokens)
    * [getFinalTokens](#models.bpool.BPool.getFinalTokens)
    * [getNormalizedWeight](#models.bpool.BPool.getNormalizedWeight)
    * [getController](#models.bpool.BPool.getController)
    * [setSwapFee](#models.bpool.BPool.setSwapFee)
    * [setPublicSwap](#models.bpool.BPool.setPublicSwap)
    * [finalize](#models.bpool.BPool.finalize)
    * [bind](#models.bpool.BPool.bind)
    * [rebind](#models.bpool.BPool.rebind)
    * [unbind](#models.bpool.BPool.unbind)
    * [gulp](#models.bpool.BPool.gulp)
    * [joinPool](#models.bpool.BPool.joinPool)
    * [exitPool](#models.bpool.BPool.exitPool)
    * [swapExactAmountIn](#models.bpool.BPool.swapExactAmountIn)
    * [joinswapExternAmountIn](#models.bpool.BPool.joinswapExternAmountIn)
    * [joinswapPoolAmountOut](#models.bpool.BPool.joinswapPoolAmountOut)
    * [exitswapPoolAmountIn](#models.bpool.BPool.exitswapPoolAmountIn)
    * [exitswapExternAmountOut](#models.bpool.BPool.exitswapExternAmountOut)
    * [calcSpotPrice](#models.bpool.BPool.calcSpotPrice)
    * [calcOutGivenIn](#models.bpool.BPool.calcOutGivenIn)
    * [calcInGivenOut](#models.bpool.BPool.calcInGivenOut)
    * [calcPoolOutGivenSingleIn](#models.bpool.BPool.calcPoolOutGivenSingleIn)
    * [calcSingleInGivenPoolOut](#models.bpool.BPool.calcSingleInGivenPoolOut)
    * [calcSingleOutGivenPoolIn](#models.bpool.BPool.calcSingleOutGivenPoolIn)
    * [calcPoolInGivenSingleOut](#models.bpool.BPool.calcPoolInGivenSingleOut)
    * [get\_liquidity\_logs](#models.bpool.BPool.get_liquidity_logs)

<a name="models.bpool"></a>
# models.bpool

<a name="models.bpool.BPool"></a>
## BPool Objects

```python
class BPool(BToken)
```

<a name="models.bpool.BPool.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(*args, **kwargs)
```

Initialises BPool object.

<a name="models.bpool.BPool.__str__"></a>
#### \_\_str\_\_

```python
 | __str__()
```

Formats with attributes as key, value pairs.

<a name="models.bpool.BPool.isFinalized"></a>
#### isFinalized

```python
 | isFinalized() -> bool
```

Returns true if state is finalized.

The `finalized` state lets users know that the weights, balances, and
fees of this pool are immutable. In the `finalized` state, `SWAP`,
`JOIN`, and `EXIT` are public. `CONTROL` capabilities are disabled.
(https://docs.balancer.finance/smart-contracts/api#access-control)

<a name="models.bpool.BPool.isBound"></a>
#### isBound

```python
 | isBound(token_address: str) -> bool
```

Returns True if the token is bound.

A bound token has a valid balance and weight. A token cannot be bound
without valid parameters which will enable e.g. `getSpotPrice` in terms
of other tokens. However, disabling `isSwapPublic` will disable any
interaction with this token in practice (assuming there are no existing
tokens in the pool, which can always `exitPool`).

<a name="models.bpool.BPool.getNumTokens"></a>
#### getNumTokens

```python
 | getNumTokens() -> int
```

How many tokens are bound to this pool.

<a name="models.bpool.BPool.getCurrentTokens"></a>
#### getCurrentTokens

```python
 | getCurrentTokens() -> typing.List[str]
```

@return -- list of [token_addr:str]

<a name="models.bpool.BPool.getFinalTokens"></a>
#### getFinalTokens

```python
 | getFinalTokens() -> typing.List[str]
```

@return -- list of [token_addr:str]

<a name="models.bpool.BPool.getNormalizedWeight"></a>
#### getNormalizedWeight

```python
 | getNormalizedWeight(token_address: str) -> int
```

The normalized weight of a token. The combined normalized weights of
all tokens will sum up to 1. (Note: the actual sum may be 1 plus or
minus a few wei due to division precision loss)

<a name="models.bpool.BPool.getController"></a>
#### getController

```python
 | getController() -> str
```

Get the "controller" address, which can call `CONTROL` functions like
`rebind`, `setSwapFee`, or `finalize`.

<a name="models.bpool.BPool.setSwapFee"></a>
#### setSwapFee

```python
 | setSwapFee(swapFee_base: int, from_wallet: Wallet)
```

Caller must be controller. Pool must NOT be finalized.

<a name="models.bpool.BPool.setPublicSwap"></a>
#### setPublicSwap

```python
 | setPublicSwap(public: bool, from_wallet: Wallet)
```

Makes `isPublicSwap` return `_publicSwap`. Requires caller to be
controller and pool not to be finalized. Finalized pools always have
public swap.

<a name="models.bpool.BPool.finalize"></a>
#### finalize

```python
 | finalize(from_wallet: Wallet)
```

This makes the pool **finalized**. This is a one-way transition. `bind`,
`rebind`, `unbind`, `setSwapFee` and `setPublicSwap` will all throw
`ERR_IS_FINALIZED` after pool is finalized. This also switches
`isSwapPublic` to true.

<a name="models.bpool.BPool.bind"></a>
#### bind

```python
 | bind(token_address: str, balance_base: int, weight_base: int, from_wallet: Wallet)
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

<a name="models.bpool.BPool.rebind"></a>
#### rebind

```python
 | rebind(token_address: str, balance_base: int, weight_base: int, from_wallet: Wallet)
```

Changes the parameters of an already-bound token. Performs the same
validation on the parameters.

<a name="models.bpool.BPool.unbind"></a>
#### unbind

```python
 | unbind(token_address: str, from_wallet: Wallet)
```

Unbinds a token, clearing all of its parameters. Exit fee is charged
and the remaining balance is sent to caller.

<a name="models.bpool.BPool.gulp"></a>
#### gulp

```python
 | gulp(token_address: str, from_wallet: Wallet)
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

<a name="models.bpool.BPool.joinPool"></a>
#### joinPool

```python
 | joinPool(poolAmountOut_base: int, maxAmountsIn_base: typing.List[int], from_wallet: Wallet)
```

Join the pool, getting `poolAmountOut` pool tokens. This will pull some
of each of the currently trading tokens in the pool, meaning you must
have called `approve` for each token for this pool. These values are
limited by the array of `maxAmountsIn` in the order of the pool tokens.

<a name="models.bpool.BPool.exitPool"></a>
#### exitPool

```python
 | exitPool(poolAmountIn_base: int, minAmountsOut_base: typing.List[int], from_wallet: Wallet)
```

Exit the pool, paying `poolAmountIn` pool tokens and getting some of
each of the currently trading tokens in return. These values are
limited by the array of `minAmountsOut` in the order of the pool tokens.

<a name="models.bpool.BPool.swapExactAmountIn"></a>
#### swapExactAmountIn

```python
 | swapExactAmountIn(tokenIn_address: str, tokenAmountIn_base: int, tokenOut_address: str, minAmountOut_base: int, maxPrice_base: int, from_wallet: Wallet)
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

<a name="models.bpool.BPool.joinswapExternAmountIn"></a>
#### joinswapExternAmountIn

```python
 | joinswapExternAmountIn(tokenIn_address: str, tokenAmountIn_base: int, minPoolAmountOut_base: int, from_wallet: Wallet)
```

Pay `tokenAmountIn` of token `tokenIn` to join the pool, getting
`poolAmountOut` of the pool shares.

<a name="models.bpool.BPool.joinswapPoolAmountOut"></a>
#### joinswapPoolAmountOut

```python
 | joinswapPoolAmountOut(tokenIn_address: str, poolAmountOut_base: int, maxAmountIn_base: int, from_wallet: Wallet)
```

Specify `poolAmountOut` pool shares that you want to get, and a token
`tokenIn` to pay with. This costs `maxAmountIn` tokens (these went
into the pool).

<a name="models.bpool.BPool.exitswapPoolAmountIn"></a>
#### exitswapPoolAmountIn

```python
 | exitswapPoolAmountIn(tokenOut_address: str, poolAmountIn_base: int, minAmountOut_base: int, from_wallet: Wallet)
```

Pay `poolAmountIn` pool shares into the pool, getting `tokenAmountOut`
of the given token `tokenOut` out of the pool.

<a name="models.bpool.BPool.exitswapExternAmountOut"></a>
#### exitswapExternAmountOut

```python
 | exitswapExternAmountOut(tokenOut_address: str, tokenAmountOut_base: int, maxPoolAmountIn_base: int, from_wallet: Wallet)
```

Specify `tokenAmountOut` of token `tokenOut` that you want to get out
of the pool. This costs `poolAmountIn` pool shares (these went into
the pool).

<a name="models.bpool.BPool.calcSpotPrice"></a>
#### calcSpotPrice

```python
 | calcSpotPrice(tokenBalanceIn_base: int, tokenWeightIn_base: int, tokenBalanceOut_base: int, tokenWeightOut_base: int, swapFee_base: int) -> int
```

Returns spotPrice_base.

<a name="models.bpool.BPool.calcOutGivenIn"></a>
#### calcOutGivenIn

```python
 | calcOutGivenIn(tokenBalanceIn_base: int, tokenWeightIn_base: int, tokenBalanceOut: int, tokenWeightOut_base: int, tokenAmountIn_base: int, swapFee_base: int) -> int
```

Returns tokenAmountOut_base.

<a name="models.bpool.BPool.calcInGivenOut"></a>
#### calcInGivenOut

```python
 | calcInGivenOut(tokenBalanceIn_base: int, tokenWeightIn_base: int, tokenBalanceOut_base: int, tokenWeightOut_base: int, tokenAmountOut_base: int, swapFee_base: int) -> int
```

Returns tokenAmountIn_base.

<a name="models.bpool.BPool.calcPoolOutGivenSingleIn"></a>
#### calcPoolOutGivenSingleIn

```python
 | calcPoolOutGivenSingleIn(tokenBalanceIn_base: int, tokenWeightIn_base: int, poolSupply_base: int, totalWeight_base: int, tokenAmountIn_base: int, swapFee_base: int) -> int
```

Returns poolAmountOut_base.

<a name="models.bpool.BPool.calcSingleInGivenPoolOut"></a>
#### calcSingleInGivenPoolOut

```python
 | calcSingleInGivenPoolOut(tokenBalanceIn_base: int, tokenWeightIn_base: int, poolSupply_base: int, totalWeight_base: int, poolAmountOut_base: int, swapFee_base: int) -> int
```

Returns tokenAmountIn_base.

<a name="models.bpool.BPool.calcSingleOutGivenPoolIn"></a>
#### calcSingleOutGivenPoolIn

```python
 | calcSingleOutGivenPoolIn(tokenBalanceOut_base: int, tokenWeightOut_base: int, poolSupply_base: int, totalWeight_base: int, poolAmountIn_base: int, swapFee_base: int) -> int
```

Returns tokenAmountOut_base.

<a name="models.bpool.BPool.calcPoolInGivenSingleOut"></a>
#### calcPoolInGivenSingleOut

```python
 | calcPoolInGivenSingleOut(tokenBalanceOut_base: int, tokenWeightOut_base: int, poolSupply_base: int, totalWeight_base: int, tokenAmountOut_base: int, swapFee_base: int) -> int
```

Returns poolAmountIn_base.

<a name="models.bpool.BPool.get_liquidity_logs"></a>
#### get\_liquidity\_logs

```python
 | get_liquidity_logs(event_name, web3, from_block, to_block=None, user_address=None, this_pool_only=True)
```

**Arguments**:

- `event_name`: str, one of LOG_JOIN, LOG_EXIT, LOG_SWAP
