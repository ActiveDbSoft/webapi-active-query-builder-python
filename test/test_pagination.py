# coding: utf-8

"""
    QueryBuilderApi

    Active Query Builder Web API lets create, analyze and modify SQL queries for different database servers using RESTful HTTP requests to a cloud-based service. It requires SQL execution context (information about database schema and used database server) to be stored under the registered account at https://webapi.activequerybuilder.com/.

    OpenAPI spec version: 1.0.0
    Contact: support@activedbsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import webapi_active_query_builder
from webapi_active_query_builder.rest import ApiException
from webapi_active_query_builder.models.pagination import Pagination


class TestPagination(unittest.TestCase):
    """ Pagination unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPagination(self):
        """
        Test Pagination
        """
        model = webapi_active_query_builder.models.pagination.Pagination()


if __name__ == '__main__':
    unittest.main()
