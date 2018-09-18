# layint_runtime_api.PolicyApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policy**](PolicyApi.md#add_policy) | **POST** /Policies | Create new security policy
[**delete_policy**](PolicyApi.md#delete_policy) | **DELETE** /Policies/{policyID} | Delete policy
[**get_containers_running_policy**](PolicyApi.md#get_containers_running_policy) | **GET** /Policies/{policyID}/Containers | Get containers running a specific policy
[**get_policies**](PolicyApi.md#get_policies) | **GET** /Policies | Get all policies
[**get_policy**](PolicyApi.md#get_policy) | **GET** /Policies/{policyID} | Get specific policy
[**get_policy_by_name**](PolicyApi.md#get_policy_by_name) | **GET** /Policies/ByName/{policyName} | Get specific policy by name
[**seccomp**](PolicyApi.md#seccomp) | **GET** /Policies/{policyID}/Seccomp | Get a Seccomp policy derivied from a LI policy
[**suspend_policy**](PolicyApi.md#suspend_policy) | **POST** /Policies/{policyID}/Suspend | Suspend security policy
[**update_policy**](PolicyApi.md#update_policy) | **POST** /Policies/{policyID} | Update security policy


# **add_policy**
> Policy add_policy(policy=policy)

Create new security policy

Creates a security policy object. ID SHOULD NOT be passed when creating a new policy.

### Example 
```python
from __future__ import print_function
import time
import layint_runtime_api
from layint_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_runtime_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_runtime_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_runtime_api.PolicyApi()
policy = layint_runtime_api.Policy() # Policy |  (optional)

try: 
    # Create new security policy
    api_response = api_instance.add_policy(policy=policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->add_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**Policy**](Policy.md)|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(policy_id)

Delete policy

### Example 
```python
from __future__ import print_function
import time
import layint_runtime_api
from layint_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_runtime_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_runtime_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_runtime_api.PolicyApi()
policy_id = 'policy_id_example' # str | hexadecimal ID of policy to delete

try: 
    # Delete policy
    api_instance.delete_policy(policy_id)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| hexadecimal ID of policy to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_containers_running_policy**
> Containers get_containers_running_policy(policy_id)

Get containers running a specific policy

Returns list of containers running the policy with the specified ID

### Example 
```python
from __future__ import print_function
import time
import layint_runtime_api
from layint_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_runtime_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_runtime_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_runtime_api.PolicyApi()
policy_id = 'policy_id_example' # str | hexadecimal ID of policy to find containers running

try: 
    # Get containers running a specific policy
    api_response = api_instance.get_containers_running_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_containers_running_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| hexadecimal ID of policy to find containers running | 

### Return type

[**Containers**](Containers.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies**
> Policies get_policies()

Get all policies

Returns a list of policies that are accessible to this user.

### Example 
```python
from __future__ import print_function
import time
import layint_runtime_api
from layint_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_runtime_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_runtime_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_runtime_api.PolicyApi()

try: 
    # Get all policies
    api_response = api_instance.get_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Policies**](Policies.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> Policy get_policy(policy_id)

Get specific policy

Returns details for policy with matching ID.

### Example 
```python
from __future__ import print_function
import time
import layint_runtime_api
from layint_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_runtime_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_runtime_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_runtime_api.PolicyApi()
policy_id = 'policy_id_example' # str | hexadecimal ID of policy to get

try: 
    # Get specific policy
    api_response = api_instance.get_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| hexadecimal ID of policy to get | 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_by_name**
> Policy get_policy_by_name(policy_name)

Get specific policy by name

Returns details for policy with matching name.

### Example 
```python
from __future__ import print_function
import time
import layint_runtime_api
from layint_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_runtime_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_runtime_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_runtime_api.PolicyApi()
policy_name = 'policy_name_example' # str | Name of policy to search database for

try: 
    # Get specific policy by name
    api_response = api_instance.get_policy_by_name(policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Name of policy to search database for | 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seccomp**
> seccomp(policy_id, li_agent=li_agent)

Get a Seccomp policy derivied from a LI policy

### Example 
```python
from __future__ import print_function
import time
import layint_runtime_api
from layint_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_runtime_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_runtime_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_runtime_api.PolicyApi()
policy_id = 'policy_id_example' # str | hexadecimal ID of policy
li_agent = false # bool | If true, the policy will include whitelisted syscalls for the LI agent. (optional) (default to false)

try: 
    # Get a Seccomp policy derivied from a LI policy
    api_instance.seccomp(policy_id, li_agent=li_agent)
except ApiException as e:
    print("Exception when calling PolicyApi->seccomp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| hexadecimal ID of policy | 
 **li_agent** | **bool**| If true, the policy will include whitelisted syscalls for the LI agent. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_policy**
> Policy suspend_policy(policy_id)

Suspend security policy

Suspends a policy so it won't block anything.

### Example 
```python
from __future__ import print_function
import time
import layint_runtime_api
from layint_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_runtime_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_runtime_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_runtime_api.PolicyApi()
policy_id = 'policy_id_example' # str | hexadecimal ID of policy to suspend

try: 
    # Suspend security policy
    api_response = api_instance.suspend_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->suspend_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| hexadecimal ID of policy to suspend | 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> Policy update_policy(policy_id, policy=policy)

Update security policy

Updates a specified security policy object.

### Example 
```python
from __future__ import print_function
import time
import layint_runtime_api
from layint_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_runtime_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_runtime_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_runtime_api.PolicyApi()
policy_id = 'policy_id_example' # str | hexadecimal ID of policy to update
policy = layint_runtime_api.Policy() # Policy |  (optional)

try: 
    # Update security policy
    api_response = api_instance.update_policy(policy_id, policy=policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| hexadecimal ID of policy to update | 
 **policy** | [**Policy**](Policy.md)|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

