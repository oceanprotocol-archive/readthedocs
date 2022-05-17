---
title: compute
slug: ocean_provider/routes/compute
app: provider
module: ocean_provider.routes.compute
source: https://github.com/oceanprotocol/provider/blob/v1.0.9/ocean_provider/routes/compute.py
version: 1.0.9
---
#### initializeCompute

```python
@services.route("/initializeCompute", methods=["POST"])
@validate(InitializeComputeRequest)
def initializeCompute()
```

Initialize a compute service request, with possible additional access requests.
In order to consume a data service the user is required to send
one datatoken to the provider, as well as provider fees for the compute job.

The datatoken is transferred via the ethereum blockchain network
by requesting the user to sign an ERC20 approval transaction
where the approval is given to the provider's ethereum account for
the number of tokens required by the service.

Accepts a payload similar to startCompute: a list of datasets (json object),
algorithm (algorithm description object), validUntil and env parameters.
Adding a transferTxId value to a dataset object will attempt to reuse that order
and return renewed provider fees if necessary.

responses:
  400:
    description: One or more of the required attributes are missing or invalid.
  503:
    description: Service Unavailable.

return:
    json object as follows:
    ```JSON
    {
        "datatoken": <data-token-contract-address>,
        "providerFee": <object containing provider fees>,
        "validOrder": <validated transfer if order can be reused.>
    }
    ```

#### computeDelete

```python
@services.route("/compute", methods=["DELETE"])
@validate_compute_request
@validate(ComputeRequest)
def computeDelete()
```

Deletes a workflow.

---
tags:
  - services
consumes:
  - application/json
parameters:
  - name: signature
    in: query
    description: Signature of the documentId to verify that the consumer has rights to download the asset.
    type: string
  - name: documentId
    in: query
    description: The ID of the asset
    required: true
    type: string
  - name: consumerAddress
    in: query
    description: The consumer address.
    required: true
    type: string
  - name: jobId
    in: query
    description: JobId.
    type: string
responses:
  200:
    description: Call to the operator-service was successful.
  400:
    description: One or more of the required attributes are missing or invalid.
  401:
    description: Invalid asset data.
  503:
    description: Service Unavailable

#### computeStop

```python
@services.route("/compute", methods=["PUT"])
@validate_compute_request
@validate(ComputeRequest)
def computeStop()
```

Stop the execution of a workflow.

---
tags:
  - services
consumes:
  - application/json
parameters:
  - name: signature
    in: query
    description: Signature of (consumerAddress+jobId+documentId) to verify the consumer of
        this compute job/asset. The signature uses ethereum based signing method
        (see https://github.com/ethereum/EIPs/pull/683)
    type: string
  - name: documentId
    in: query
    description: The ID of the asset. If not provided, all currently running compute
        jobs will be stopped for the specified consumerAddress
    required: true
    type: string
  - name: consumerAddress
    in: query
    description: The consumer ethereum address.
    required: true
    type: string
  - name: jobId
    in: query
    description: The ID of the compute job. If not provided, all running compute jobs of
        the specified consumerAddress/documentId are suspended
    type: string
responses:
  200:
    description: Call to the operator-service was successful.
  400:
    description: One or more of the required attributes are missing or invallid.
  401:
    description: Consumer signature is invalid or failed verification.
  503:
    description: Service unavailable

#### computeStatus

```python
@services.route("/compute", methods=["GET"])
@validate_compute_request
@validate(UnsignedComputeRequest)
def computeStatus()
```

Get status for a specific jobId/documentId/owner

---
tags:
  - services
consumes:
  - application/json
parameters:
  - name: jobId
    in: query
    description: The ID of the compute job. If not provided, all running compute jobs of
        the specified consumerAddress/documentId are suspended
    type: string
    required: true
  - name: documentId
    in: query
    description: The ID of the asset. If not provided, the status of all
        currently running and old compute jobs for the specified consumerAddress will be returned.
    type: string
  - name: consumerAddress
    in: query
    description: The consumer ethereum address.
    required: true
    type: string

responses:
  200:
    description: Call to the operator-service was successful.
  400:
    description: One or more of the required attributes are missing or invalid.
  401:
    description: Consumer signature is invalid or failed verification.
  503:
    description: Service Unavailable

#### computeStart

```python
@services.route("/compute", methods=["POST"])
@validate_compute_request
@validate(ComputeStartRequest)
def computeStart()
```

Call the execution of a workflow.

---
tags:
  - services
consumes:
  - application/json
parameters:
  - name: signature
    in: query
    description: Signature of (consumerAddress+jobId+documentId) to verify the consumer of
        this asset/compute job. The signature uses ethereum based signing method
        (see https://github.com/ethereum/EIPs/pull/683)
    type: string
  - name: consumerAddress
    in: query
    description: The consumer ethereum address.
    required: true
    type: string
  - name: computeEnv
    in: query
    description: Compute Environment
    required: true
    type: string
  - name: algorithmDid
    in: query
    description: The DID of the algorithm Asset to be executed
    required: false
    type: string
  - name: algorithmServiceId
    in: query
    description: the id of the service to use to process the algorithm
    required: true
    type: string
  - name: algorithmMeta
    in: query
    description: json object that define the algorithm attributes and url or raw code
    required: false
    type: json string
  - name: output
    in: query
    description: json object that defines the output section
    required: true
    type: json string
responses:
  200:
    description: Call to the operator-service was successful.
  400:
    description: One or more of the required attributes are missing or invalid.
  401:
    description: Consumer signature is invalid or failed verification
  503:
    description: Service unavailable

#### computeResult

```python
@services.route("/computeResult", methods=["GET"])
@validate_compute_request
@validate(ComputeGetResult)
def computeResult()
```

Allows download of asset data result file.

---
tags:
  - services
consumes:
  - application/json
parameters:
  - name: consumerAddress
    in: query
    description: The consumer address.
    required: true
    type: string
  - name: jobId
    in: query
    description: jobId
    required: true
    type: string
  - name: index
    in: query
    description: Result index
    required: true
  - name: nonce
    in: query
    description: The UTC timestamp, used to prevent replay attacks
  - name: signature
    in: query
    description: Signature of (consumerAddress+jobId+index+nonce) to verify that the consumer has rights to download the result
responses:
  200:
    description: Content of the result
  400:
    description: One or more of the required attributes are missing or invalid.
  404:
    description: Result not found
  503:
    description: Service Unavailable

#### computeEnvironments

```python
@services.route("/computeEnvironments", methods=["GET"])
@validate_compute_request
def computeEnvironments()
```

Get list of compute environments

---
tags:
  - services
consumes:
  - application/json

responses:
  200:
    description: Call to the operator-service was successful.
  503:
    description: Service Unavailable
return: list of objects containing information about each compute environment

