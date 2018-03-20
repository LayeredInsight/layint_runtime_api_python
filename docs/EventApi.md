# layint_runtime_api.EventApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_event**](EventApi.md#describe_event) | **GET** /Events/{eventID} | Gets description about specific event


# **describe_event**
> AlertEvents describe_event(event_id)

Gets description about specific event

Describes an event in a manner that can be understood by humans.

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
api_instance = layint_runtime_api.EventApi()
event_id = 'event_id_example' # str | hexadecimal ID of event to get description of

try: 
    # Gets description about specific event
    api_response = api_instance.describe_event(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->describe_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| hexadecimal ID of event to get description of | 

### Return type

[**AlertEvents**](AlertEvents.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

