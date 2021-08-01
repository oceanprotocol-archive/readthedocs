---
title: signature
slug: ocean_lib/web3_internal/web3_overrides/signature
app: ocean.py
module: ocean_lib.web3_internal.web3_overrides.signature
source: https://github.com/oceanprotocol/ocean.py/blob/issue-384-improve-docs/ocean_lib/web3_internal/web3_overrides/signature.py
version: 0.5.26
---
## SignatureFix

```python
@enforce_types
class SignatureFix(Signature)
```

Hack the Signature class to allow rebuilding of signature with a
v value of 27 or 28 instead of 0 or 1

#### \_\_init\_\_

```python
 | def __init__(signature_bytes=None, vrs=None, backend=None) -> None
```

Initialises SignatureFix object.

