---
title: asset
slug: ocean_lib/assets/asset
app: ocean.py
module: ocean_lib.assets.asset
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/assets/asset.py
version: 0.7.0
---
## Asset

```python
class Asset(DDO)
```

#### update\_compute\_privacy

```python
 | @enforce_types
 | def update_compute_privacy(trusted_algorithms: list, trusted_algo_publishers: Optional[list], allow_all: bool, allow_raw_algorithm: bool) -> None
```

Set the `trusted_algorithms` on the compute service.

- An assertion is raised if this asset has no compute service
- Updates the compute service in place
- Adds the trusted algorithms under privacy.publisherTrustedAlgorithms

**Arguments**:

- `trusted_algorithms`: list of dicts, each dict contain the keys
("containerSectionChecksum", "filesChecksum", "did")
- `trusted_algo_publishers`: list of strings, addresses of trusted publishers
- `allow_all`: bool -- set to True to allow all published algorithms to run on this dataset
- `allow_raw_algorithm`: bool -- determine whether raw algorithms (i.e. unpublished) can be run on this dataset

**Returns**:

None
:raises AssertionError if this asset has no `ServiceTypes.CLOUD_COMPUTE` service

