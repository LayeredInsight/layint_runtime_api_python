# Limit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_num_proc** | **int** | Maximum number of processes allowed to run in a container. If value is 0, no limit enforced. | [optional] 
**max_proc_life** | **int** | Maximum lifetime, in seconds, for a process in a container. If breached, an alert will be generated. If value is 0, no limit enforced. | [optional] 
**syscalls** | [**SyscallLimit**](SyscallLimit.md) |  | [optional] 
**processes** | [**ProcessLimit**](ProcessLimit.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


