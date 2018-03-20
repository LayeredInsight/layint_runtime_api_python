# layint_runtime_api.RegistryApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_registry**](RegistryApi.md#add_registry) | **POST** /Registries | Create new registry definition
[**delete_registry**](RegistryApi.md#delete_registry) | **DELETE** /Registries/{registryID} | Delete specified registry
[**get_registries**](RegistryApi.md#get_registries) | **GET** /Registries | Get defined registries
[**get_registry**](RegistryApi.md#get_registry) | **GET** /Registries/{registryID} | Get specified registry
[**get_registry_by_name**](RegistryApi.md#get_registry_by_name) | **GET** /Registries/ByName/{registryName} | Get registry by name
[**list_all_images_in_registry**](RegistryApi.md#list_all_images_in_registry) | **GET** /Registries/{registryID}/Images | Get container images in registry
[**update_registry**](RegistryApi.md#update_registry) | **POST** /Registries/{registryID} | Update specified registry


# **add_registry**
> Registry add_registry(registry=registry)

Create new registry definition

Creates a registry object which can then be used to specify where container images are stored. ID SHOULD NOT be passed when creating a new registry.

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
api_instance = layint_runtime_api.RegistryApi()
registry = layint_runtime_api.Registry() # Registry |  (optional)

try: 
    # Create new registry definition
    api_response = api_instance.add_registry(registry=registry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->add_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | [**Registry**](Registry.md)|  | [optional] 

### Return type

[**Registry**](Registry.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registry**
> delete_registry(registry_id)

Delete specified registry

Deletes the specified registry.

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
api_instance = layint_runtime_api.RegistryApi()
registry_id = 'registry_id_example' # str | hexadecimal ID of registry to delete

try: 
    # Delete specified registry
    api_instance.delete_registry(registry_id)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| hexadecimal ID of registry to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registries**
> Registries get_registries()

Get defined registries

Returns a list of defined images that are accessible to this user.

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
api_instance = layint_runtime_api.RegistryApi()

try: 
    # Get defined registries
    api_response = api_instance.get_registries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_registries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Registries**](Registries.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry**
> Registry get_registry(registry_id)

Get specified registry

Returns details about the specified registry.

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
api_instance = layint_runtime_api.RegistryApi()
registry_id = 'registry_id_example' # str | hexadecimal ID of registry to get

try: 
    # Get specified registry
    api_response = api_instance.get_registry(registry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| hexadecimal ID of registry to get | 

### Return type

[**Registry**](Registry.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_by_name**
> Registry get_registry_by_name(registry_name)

Get registry by name

Returns details about a registry matching the passed name.

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
api_instance = layint_runtime_api.RegistryApi()
registry_name = 'registry_name_example' # str | Name of registry to get

try: 
    # Get registry by name
    api_response = api_instance.get_registry_by_name(registry_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_registry_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_name** | **str**| Name of registry to get | 

### Return type

[**Registry**](Registry.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_images_in_registry**
> Image list_all_images_in_registry(registry_id)

Get container images in registry

Returns an array of images which are definied as using the specified registry.

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
api_instance = layint_runtime_api.RegistryApi()
registry_id = 'registry_id_example' # str | hexadecimal ID of registry to get list of images for

try: 
    # Get container images in registry
    api_response = api_instance.list_all_images_in_registry(registry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->list_all_images_in_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| hexadecimal ID of registry to get list of images for | 

### Return type

[**Image**](Image.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_registry**
> Registry update_registry(registry_id, registry=registry)

Update specified registry

Updates the specified registry with data passed in request body.

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
api_instance = layint_runtime_api.RegistryApi()
registry_id = 'registry_id_example' # str | hexadecimal ID of registry to update
registry = layint_runtime_api.Registry() # Registry |  (optional)

try: 
    # Update specified registry
    api_response = api_instance.update_registry(registry_id, registry=registry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->update_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| hexadecimal ID of registry to update | 
 **registry** | [**Registry**](Registry.md)|  | [optional] 

### Return type

[**Registry**](Registry.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

