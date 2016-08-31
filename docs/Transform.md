# Transform

SQL transformation parameters and commands.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Unique identifier that defines SQL execution context for the given query, i.e. database server (SQL syntax rules),  database schema. The context itself must be saved in the user account on https://webapi.activequerybuilder.com/. | [optional] 
**sql** | **str** | Text of original SQL query to be transformed. | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**totals** | [**list[Totals]**](Totals.md) |  | [optional] 
**sortings** | [**list[Sorting]**](Sorting.md) |  | [optional] 
**filter** | [**ConditionGroup**](ConditionGroup.md) |  | [optional] 
**hidden_columns** | [**list[HiddenColumn]**](HiddenColumn.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


