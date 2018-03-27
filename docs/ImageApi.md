# layint_runtime_api.ImageApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_image**](ImageApi.md#add_image) | **POST** /Images | Create new image definition
[**assign_configuration_to_image**](ImageApi.md#assign_configuration_to_image) | **POST** /Images/{imageID}/Configs/{configID} | Assign configuration to image
[**assign_policy_to_image**](ImageApi.md#assign_policy_to_image) | **POST** /Images/{imageID}/Policies/{policyID} | Assign security policy to image
[**delete_image**](ImageApi.md#delete_image) | **DELETE** /Images/{imageID} | Delete specified image
[**get_image**](ImageApi.md#get_image) | **GET** /Images/{imageID} | Get specified container image
[**get_images**](ImageApi.md#get_images) | **GET** /Images | Get defined container images
[**instrument_image**](ImageApi.md#instrument_image) | **POST** /Images/{imageID}/Instrument | Request instrumentation of specified container image
[**number_of_instrumented_images**](ImageApi.md#number_of_instrumented_images) | **GET** /Images/NumberOfInstrumentedImages | Returns number of instrumented images
[**show_container_running_image**](ImageApi.md#show_container_running_image) | **GET** /Images/{imageID}/Containers | Get specified container image
[**update_image**](ImageApi.md#update_image) | **POST** /Images/{imageID} | Update image definition


# **add_image**
> Image add_image(image=image, instrument_image=instrument_image)

Create new image definition

Creates a image object. ID SHOULD NOT be passed when creating a new image.

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
api_instance = layint_runtime_api.ImageApi()
image = layint_runtime_api.Image() # Image |  (optional)
instrument_image = 'false' # str | Set to \"true\" to instrument image at time of API call (optional) (default to false)

try: 
    # Create new image definition
    api_response = api_instance.add_image(image=image, instrument_image=instrument_image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->add_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | [**Image**](Image.md)|  | [optional] 
 **instrument_image** | **str**| Set to \&quot;true\&quot; to instrument image at time of API call | [optional] [default to false]

### Return type

[**Image**](Image.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_configuration_to_image**
> assign_configuration_to_image(image_id, config_id)

Assign configuration to image

Assigns the specified configuration to the specified image.

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
api_instance = layint_runtime_api.ImageApi()
image_id = 'image_id_example' # str | hexadecimal ID of image to instrument
config_id = 'config_id_example' # str | hexadecimal ID of configuration to assign to image

try: 
    # Assign configuration to image
    api_instance.assign_configuration_to_image(image_id, config_id)
except ApiException as e:
    print("Exception when calling ImageApi->assign_configuration_to_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| hexadecimal ID of image to instrument | 
 **config_id** | **str**| hexadecimal ID of configuration to assign to image | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_policy_to_image**
> Image assign_policy_to_image(image_id, policy_id)

Assign security policy to image

Assigns the specified security policy to the specified image. Running containers will update to the new policy within one minute.

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
api_instance = layint_runtime_api.ImageApi()
image_id = 'image_id_example' # str | hexadecimal ID of image to instrument
policy_id = 'policy_id_example' # str | hexadecimal ID of policy to assign to image

try: 
    # Assign security policy to image
    api_response = api_instance.assign_policy_to_image(image_id, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->assign_policy_to_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| hexadecimal ID of image to instrument | 
 **policy_id** | **str**| hexadecimal ID of policy to assign to image | 

### Return type

[**Image**](Image.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image**
> delete_image(image_id)

Delete specified image

Deletes the specified image.

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
api_instance = layint_runtime_api.ImageApi()
image_id = 'image_id_example' # str | hexadecimal ID of image to delete

try: 
    # Delete specified image
    api_instance.delete_image(image_id)
except ApiException as e:
    print("Exception when calling ImageApi->delete_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| hexadecimal ID of image to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> Image get_image(image_id)

Get specified container image

Returns details about specified image.

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
api_instance = layint_runtime_api.ImageApi()
image_id = 'image_id_example' # str | hexadecimal ID of image to get

try: 
    # Get specified container image
    api_response = api_instance.get_image(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| hexadecimal ID of image to get | 

### Return type

[**Image**](Image.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> Images get_images()

Get defined container images

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
api_instance = layint_runtime_api.ImageApi()

try: 
    # Get defined container images
    api_response = api_instance.get_images()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_images: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Images**](Images.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instrument_image**
> instrument_image(image_id)

Request instrumentation of specified container image

Lists containers that are running specified image.

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
api_instance = layint_runtime_api.ImageApi()
image_id = 'image_id_example' # str | hexadecimal ID of image to instrument

try: 
    # Request instrumentation of specified container image
    api_instance.instrument_image(image_id)
except ApiException as e:
    print("Exception when calling ImageApi->instrument_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| hexadecimal ID of image to instrument | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **number_of_instrumented_images**
> InlineResponse200 number_of_instrumented_images()

Returns number of instrumented images

Returns number of instrumented images belonging to a user's group

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
api_instance = layint_runtime_api.ImageApi()

try: 
    # Returns number of instrumented images
    api_response = api_instance.number_of_instrumented_images()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->number_of_instrumented_images: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_container_running_image**
> Container show_container_running_image(image_id)

Get specified container image

Lists containers that are running specified image.

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
api_instance = layint_runtime_api.ImageApi()
image_id = 'image_id_example' # str | hexadecimal ID of image to get containers for

try: 
    # Get specified container image
    api_response = api_instance.show_container_running_image(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->show_container_running_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| hexadecimal ID of image to get containers for | 

### Return type

[**Container**](Container.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_image**
> Image update_image(image_id, image=image)

Update image definition

Updates an existing image object.

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
api_instance = layint_runtime_api.ImageApi()
image_id = 'image_id_example' # str | hexadecimal ID of image to get
image = layint_runtime_api.Image() # Image |  (optional)

try: 
    # Update image definition
    api_response = api_instance.update_image(image_id, image=image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->update_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| hexadecimal ID of image to get | 
 **image** | [**Image**](Image.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

