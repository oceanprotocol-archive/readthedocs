---
title: test_contract_handler_other
slug: /read-the-docs/provider/test_contract_handler_other
app: provider
module: web3_internal.test.test_contract_handler_other
---
#### test\_set\_artifacts\_path\_\_deny\_change\_to\_empty

```python
def test_set_artifacts_path__deny_change_to_empty()
```

Tests can not set empty artifacts path.

#### test\_set\_artifacts\_path\_\_deny\_change\_to\_same

```python
def test_set_artifacts_path__deny_change_to_same()
```

Tests can not set unchanged artifacts path.

#### test\_set\_artifacts\_path\_\_allow\_change

```python
def test_set_artifacts_path__allow_change()
```

Tests that a correct artifacts path can be set (happy flow).

#### test\_get\_unhappy\_paths

```python
def test_get_unhappy_paths()
```

Test that some erroneous artifacts paths can not be set (sad flows).

#### test\_get\_and\_has\_\_name\_only

```python
def test_get_and_has__name_only()
```

Tests get() and has() from name-only queries, which also call _load() and read_abi_from_file().

#### test\_get\_and\_has\_\_name\_and\_address

```python
def test_get_and_has__name_and_address(network, example_config)
```

Tests get() and has() from (name, address) queries, which also call _load() and read_abi_from_file().

#### test\_get\_concise\_contract

```python
def test_get_concise_contract()
```

Tests that a concise contract can be retrieved from a DataTokenTemplate.

#### test\_set

```python
def test_set()
```

Tests setting of a DataTokenTemplate on a Contract.

#### test\_read\_abi\_from\_file\_\_example\_config\_\_happy\_path

```python
def test_read_abi_from_file__example_config__happy_path(example_config)
```

Tests a correct reading of abi from file (happy path).

#### test\_read\_abi\_from\_file\_\_example\_config\_\_bad\_contract\_name

```python
def test_read_abi_from_file__example_config__bad_contract_name(example_config)
```

Tests an incorrect reading of abi from file (sad path).

