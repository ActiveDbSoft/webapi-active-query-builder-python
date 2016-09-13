# coding: utf-8

"""
    QueryBuilderApi

    Active Query Builder Web API lets create, analyze and modify SQL queries for different database servers using RESTful HTTP requests to a cloud-based service. It requires SQL execution context (information about database schema and used database server) to be stored under the registered account at https://webapi.activequerybuilder.com/.

    OpenAPI spec version: 1.1.6
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

from pprint import pformat
from six import iteritems
import re


class Pagination(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, skip=None, take=None):
        """
        Pagination - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'skip': 'int',
            'take': 'int'
        }

        self.attribute_map = {
            'skip': 'skip',
            'take': 'take'
        }

        self._skip = skip
        self._take = take

    @property
    def skip(self):
        """
        Gets the skip of this Pagination.
        Number of rows to skip from the top of original resultset.

        :return: The skip of this Pagination.
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """
        Sets the skip of this Pagination.
        Number of rows to skip from the top of original resultset.

        :param skip: The skip of this Pagination.
        :type: int
        """

        self._skip = skip

    @property
    def take(self):
        """
        Gets the take of this Pagination.
        Number of rows to get from orignal to new resultset.

        :return: The take of this Pagination.
        :rtype: int
        """
        return self._take

    @take.setter
    def take(self, take):
        """
        Sets the take of this Pagination.
        Number of rows to get from orignal to new resultset.

        :param take: The take of this Pagination.
        :type: int
        """

        self._take = take

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
