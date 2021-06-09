---
title: ocean_compute
slug: ocean_lib/ocean/ocean_compute
app: ocean.py
module: ocean_lib.ocean.ocean_compute
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/ocean/ocean_compute.py
version: 0.5.24
---
## OceanCompute

```python
@enforce_types
class OceanCompute()
```

Ocean assets class.

#### \_\_init\_\_

```python
 | def __init__(config, data_provider)
```

Initialises OceanCompute class.

#### build\_cluster\_attributes

```python
 | @staticmethod
 | def build_cluster_attributes(cluster_type, url)
```

Builds cluster attributes.

**Arguments**:

- `cluster_type`: str (e.g. Kubernetes)
- `url`: str (e.g. http://10.0.0.17/xxx)

**Returns**:



#### build\_container\_attributes

```python
 | @staticmethod
 | def build_container_attributes(image, tag, entrypoint)
```

Builds container attributes.

**Arguments**:

- `image`: str name of Docker image (e.g. node)
- `tag`: str the Docker image tag (e.g. latest or a specific version number)
- `entrypoint`: str executable file (e.g. node $ALGO)

**Returns**:



#### build\_server\_attributes

```python
 | @staticmethod
 | def build_server_attributes(server_id, server_type, cpu, gpu, memory, disk, max_run_time)
```

Builds server attributes.

**Arguments**:

- `server_id`: str
- `server_type`: str
- `cpu`: integer number of available cpu units
- `gpu`: integer number of available gpu units
- `memory`: str amount of RAM memory (in mb or gb)
- `disk`: str storage capacity (in gb, tb, etc.)
- `max_run_time`: integer maximum allowed run time in seconds

**Returns**:



#### build\_service\_provider\_attributes

```python
 | @staticmethod
 | def build_service_provider_attributes(provider_type, description, cluster, containers, servers)
```

Return a dict with attributes describing the details of compute resources in this service

**Arguments**:

- `provider_type`: str type of resource provider such as Azure or AWS
- `description`: str details describing the resource provider
- `cluster`: dict attributes describing the cluster (see `build_cluster_attributes`)
- `containers`: list of dicts each has attributes describing the container (see `build_container_attributes`)
- `servers`: list of dicts each has attributes to describe server (see `build_server_attributes`)

**Returns**:



#### build\_service\_privacy\_attributes

```python
 | @staticmethod
 | def build_service_privacy_attributes(trusted_algorithms: list = None, metadata_cache_uri: str = None, allow_raw_algorithm: bool = False, allow_all_published_algorithms: bool = False, allow_network_access: bool = False)
```

**Arguments**:

- `trusted_algorithms`: list of algorithm did to be trusted by the compute service provider
- `metadata_cache_uir`: URI used to get DDOs for trusted algorithm DIDs if trusted_algorithms set
- `allow_raw_algorithm`: bool -- when True, unpublished raw algorithm code can be run on this dataset
- `allow_all_published_algorithms`: bool -- when True, any published algorithm can be run on this dataset
The list of `trusted_algorithms` will be ignored in this case.
- `allow_network_access`: bool -- allow/disallow the algorithm network access during execution

**Returns**:

dict

#### create\_compute\_service\_attributes

```python
 | @staticmethod
 | def create_compute_service_attributes(timeout: int, creator: str, date_published: str, provider_attributes: dict = None, privacy_attributes: dict = None)
```

Creates compute service attributes.

**Arguments**:

- `timeout`: integer maximum amount of running compute service in seconds
- `creator`: str ethereum address
- `date_published`: str timestamp (datetime.utcnow().replace(microsecond=0).isoformat() + "Z")
- `provider_attributes`: dict describing the details of the compute resources (see `build_service_provider_attributes`)
- `privacy_attributes`: dict specifying what algorithms can be run in this compute service

**Returns**:

dict with `main` key and value contain the minimum required attributes of a compute service

#### check\_output\_dict

```python
 | @staticmethod
 | def check_output_dict(output_def, consumer_address, data_provider, config: Config)
```

Validate the `output_def` dict and fills in defaults for missing values.

**Arguments**:

- `output_def`: dict
- `consumer_address`: hex str the consumer ethereum address
- `data_provider`: DataServiceProvider class or similar interface
- `config`: Config instance

**Returns**:

dict a valid `output_def` object

#### create\_compute\_service\_descriptor

```python
 | def create_compute_service_descriptor(attributes)
```

Return a service descriptor (tuple) for service of type ServiceTypes.CLOUD_COMPUTE
and having the required attributes and service endpoint.

**Arguments**:

- `attributes`: dict as created in `create_compute_service_attributes`

#### start

```python
 | def start(input_datasets: list, consumer_wallet: Wallet, nonce: Optional[int] = None, algorithm_did: Optional[str] = None, algorithm_meta: Optional[AlgorithmMetadata] = None, algorithm_tx_id: str = None, algorithm_data_token: str = None, output: dict = None, job_id: str = None)
```

Start a remote compute job on the asset files.

Files are identified by `did` after verifying that the provider service is active and transferring the
number of data-tokens required for using this compute service.

**Arguments**:

- `input_datasets`: list of ComputeInput -- list of input datasets to the compute job. A dataset is
represented with ComputeInput struct
- `consumer_wallet`: Wallet instance of the consumer ordering the service
- `nonce`: int value to use in the signature
- `algorithm_did`: str -- the asset did (of `algorithm` type) which consist of `did:op:` and
the assetId hex str (without `0x` prefix)
- `algorithm_meta`: `AlgorithmMetadata` instance -- metadata about the algorithm being run if
`algorithm` is being used. This is ignored when `algorithm_did` is specified.
- `algorithm_tx_id`: transaction hash of algorithm StartOrder tx (Required when using `algorithm_did`)
- `algorithm_data_token`: datatoken address of this algorithm (Required when using `algorithm_did`)
- `output`: dict object to be used in publishing mechanism, must define
- `job_id`: str identifier of a compute job that was previously started and
stopped (if supported by the provider's  backend)

**Returns**:

str -- id of compute job being executed

#### status

```python
 | def status(did, job_id, wallet)
```

Gets job status.

**Arguments**:

- `did`: str id of the asset offering the compute service of this job
- `job_id`: str id of the compute job
- `wallet`: Wallet instance

**Returns**:

dict the status for an existing compute job, keys are (ok, status, statusText)

#### result

```python
 | def result(did, job_id, wallet)
```

Gets job result.

**Arguments**:

- `did`: str id of the asset offering the compute service of this job
- `job_id`: str id of the compute job
- `wallet`: Wallet instance

**Returns**:

dict the results/logs urls for an existing compute job, keys are (did, urls, logs)

#### stop

```python
 | def stop(did, job_id, wallet)
```

Attempt to stop the running compute job.

**Arguments**:

- `did`: str id of the asset offering the compute service of this job
- `job_id`: str id of the compute job
- `wallet`: Wallet instance

**Returns**:

dict the status for the stopped compute job, keys are (ok, status, statusText)

