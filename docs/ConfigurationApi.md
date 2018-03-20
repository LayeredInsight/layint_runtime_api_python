# layint_runtime_api.ConfigurationApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_config**](ConfigurationApi.md#add_config) | **POST** /Configs | Create new configuration definition
[**delete_config**](ConfigurationApi.md#delete_config) | **DELETE** /Configs/{configID} | Delete configuration
[**get_config**](ConfigurationApi.md#get_config) | **GET** /Configs/{configID} | Get configuration
[**get_config_by_name**](ConfigurationApi.md#get_config_by_name) | **GET** /Configs/ByName/{configName} | Get configuration by name
[**list_all_configurations**](ConfigurationApi.md#list_all_configurations) | **GET** /Configs | Get configurations
[**update_config**](ConfigurationApi.md#update_config) | **POST** /Configs/{configID} | Update configuration


# **add_config**
> Config add_config(config=config)

Create new configuration definition

Creates a configuration object. ID SHOULD NOT be passed when creating a new configuration.

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
api_instance = layint_runtime_api.ConfigurationApi()
config = layint_runtime_api.Config() # Config |  (optional)

try: 
    # Create new configuration definition
    api_response = api_instance.add_config(config=config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->add_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**Config**](Config.md)|  | [optional] 

### Return type

[**Config**](Config.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_config**
> delete_config(config_id)

Delete configuration

Delete configuration.

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
api_instance = layint_runtime_api.ConfigurationApi()
config_id = 'config_id_example' # str | hexadecimal ID of config to delete

try: 
    # Delete configuration
    api_instance.delete_config(config_id)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| hexadecimal ID of config to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> Config get_config(config_id)

Get configuration

Returns details about the specified configuration.

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
api_instance = layint_runtime_api.ConfigurationApi()
config_id = 'config_id_example' # str | hexadecimal ID of config to return

try: 
    # Get configuration
    api_response = api_instance.get_config(config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| hexadecimal ID of config to return | 

### Return type

[**Config**](Config.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_by_name**
> Config get_config_by_name(config_name)

Get configuration by name

Returns details about the specified configuration.

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
api_instance = layint_runtime_api.ConfigurationApi()
config_name = 'config_name_example' # str | Name of config to return

try: 
    # Get configuration by name
    api_response = api_instance.get_config_by_name(config_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_config_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_name** | **str**| Name of config to return | 

### Return type

[**Config**](Config.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_configurations**
> Configs list_all_configurations()

Get configurations

Returns a list of configurations that are accessible to this user.

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
api_instance = layint_runtime_api.ConfigurationApi()

try: 
    # Get configurations
    api_response = api_instance.list_all_configurations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->list_all_configurations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Configs**](Configs.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config**
> update_config(config_id, config=config)

Update configuration

Update configurations parameters

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
api_instance = layint_runtime_api.ConfigurationApi()
config_id = 'config_id_example' # str | hexadecimal ID of config to delete
config = layint_runtime_api.UpdateConfig() # UpdateConfig |  (optional)

try: 
    # Update configuration
    api_instance.update_config(config_id, config=config)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| hexadecimal ID of config to delete | 
 **config** | [**UpdateConfig**](UpdateConfig.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

