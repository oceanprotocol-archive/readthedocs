---
title: test_contract_handler_load
slug: /read-the-docs/provider/test_contract_handler_load
app: provider
module: web3_internal.test.test_contract_handler_load
---
#### test\_load\_\_fail\_empty\_artifacts\_path

```python
def test_load__fail_empty_artifacts_path()
```

Tests that an empty artifacts path can not be loaded.

#### test\_load\_\_fail\_malformed\_eth\_address

```python
def test_load__fail_malformed_eth_address()
```

Tests that an invalid ETH addres makes the Contract unloadable.

#### test\_load\_\_fail\_wrong\_eth\_address

```python
def test_load__fail_wrong_eth_address()
```

Tests that a different ETH address from the Contract makes it unloadable.

#### test\_load\_\_name\_only

```python
@pytest.mark.skip(reason="postpone until #202 #227 fixed, then revisit in #185")
def test_load__name_only()
```

Tests load() from name-only query.

#### test\_load\_\_name\_and\_address

```python
def test_load__name_and_address(network, example_config)
```

Tests load() from (name, address) query.

#### test\_issue185\_unit

```python
@pytest.mark.skip(reason="postpone until #202 #227 fixed, then revisit in #185")
@pytest.mark.nosetup_all
def test_issue185_unit(monkeypatch)
```

For `185`, unit-test the root cause method, which is load

#### test\_issue185\_system

```python
@pytest.mark.skip(reason="postpone until #202 #227 fixed, then revisit in #185")
@pytest.mark.nosetup_all
def test_issue185_system(monkeypatch)
```

A system-level test, to replicate original failure seen in `185`

#### setup\_issue\_185

```python
def setup_issue_185(monkeypatch)
```

Used by tests of issue `185`. It's a nuanced setup to replicate the
issue; the github issue itself is the best source of details.

