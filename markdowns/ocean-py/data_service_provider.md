---
title: data_service_provider
slug: /read-the-docs/ocean-py/data_service_provider
app: ocean.py
module: ocean_lib.data_provider.data_service_provider
---
Provider module.

## DataServiceProvider

```python
@enforce_types_shim
class DataServiceProvider()
```

DataServiceProvider class.

The main functions available are:
- consume_service
- run_compute_service (not implemented yet)

#### get\_http\_client

```python
 | @staticmethod
 | def get_http_client()
```

Get the http client.

#### set\_http\_client

```python
 | @staticmethod
 | def set_http_client(http_client)
```

Set the http client to something other than the default `requests`.

#### get\_order\_requirements

```python
 | @staticmethod
 | def get_order_requirements(did, service_endpoint, consumer_address, service_id, service_type, token_address)
```

**Arguments**:

- `did`: 
- `service_endpoint`: 
- `consumer_address`: hex str the ethereum account address of the consumer
- `service_id`: 
- `service_type`: 
- `token_address`: 

**Returns**:

OrderRequirements instance -- named tuple (amount, data_token_address, receiver_address, nonce),

#### download\_service

```python
 | @staticmethod
 | def download_service(did, service_endpoint, wallet, files, destination_folder, service_id, token_address, order_tx_id, index=None)
```

Call the provider endpoint to get access to the different files that form the asset.

**Arguments**:

- `did`: str id of the asset
- `service_endpoint`: Url to consume, str
- `wallet`: hex str Wallet instance of the consumer signing this request
- `files`: List containing the files to be consumed, list
- `destination_folder`: Path, str
- `service_id`: integer the id of the service inside the DDO's service dict
- `token_address`: hex str the data token address associated with this asset/service
- `order_tx_id`: hex str the transaction hash for the required data token
transfer (tokens of the same token address above)
- `index`: Index of the document that is going to be downloaded, int

**Returns**:

True if was downloaded, bool

#### start\_compute\_job

```python
 | @staticmethod
 | def start_compute_job(did: str, service_endpoint: str, consumer_address: str, signature: str, service_id: int, order_tx_id: str, algorithm_did: str = None, algorithm_meta: AlgorithmMetadata = None, algorithm_tx_id: str = None, algorithm_data_token: str = None, output: dict = None, input_datasets: list = None, job_id: str = None)
```

**Arguments**:

- `did`: id of asset starting with `did:op:` and a hex str without 0x prefix
- `service_endpoint`: 
- `consumer_address`: hex str the ethereum address of the consumer executing the compute job
- `signature`: hex str signed message to allow the provider to authorize the consumer
- `service_id`: 
- `order_tx_id`: hex str id of the token transfer transaction
- `algorithm_did`: str -- the asset did (of `algorithm` type) which consist of `did:op:` and
the assetId hex str (without `0x` prefix)
- `algorithm_meta`: see `OceanCompute.execute`
- `algorithm_tx_id`: transaction hash of algorithm StartOrder tx (Required when using `algorithm_did`)
- `algorithm_data_token`: datatoken address of this algorithm (Required when using `algorithm_did`)
- `output`: see `OceanCompute.execute`
- `input_datasets`: list of ComputeInput
- `job_id`: str id of compute job that was started and stopped (optional, use it
here to start a job after it was stopped)

**Returns**:

job_info dict with jobId, status, and other values

#### stop\_compute\_job

```python
 | @staticmethod
 | def stop_compute_job(did, job_id, service_endpoint, consumer_address, signature)
```

**Arguments**:

- `did`: hex str the asset/DDO id
- `job_id`: str id of compute job that was returned from `start_compute_job`
- `service_endpoint`: str url of the provider service endpoint for compute service
- `consumer_address`: hex str the ethereum address of the consumer's account
- `signature`: hex str signed message to allow the provider to authorize the consumer

**Returns**:

bool whether the job was stopped successfully

#### restart\_compute\_job

```python
 | @staticmethod
 | def restart_compute_job(did, job_id, service_endpoint, consumer_address, signature, service_id, order_tx_id, algorithm_did=None, algorithm_meta=None, output=None, input_datasets=None)
```

**Arguments**:

- `did`: id of asset starting with `did:op:` and a hex str without 0x prefix
- `job_id`: str id of compute job that was started and stopped (optional, use it
here to start a job after it was stopped)
- `service_endpoint`: 
- `consumer_address`: hex str the ethereum address of the consumer executing the compute job
- `signature`: hex str signed message to allow the provider to authorize the consumer
- `service_id`: 
- `token_address`: 
- `order_tx_id`: hex str id of the token transfer transaction
- `algorithm_did`: str -- the asset did (of `algorithm` type) which consist of `did:op:` and
the assetId hex str (without `0x` prefix)
- `algorithm_meta`: see `OceanCompute.execute`
- `output`: see `OceanCompute.execute`
- `input_datasets`: list of ComputeInput

**Returns**:

bool whether the job was restarted successfully

#### delete\_compute\_job

```python
 | @staticmethod
 | def delete_compute_job(did, job_id, service_endpoint, consumer_address, signature)
```

**Arguments**:

- `did`: hex str the asset/DDO id
- `job_id`: str id of compute job that was returned from `start_compute_job`
- `service_endpoint`: str url of the provider service endpoint for compute service
- `consumer_address`: hex str the ethereum address of the consumer's account
- `signature`: hex str signed message to allow the provider to authorize the consumer

**Returns**:

bool whether the job was deleted successfully

#### compute\_job\_status

```python
 | @staticmethod
 | def compute_job_status(did, job_id, service_endpoint, consumer_address, signature)
```

**Arguments**:

- `did`: hex str the asset/DDO id
- `job_id`: str id of compute job that was returned from `start_compute_job`
- `service_endpoint`: str url of the provider service endpoint for compute service
- `consumer_address`: hex str the ethereum address of the consumer's account
- `signature`: hex str signed message to allow the provider to authorize the consumer

**Returns**:

dict of job_id to status info. When job_id is not provided, this will return
status for each job_id that exist for the did

#### compute\_job\_result

```python
 | @staticmethod
 | def compute_job_result(did, job_id, service_endpoint, consumer_address, signature)
```

**Arguments**:

- `did`: hex str the asset/DDO id
- `job_id`: str id of compute job that was returned from `start_compute_job`
- `service_endpoint`: str url of the provider service endpoint for compute service
- `consumer_address`: hex str the ethereum address of the consumer's account
- `signature`: hex str signed message to allow the provider to authorize the consumer

**Returns**:

dict of job_id to result urls. When job_id is not provided, this will return
result for each job_id that exist for the did

#### get\_url

```python
 | @staticmethod
 | def get_url(config)
```

Return the DataProvider component url.

**Arguments**:

- `config`: Config

**Returns**:

Url, str

#### get\_service\_endpoints

```python
 | @staticmethod
 | def get_service_endpoints(provider_uri=None)
```

Return the service endpoints from the provider URL.

#### get\_provider\_address

```python
 | @staticmethod
 | def get_provider_address(provider_uri=None)
```

Return the provider address

#### write\_file

```python
 | @staticmethod
 | def write_file(response, destination_folder, file_name)
```

Write the response content in a file in the destination folder.

**Arguments**:

- `response`: Response
- `destination_folder`: Destination folder, string
- `file_name`: File name, string

**Returns**:

bool

