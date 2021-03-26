# Table of Contents

* [web3\_internal.web3\_overrides.signature](#web3_internal.web3_overrides.signature)
  * [SignatureFix](#web3_internal.web3_overrides.signature.SignatureFix)
    * [\_\_init\_\_](#web3_internal.web3_overrides.signature.SignatureFix.__init__)

<a name="web3_internal.web3_overrides.signature"></a>
# web3\_internal.web3\_overrides.signature

<a name="web3_internal.web3_overrides.signature.SignatureFix"></a>
## SignatureFix Objects

```python
class SignatureFix(Signature)
```

Hack the Signature class to allow rebuilding of signature with a
v value of 27 or 28 instead of 0 or 1

<a name="web3_internal.web3_overrides.signature.SignatureFix.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(signature_bytes=None, vrs=None, backend=None) -> None
```

Initialises SignatureFix object.

