---
title: ocean_compute
slug: ocean_lib/ocean/ocean_compute
app: ocean.py
module: ocean_lib.ocean.ocean_compute
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/ocean/ocean_compute.py
version: 1.0.0-alpha.1
---
## OceanCompute

```python
class OceanCompute()
```

Ocean assets class.

#### \_\_init\_\_

```python
 | @enforce_types
 | def __init__(config: Union[Config, Dict], data_provider: Type[DataServiceProvider]) -> None
```

Initialises OceanCompute class.

#### status

```python
 | @enforce_types
 | def status(asset: Asset, service: Service, job_id: str, wallet: Wallet) -> Dict[str, Any]
```

Gets job status.

**Arguments**:

- `asset`: Asset offering the compute service of this job
- `service`: compute service of this job
- `job_id`: str id of the compute job
- `wallet`: Wallet instance

**Returns**:

dict the status for an existing compute job, keys are (ok, status, statusText)

#### result

```python
 | @enforce_types
 | def result(asset: Asset, service: Service, job_id: str, index: int, wallet: Wallet) -> Dict[str, Any]
```

Gets job result.

**Arguments**:

- `asset`: Asset offering the compute service of this job
- `service`: compute service of this job
- `job_id`: str id of the compute job
- `index`: compute result index
- `wallet`: Wallet instance

**Returns**:

dict the results/logs urls for an existing compute job, keys are (did, urls, logs)

#### stop

```python
 | @enforce_types
 | def stop(asset: Asset, service: Service, job_id: str, wallet: Wallet) -> Dict[str, Any]
```

Attempt to stop the running compute job.

**Arguments**:

- `asset`: Asset offering the compute service of this job
- `job_id`: str id of the compute job
- `wallet`: Wallet instance

**Returns**:

dict the status for the stopped compute job, keys are (ok, status, statusText)

