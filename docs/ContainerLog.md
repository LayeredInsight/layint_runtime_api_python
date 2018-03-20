# ContainerLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 12 character internal hexadecimal identifier for this log | [optional] 
**message_type** | **int** | Number representing the type of log this is. 2 for \&quot;action\&quot; logs, 3 for \&quot;behavioral\&quot; logs | [optional] 
**process_id** | **int** | UNIX process id of the process that generated the log | [optional] 
**process_name** | **str** | Name of the process that generated the log | [optional] 
**system_call** | **int** | Number representing the system call that generated this log entry | [optional] 
**system_call_name** | **str** | String representation of the system call that generated this log entry | [optional] 
**action** | **int** | Number representing the action taken on the function call that generated this log. 0 for deny, 1 for allow. | [optional] 
**file_name** | **str** | Optional name of file that was being operated on in the function call that generated this log | [optional] 
**date_created** | **str** | Timestamp for when this log was created | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


