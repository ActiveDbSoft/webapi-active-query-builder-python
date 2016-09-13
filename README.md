# webapi_active_query_builder
Active Query Builder Web API lets create, analyze and modify SQL queries for different database servers using RESTful HTTP requests to a cloud-based service. It requires SQL execution context (information about database schema and used database server) to be stored under the registered account at https://webapi.activequerybuilder.com/.

## Requirements.

Python 2.7 and 3.4+

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import webapi_active_query_builder
from webapi_active_query_builder.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = webapi_active_query_builder.ActiveQueryBuilderApi
query = webapi_active_query_builder.SqlQuery() # SqlQuery | Information about SQL query and it's context.

try:
    api_response = api_instance.get_query_columns_post(query)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ActiveQueryBuilderApi->get_query_columns_post: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://webapi.activequerybuilder.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActiveQueryBuilderApi* | [**get_query_columns_post**](docs/ActiveQueryBuilderApi.md#get_query_columns_post) | **POST** /getQueryColumns | 
*ActiveQueryBuilderApi* | [**transform_sql_post**](docs/ActiveQueryBuilderApi.md#transform_sql_post) | **POST** /transformSQL | 


## Documentation For Models

 - [Condition](docs/Condition.md)
 - [ConditionGroup](docs/ConditionGroup.md)
 - [HiddenColumn](docs/HiddenColumn.md)
 - [Pagination](docs/Pagination.md)
 - [QueryColumn](docs/QueryColumn.md)
 - [Sorting](docs/Sorting.md)
 - [SqlQuery](docs/SqlQuery.md)
 - [Totals](docs/Totals.md)
 - [Transform](docs/Transform.md)
 - [TransformResult](docs/TransformResult.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

support@activedbsoft.com


## Source code
Full source code of all clients for Active Query Builder Web API is available on GitHub. Get the source code of javascript here: [https://github.com/ActiveDbSoft/webapi-active-query-builder-python](https://github.com/ActiveDbSoft/webapi-active-query-builder-python)
