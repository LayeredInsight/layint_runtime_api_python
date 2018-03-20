# Image

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 12 character internal hexadecimal identifier for this image | [optional] 
**name** | **str** | Image name | [optional] 
**description** | **str** | Description for this image | [optional] 
**user_id** | **str** | User ID of owner of the image | [optional] 
**group_id** | **str** | Group ID of owner of the image | [optional] 
**image_id** | **str** | Docker image ID | [optional] 
**sha_sum** | **str** | SHA256 hash value for this image | [optional] 
**size** | **int** | Size of the image, in bytes | [optional] 
**registry** | **str** | 12 character hexadecimal internal identifier to layered insight record defining the registry this image is stored in | [optional] 
**config_id** | **str** | 12 character hexadecimal internal identifier for Runtime configuration for this Container | [optional] 
**policy_id** | **str** | 12 character hexadecimal internal identifier for security policy for this Container | [optional] 
**status** | **int** | Value representing the current status of working with the image: 0: Added to system, but not yet analyzed 1: Processing - preparing for download 2: Downloading for analysis and instrumentation 3: There was an error during download, analysis, or instrumentation of the image 4: Instrumented image; Needs to be run to gather behavioral data 5: Instrumented and ready for use | [optional] 
**status_msg** | **str** | Stores details about status of image, if any | [optional] 
**date_created** | **str** | Timestamp for when object was created | [optional] 
**date_updated** | **str** | Timestamp for when object was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


