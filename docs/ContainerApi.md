# layint_runtime_api.ContainerApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_container_dossier_tempate**](ContainerApi.md#build_container_dossier_tempate) | **GET** /Containers/{containerID}/DossierTemplate | Builds a security policy based on containers behavior
[**get_container_dossier**](ContainerApi.md#get_container_dossier) | **GET** /Containers/{containerID}/Dossier | Gets dossier for container
[**get_container_logs**](ContainerApi.md#get_container_logs) | **GET** /Containers/{containerID}/GetContainerLogs | Gets behavioral logs for container
[**get_containers**](ContainerApi.md#get_containers) | **GET** /Containers | Get containers
[**toggle_container_sniffer**](ContainerApi.md#toggle_container_sniffer) | **POST** /Containers/{containerID}/ToggleSniffer | Toggles network sniffer


# **build_container_dossier_tempate**
> DossierTemplateResponse build_container_dossier_tempate(container_id, merge_policy_id=merge_policy_id, log_action=log_action)

Builds a security policy based on containers behavior

This call builds a new custom security policy based on the recorded activities of the container.

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
api_instance = layint_runtime_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to gather dossier for
merge_policy_id = 'merge_policy_id_example' # str | hexadecimal ID of policy to merge gathered dossier rules (optional)
log_action = 'all' # str | action string to match action type in log for gathered dossier rules (optional) (default to all)

try: 
    # Builds a security policy based on containers behavior
    api_response = api_instance.build_container_dossier_tempate(container_id, merge_policy_id=merge_policy_id, log_action=log_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->build_container_dossier_tempate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to gather dossier for | 
 **merge_policy_id** | **str**| hexadecimal ID of policy to merge gathered dossier rules | [optional] 
 **log_action** | **str**| action string to match action type in log for gathered dossier rules | [optional] [default to all]

### Return type

[**DossierTemplateResponse**](DossierTemplateResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_dossier**
> Dossier get_container_dossier(container_id)

Gets dossier for container

This call produces a list of all data Witness has learend about the container

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
api_instance = layint_runtime_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to gather dossier for

try: 
    # Gets dossier for container
    api_response = api_instance.get_container_dossier(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_dossier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to gather dossier for | 

### Return type

[**Dossier**](Dossier.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_logs**
> ContainerLogs get_container_logs(container_id, page_size=page_size, page=page)

Gets behavioral logs for container

This call produces a list of all behavior logs Witness has received for the container

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
api_instance = layint_runtime_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to gather logs for
page_size = 56 # int | Maximum number of log records to return per \"page\" (think pager in a browser) (optional)
page = 56 # int | Page number of results to return. Results will start with record number (Page * PageSize) (optional)

try: 
    # Gets behavioral logs for container
    api_response = api_instance.get_container_logs(container_id, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to gather logs for | 
 **page_size** | **int**| Maximum number of log records to return per \&quot;page\&quot; (think pager in a browser) | [optional] 
 **page** | **int**| Page number of results to return. Results will start with record number (Page * PageSize) | [optional] 

### Return type

[**ContainerLogs**](ContainerLogs.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_containers**
> Containers get_containers()

Get containers

Returns a list of containers that are accessible to this user.

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
api_instance = layint_runtime_api.ContainerApi()

try: 
    # Get containers
    api_response = api_instance.get_containers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_containers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Containers**](Containers.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_container_sniffer**
> Container toggle_container_sniffer(container_id)

Toggles network sniffer

Toggles network sniffer on/off for specified container. This call doesn't take any parameters beside the container ID - each call of the API toggles the sniffer setting between enabled and disabled. Sniffer in a running container will change status within 30 seconds of this API call.

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
api_instance = layint_runtime_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of registry to return

try: 
    # Toggles network sniffer
    api_response = api_instance.toggle_container_sniffer(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->toggle_container_sniffer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of registry to return | 

### Return type

[**Container**](Container.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

