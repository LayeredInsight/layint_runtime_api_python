# Policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 12 character internal hexadecimal identifier for this policy | [optional] 
**name** | **str** | Name to refer to policy with and display | [optional] 
**description** | **str** | Free-form description of this policy | [optional] 
**user_id** | **str** | User ID of owner of the policy | [optional] 
**group_id** | **str** | Group ID of owner of the policy | [optional] 
**schema_version** | **str** | Schema version for this policy | [optional] 
**default_file_action** | **str** | Default action for file rules if no rule matches. This allows blacklisting or whitelisting. | [optional] 
**default_network_action** | **str** | Default action for network rules if no rule matches. This allows blacklisting or whitelisting. | [optional] 
**default_program_action** | **str** | Default action for program rules if no rule matches. This allows blacklisting or whitelisting. | [optional] 
**suspend** | **bool** | Allows suspension of policy enforcement | [optional] [default to False]
**limits** | [**Limit**](Limit.md) |  | [optional] 
**rules** | [**list[PolicyRule]**](PolicyRule.md) | Policy rules defining control for this policy | [optional] 
**date_created** | **str** | Timestamp for when object was created | [optional] 
**date_updated** | **str** | Timestamp for when object was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


