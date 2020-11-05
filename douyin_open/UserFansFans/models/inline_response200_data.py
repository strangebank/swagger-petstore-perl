# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse200Data(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error_code': 'ErrorCode',
        'description': 'Description',
        'cursor': 'Cursor',
        'has_more': 'HasMore',
        'list': 'list[User]',
        'total': 'int'
    }

    attribute_map = {
        'error_code': 'error_code',
        'description': 'description',
        'cursor': 'cursor',
        'has_more': 'has_more',
        'list': 'list',
        'total': 'total'
    }

    def __init__(self, error_code=None, description=None, cursor=None, has_more=None, list=None, total=None):  # noqa: E501
        """InlineResponse200Data - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._description = None
        self._cursor = None
        self._has_more = None
        self._list = None
        self._total = None
        self.discriminator = None
        if error_code is not None:
            self.error_code = error_code
        if description is not None:
            self.description = description
        if cursor is not None:
            self.cursor = cursor
        if has_more is not None:
            self.has_more = has_more
        if list is not None:
            self.list = list
        if total is not None:
            self.total = total

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse200Data.  # noqa: E501


        :return: The error_code of this InlineResponse200Data.  # noqa: E501
        :rtype: ErrorCode
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse200Data.


        :param error_code: The error_code of this InlineResponse200Data.  # noqa: E501
        :type: ErrorCode
        """

        self._error_code = error_code

    @property
    def description(self):
        """Gets the description of this InlineResponse200Data.  # noqa: E501


        :return: The description of this InlineResponse200Data.  # noqa: E501
        :rtype: Description
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse200Data.


        :param description: The description of this InlineResponse200Data.  # noqa: E501
        :type: Description
        """

        self._description = description

    @property
    def cursor(self):
        """Gets the cursor of this InlineResponse200Data.  # noqa: E501


        :return: The cursor of this InlineResponse200Data.  # noqa: E501
        :rtype: Cursor
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this InlineResponse200Data.


        :param cursor: The cursor of this InlineResponse200Data.  # noqa: E501
        :type: Cursor
        """

        self._cursor = cursor

    @property
    def has_more(self):
        """Gets the has_more of this InlineResponse200Data.  # noqa: E501


        :return: The has_more of this InlineResponse200Data.  # noqa: E501
        :rtype: HasMore
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this InlineResponse200Data.


        :param has_more: The has_more of this InlineResponse200Data.  # noqa: E501
        :type: HasMore
        """

        self._has_more = has_more

    @property
    def list(self):
        """Gets the list of this InlineResponse200Data.  # noqa: E501


        :return: The list of this InlineResponse200Data.  # noqa: E501
        :rtype: list[User]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this InlineResponse200Data.


        :param list: The list of this InlineResponse200Data.  # noqa: E501
        :type: list[User]
        """

        self._list = list

    @property
    def total(self):
        """Gets the total of this InlineResponse200Data.  # noqa: E501

        粉丝总数  # noqa: E501

        :return: The total of this InlineResponse200Data.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse200Data.

        粉丝总数  # noqa: E501

        :param total: The total of this InlineResponse200Data.  # noqa: E501
        :type: int
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse200Data, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other