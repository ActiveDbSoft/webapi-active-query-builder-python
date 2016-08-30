# coding: utf-8

"""
    QueryBuilderApi

    Active Query Builder Web API lets create, analyze and modify SQL queries for different database servers using RESTful HTTP requests to a cloud-based service. It requires SQL execution context (information about database schema and used database server) to be stored under the registered account at https://webapi.activequerybuilder.com/.

    OpenAPI spec version: 1.1.3
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


class Totals(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, field=None, aggregate=None):
        """
        Totals - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'field': 'str',
            'aggregate': 'str'
        }

        self.attribute_map = {
            'field': 'field',
            'aggregate': 'aggregate'
        }

        self._field = field
        self._aggregate = aggregate

    @property
    def field(self):
        """
        Gets the field of this Totals.
        Column of original query to which an aggregate function will be applied.

        :return: The field of this Totals.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this Totals.
        Column of original query to which an aggregate function will be applied.

        :param field: The field of this Totals.
        :type: str
        """

        self._field = field

    @property
    def aggregate(self):
        """
        Gets the aggregate of this Totals.
        Aggregate function name.

        :return: The aggregate of this Totals.
        :rtype: str
        """
        return self._aggregate

    @aggregate.setter
    def aggregate(self, aggregate):
        """
        Sets the aggregate of this Totals.
        Aggregate function name.

        :param aggregate: The aggregate of this Totals.
        :type: str
        """
        allowed_values = ["avg", "count", "max", "min", "sum"]
        if aggregate not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregate` ({0}), must be one of {1}"
                .format(aggregate, allowed_values)
            )

        self._aggregate = aggregate

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