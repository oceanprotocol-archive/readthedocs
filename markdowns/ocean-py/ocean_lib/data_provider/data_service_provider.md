---
title: data_service_provider
slug: ocean_lib/data_provider/data_service_provider
app: ocean.py
module: ocean_lib.data_provider.data_service_provider
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.2-1-g9fb6083/ocean_lib/data_provider/data_service_provider.py
version: 1.0.0-alpha.2
---
Provider module.

## DataServiceProvider

```python
class DataServiceProvider()
```

DataServiceProvider class.

The main functions available are:
- consume_service
- run_compute_service (not implemented yet)

#### get\_http\_client

```python
 | @staticmethod
 | @enforce_types
 | def get_http_client() -> Session
```

Get the http client.

#### set\_http\_client

```python
 | @staticmethod
 | @enforce_types
 | def set_http_client(http_client: Session) -> None
```

Set the http client to something other than the default `requests`.

#### start\_compute\_job

```python
 | @staticmethod
 | def start_compute_job(dataset_compute_service: Any, consumer: Wallet, dataset: ComputeInput, compute_environment: str, algorithm: Optional[ComputeInput] = None, algorithm_meta: Optional[AlgorithmMetadata] = None, algorithm_custom_data: Optional[str] = None, input_datasets: Optional[List[ComputeInput]] = None) -> Dict[str, Any]
```

Start a compute job.

Either algorithm or algorithm_meta must be defined.

**Arguments**:

- `dataset_compute_service`: 
- `consumer`: hex str the ethereum address of the consumer executing the compute job
- `dataset`: ComputeInput dataset with a compute service
- `compute_environment`: str compute environment id
- `algorithm`: ComputeInput algorithm witha download service.
- `algorithm_meta`: AlgorithmMetadata algorithm metadata
- `algorithm_custom_data`: dict customizable algo parameters (ie. no of iterations, etc)
- `input_datasets`: List[ComputeInput] additional input datasets
:return job_info dict

#### stop\_compute\_job

```python
 | @staticmethod
 | @enforce_types
 | def stop_compute_job(did: str, job_id: str, dataset_compute_service: Any, consumer: Wallet) -> Dict[str, Any]
```

**Arguments**:

- `did`: hex str the asset/DDO id
- `job_id`: str id of compute job that was returned from `start_compute_job`
- `dataset_compute_service`: 
- `consumer`: Wallet of the consumer's account

**Returns**:

bool whether the job was stopped successfully

#### delete\_compute\_job

```python
 | @staticmethod
 | @enforce_types
 | def delete_compute_job(did: str, job_id: str, dataset_compute_service: Any, consumer: Wallet) -> Dict[str, str]
```

**Arguments**:

- `did`: hex str the asset/DDO id
- `job_id`: str id of compute job that was returned from `start_compute_job`
- `dataset_compute_service`: 
- `consumer`: Wallet of the consumer's account

**Returns**:

bool whether the job was deleted successfully

#### compute\_job\_status

```python
 | @staticmethod
 | @enforce_types
 | def compute_job_status(did: str, job_id: str, dataset_compute_service: Any, consumer: Wallet) -> Dict[str, Any]
```

**Arguments**:

- `did`: hex str the asset/DDO id
- `job_id`: str id of compute job that was returned from `start_compute_job`
- `dataset_compute_service`: 
- `consumer`: Wallet of the consumer's account

**Returns**:

dict of job_id to status info. When job_id is not provided, this will return
status for each job_id that exist for the did

#### compute\_job\_result

```python
 | @staticmethod
 | @enforce_types
 | def compute_job_result(job_id: str, index: int, dataset_compute_service: Any, consumer: Wallet) -> Dict[str, Any]
```

**Arguments**:

- `job_id`: str id of compute job that was returned from `start_compute_job`
- `index`: int compute result index
- `dataset_compute_service`: 
- `consumer`: Wallet of the consumer's account

**Returns**:

dict of job_id to result urls.

#### get\_url

```python
 | @staticmethod
 | @enforce_types
 | def get_url(config: Config) -> str
```

Return the DataProvider component url.

**Arguments**:

- `config`: Config

**Returns**:

Url, str

#### get\_service\_endpoints

```python
 | @staticmethod
 | @enforce_types
 | def get_service_endpoints(provider_uri: str) -> Dict[str, List[str]]
```

Return the service endpoints from the provider URL.

#### get\_c2d\_environments

```python
 | @staticmethod
 | @enforce_types
 | def get_c2d_environments(provider_uri: str) -> Optional[str]
```

Return the provider address

#### get\_provider\_address

```python
 | @staticmethod
 | @enforce_types
 | def get_provider_address(provider_uri: str) -> Optional[str]
```

Return the provider address

#### write\_file

```python
 | @staticmethod
 | @enforce_types
 | def write_file(response: Response, destination_folder: Union[str, bytes, os.PathLike], file_name: str) -> None
```

Write the response content in a file in the destination folder.

**Arguments**:

- `response`: Response
- `destination_folder`: Destination folder, string
- `file_name`: File name, string

**Returns**:

None

