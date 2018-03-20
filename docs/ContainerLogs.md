# ContainerLogs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Number describing what page of $PageSize logs is in this object | [optional] 
**page_size** | **int** | Number describing maximum number of logs are displayed per \&quot;page\&quot; | [optional] 
**prev_page** | **str** | URL to get previous page of logs from system | [optional] 
**next_page** | **str** | URL to get next page of logs from system | [optional] 
**uri** | **str** | Uri that this set of data came from | [optional] 
**total_log_count** | **int** | Total number of logs for this container in the system | [optional] 
**log_data** | [**list[ContainerLog]**](ContainerLog.md) | Array of logs for this \&quot;page\&quot; of results | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


