# coding: utf-8

"""
    QueryBuilderApi

    Active Query Builder Web API lets create, analyze and modify SQL queries for different database servers using RESTful HTTP requests to a cloud-based service. It requires SQL execution context (information about database schema and used database server) to be stored under the registered account at https://webapi.activequerybuilder.com/.

    OpenAPI spec version: 1.1.8
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


class ConditionGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, junction_type=None, conditions=None, condition_groups=None):
        """
        ConditionGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'junction_type': 'str',
            'conditions': 'list[Condition]',
            'condition_groups': 'list[ConditionGroup]'
        }

        self.attribute_map = {
            'junction_type': 'junctionType',
            'conditions': 'conditions',
            'condition_groups': 'conditionGroups'
        }

        self._junction_type = junction_type
        self._conditions = conditions
        self._condition_groups = condition_groups

    @property
    def junction_type(self):
        """
        Gets the junction_type of this ConditionGroup.
        Type of junction. All = AND; Any = OR.

        :return: The junction_type of this ConditionGroup.
        :rtype: str
        """
        return self._junction_type

    @junction_type.setter
    def junction_type(self, junction_type):
        """
        Sets the junction_type of this ConditionGroup.
        Type of junction. All = AND; Any = OR.

        :param junction_type: The junction_type of this ConditionGroup.
        :type: str
        """
        allowed_values = ["And", "Or", "Any", "All"]
        if junction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `junction_type` ({0}), must be one of {1}"
                .format(junction_type, allowed_values)
            )

        self._junction_type = junction_type

    @property
    def conditions(self):
        """
        Gets the conditions of this ConditionGroup.
        List of conditions to join.

        :return: The conditions of this ConditionGroup.
        :rtype: list[Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this ConditionGroup.
        List of conditions to join.

        :param conditions: The conditions of this ConditionGroup.
        :type: list[Condition]
        """

        self._conditions = conditions

    @property
    def condition_groups(self):
        """
        Gets the condition_groups of this ConditionGroup.
        List of nested condition groups to join them with a different boolean operator.

        :return: The condition_groups of this ConditionGroup.
        :rtype: list[ConditionGroup]
        """
        return self._condition_groups

    @condition_groups.setter
    def condition_groups(self, condition_groups):
        """
        Sets the condition_groups of this ConditionGroup.
        List of nested condition groups to join them with a different boolean operator.

        :param condition_groups: The condition_groups of this ConditionGroup.
        :type: list[ConditionGroup]
        """

        self._condition_groups = condition_groups

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
