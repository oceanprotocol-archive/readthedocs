---
title:assets-asset
slug:/docs/ocean-py/assets-asset
section:content
---
<a name="assets.asset"></a>
# assets.asset

<a name="assets.asset.Asset"></a>
## Asset Objects
    
```python
class Asset(DDO)
```

<a name="assets.asset.Asset.update_compute_privacy"></a>
#### update\_compute\_privacy

```python
 | update_compute_privacy(trusted_algorithms: list, allow_all: bool, allow_raw_algorithm: bool)
```

Set the `trusted_algorithms` on the compute service.

- An assertion is raised if this asset has no compute service
- Updates the compute service in place
- Adds the trusted algorithms under privacy.publisherTrustedAlgorithms
- If list is empty or trusted_algorithms is None, the `privacy` section is deleted

**Arguments**:

- `trusted_algorithms`: list of dicts, each dict contain the keys
("containerSectionChecksum", "filesChecksum", "did")
- `allow_all`: bool -- set to True to allow all published algorithms to run on this dataset
- `allow_raw_algorithm`: bool -- determine whether raw algorithms (i.e. unpublished) can be run on this dataset

**Returns**:

None
:raises AssertionError if this asset has no `ServiceTypes.CLOUD_COMPUTE` service

