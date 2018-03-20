# PolicyRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name to refer to rule with and display | [optional] 
**in_active** | **bool** | Allows the enabling/disabling of this rule | [optional] [default to False]
**rule_type** | **str** | Specifies the type of rule this is | [optional] 
**program** | **str** | Specifies path to program that this rule applies to. Wildcards are allowed. | [optional] [default to '*']
**listening_port** | **int** | Local network port number this this rule applies to. Used only by network and listener rules. | [optional] 
**listening_addr** | **str** | Local IP address this rule applies to. Used only by network rules. | [optional] 
**protocol** | **str** | Network protocol that this rule applies to. Used only by network rules. | [optional] 
**remote_port** | **int** | Remote network port number this this rule applies to. Used only by network rules. | [optional] 
**syscall** | **int** | System call number, for rules where an individual system call is to be blocked. Used only in syscall rules. | [optional] 
**arg1** | **str** | Variable argument, usage differs depending on rule type. | [optional] 
**arg2** | **str** | Variable argument, usage differs depending on rule type. | [optional] 
**arg3** | **str** | Variable argument, usage differs depending on rule type. | [optional] 
**file** | **str** | Path to file that rule applies to | [optional] 
**action** | **str** | Action that should be taken if this rule is matched | [optional] 
**date_created** | **str** | Timestamp for when object was created | [optional] 
**date_updated** | **str** | Timestamp for when object was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


