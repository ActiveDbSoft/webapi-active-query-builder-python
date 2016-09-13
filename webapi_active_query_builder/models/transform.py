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


class Transform(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, guid=None, sql=None, pagination=None, totals=None, sortings=None, filter=None, hidden_columns=None):
        """
        Transform - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'guid': 'str',
            'sql': 'str',
            'pagination': 'Pagination',
            'totals': 'list[Totals]',
            'sortings': 'list[Sorting]',
            'filter': 'ConditionGroup',
            'hidden_columns': 'list[HiddenColumn]'
        }

        self.attribute_map = {
            'guid': 'Guid',
            'sql': 'Sql',
            'pagination': 'Pagination',
            'totals': 'Totals',
            'sortings': 'Sortings',
            'filter': 'Filter',
            'hidden_columns': 'HiddenColumns'
        }

        self._guid = guid
        self._sql = sql
        self._pagination = pagination
        self._totals = totals
        self._sortings = sortings
        self._filter = filter
        self._hidden_columns = hidden_columns

    @property
    def guid(self):
        """
        Gets the guid of this Transform.
        Unique identifier that defines SQL execution context for the given query, i.e. database server (SQL syntax rules),  database schema. The context itself must be saved in the user account on https://webapi.activequerybuilder.com/.

        :return: The guid of this Transform.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this Transform.
        Unique identifier that defines SQL execution context for the given query, i.e. database server (SQL syntax rules),  database schema. The context itself must be saved in the user account on https://webapi.activequerybuilder.com/.

        :param guid: The guid of this Transform.
        :type: str
        """

        self._guid = guid

    @property
    def sql(self):
        """
        Gets the sql of this Transform.
        Text of original SQL query to be transformed.

        :return: The sql of this Transform.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """
        Sets the sql of this Transform.
        Text of original SQL query to be transformed.

        :param sql: The sql of this Transform.
        :type: str
        """

        self._sql = sql

    @property
    def pagination(self):
        """
        Gets the pagination of this Transform.


        :return: The pagination of this Transform.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """
        Sets the pagination of this Transform.


        :param pagination: The pagination of this Transform.
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def totals(self):
        """
        Gets the totals of this Transform.


        :return: The totals of this Transform.
        :rtype: list[Totals]
        """
        return self._totals

    @totals.setter
    def totals(self, totals):
        """
        Sets the totals of this Transform.


        :param totals: The totals of this Transform.
        :type: list[Totals]
        """

        self._totals = totals

    @property
    def sortings(self):
        """
        Gets the sortings of this Transform.


        :return: The sortings of this Transform.
        :rtype: list[Sorting]
        """
        return self._sortings

    @sortings.setter
    def sortings(self, sortings):
        """
        Sets the sortings of this Transform.


        :param sortings: The sortings of this Transform.
        :type: list[Sorting]
        """

        self._sortings = sortings

    @property
    def filter(self):
        """
        Gets the filter of this Transform.


        :return: The filter of this Transform.
        :rtype: ConditionGroup
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this Transform.


        :param filter: The filter of this Transform.
        :type: ConditionGroup
        """

        self._filter = filter

    @property
    def hidden_columns(self):
        """
        Gets the hidden_columns of this Transform.


        :return: The hidden_columns of this Transform.
        :rtype: list[HiddenColumn]
        """
        return self._hidden_columns

    @hidden_columns.setter
    def hidden_columns(self, hidden_columns):
        """
        Sets the hidden_columns of this Transform.


        :param hidden_columns: The hidden_columns of this Transform.
        :type: list[HiddenColumn]
        """

        self._hidden_columns = hidden_columns

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
