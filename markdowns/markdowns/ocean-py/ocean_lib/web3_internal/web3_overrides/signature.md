---
title: signature
slug: None
app: ocean.py
module: ocean_lib.web3_internal.web3_overrides.signature
---
## SignatureFix

```python
@enforce_types_shim
class SignatureFix(Signature)
```

Hack the Signature class to allow rebuilding of signature with a
v value of 27 or 28 instead of 0 or 1

#### \_\_init\_\_

```python
 | def __init__(signature_bytes=None, vrs=None, backend=None) -> None
```

Initialises SignatureFix object.

