---
title: test_contract_handler_addresses
slug: /read-the-docs/provider/test_contract_handler_addresses
app: provider
module: web3_internal.test.test_contract_handler_addresses
---
This file does tests for method "get_contracts_addresses()", that's all.

#### test\_get\_contracts\_addresses\_empty

```python
def test_get_contracts_addresses_empty()
```

Tests that an empty address can not be set on a Contract.

#### test\_get\_contracts\_addresses\_bad\_path

```python
def test_get_contracts_addresses_bad_path()
```

Tests that a non-existent address can not be set on a Contract.

#### test\_get\_contracts\_addresses\_good\_path\_custom\_network

```python
def test_get_contracts_addresses_good_path_custom_network(tmp_path)
```

Tests that an address with a custom network can be set on a Contract.

#### test\_get\_contracts\_addresses\_good\_path\_use\_network\_alias

```python
def test_get_contracts_addresses_good_path_use_network_alias(tmp_path)
```

Tests that an address with a network alias can be set on a Contract.

#### test\_get\_contracts\_addresses\_example\_config

```python
def test_get_contracts_addresses_example_config(network, example_config)
```

Tests that an address can be set if using testing config.

