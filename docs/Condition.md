# Condition

Defines a constraint for original query resultset values.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Column of original query to which a constraint will applied. | [optional] 
**condition_operator** | **str** | Condition operator. | [optional] 
**values** | **list[str]** | List of values for a constraint. 'IsNull', 'IsNotNull' need no values; 'Between', 'NotBetween' require 2 values; 'In' accepts one or more values; other conditions accept single value only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


