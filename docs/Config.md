# Config

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 12 character internal hexadecimal identifier for this Configuration | [optional] 
**name** | **str** | Name of the configuration | [optional] 
**user_id** | **int** | User ID of owner of the container | [optional] 
**group_id** | **int** | Group ID of owner of the container | [optional] 
**mq** | **str** | Connection string for RabbitMQ system the instrumented container should connect to. Both AMQP and AMQPS are supported. | [optional] 
**policy_id** | **str** | 12 character hexadecimal internal identifier for security policy for this Container | [optional] 
**logging** | **bool** | When true, specifies that behavioral logging should be sent to servers. | [optional] [default to False]
**sniffing** | **bool** | When true, enables basic network monitoring for malicious activity and network behavior recording. | [optional] [default to False]
**date_created** | **str** | Timestamp for when object was created | [optional] 
**date_updated** | **str** | Timestamp for when object was last updated | [optional] 
**default** | **bool** | Default configuration for group | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


