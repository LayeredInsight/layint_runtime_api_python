# Container

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 12 character internal hexadecimal identifier for this Container | [optional] 
**name** | **str** | Containers name, or empty string | [optional] 
**user_id** | **int** | User ID of owner of the container | [optional] 
**group_id** | **int** | Group ID of owner of the container | [optional] 
**date_created** | **str** | Timestamp for when object was created | [optional] 
**date_updated** | **str** | Timestamp for when object was last updated | [optional] 
**image_id** | **str** | 12 character hexadecimal internal identifier for container image this container is running | [optional] 
**config_id** | **str** | 12 character hexadecimal internal identifier for Runtime configuration for this Container | [optional] 
**status** | **str** | Current status of the container. | [optional] 
**location** | **str** | Displays user defined &#39;location&#39; of this container. | [optional] 
**application** | **str** | Displays user defined &#39;Application&#39; for this container | [optional] 
**passive** | **bool** | Instructs Runtime to bypass any protection in this container when this field is set to true | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


