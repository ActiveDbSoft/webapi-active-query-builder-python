# webapi_active_query_builder.ActiveQueryBuilderApi

All URIs are relative to *https://webapi.activequerybuilder.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_query_columns_post**](ActiveQueryBuilderApi.md#get_query_columns_post) | **POST** /getQueryColumns | 
[**transform_sql_post**](ActiveQueryBuilderApi.md#transform_sql_post) | **POST** /transformSQL | 


# **get_query_columns_post**
> list[QueryColumn] get_query_columns_post(query)



Returns list of columns for the given SQL query.

### Example 
```python
import time
import webapi_active_query_builder
from webapi_active_query_builder.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = webapi_active_query_builder.ActiveQueryBuilderApi()
query = webapi_active_query_builder.SqlQuery() # SqlQuery | Information about SQL query and it's context.

try: 
    api_response = api_instance.get_query_columns_post(query)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ActiveQueryBuilderApi->get_query_columns_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**SqlQuery**](SqlQuery.md)| Information about SQL query and it&#39;s context. | 

### Return type

[**list[QueryColumn]**](QueryColumn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transform_sql_post**
> TransformResult transform_sql_post(transform)



Transforms the given SQL query according to the commands provided in this request. You can add constraints, hide some of the resultset columns, chang sorting or limit rows of resultset. All transformations can only lead to reorganization or limitation of the resultset data. This means that it's impossible to get transformed SQL that reveals any other data than the data retutned by original query.

### Example 
```python
import time
import webapi_active_query_builder
from webapi_active_query_builder.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = webapi_active_query_builder.ActiveQueryBuilderApi()
transform = webapi_active_query_builder.Transform() # Transform | SQL transformation parameters and commands.

try: 
    api_response = api_instance.transform_sql_post(transform)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ActiveQueryBuilderApi->transform_sql_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transform** | [**Transform**](Transform.md)| SQL transformation parameters and commands. | 

### Return type

[**TransformResult**](TransformResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

