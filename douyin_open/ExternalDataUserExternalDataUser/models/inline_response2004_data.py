# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse2004Data(object):
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
        'result_list': 'list[ExternalUserShare]'
    }

    attribute_map = {
        'error_code': 'error_code',
        'description': 'description',
        'result_list': 'result_list'
    }

    def __init__(self, error_code=None, description=None, result_list=None):  # noqa: E501
        """InlineResponse2004Data - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._description = None
        self._result_list = None
        self.discriminator = None
        self.error_code = error_code
        self.description = description
        if result_list is not None:
            self.result_list = result_list

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse2004Data.  # noqa: E501


        :return: The error_code of this InlineResponse2004Data.  # noqa: E501
        :rtype: ErrorCode
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse2004Data.


        :param error_code: The error_code of this InlineResponse2004Data.  # noqa: E501
        :type: ErrorCode
        """
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def description(self):
        """Gets the description of this InlineResponse2004Data.  # noqa: E501


        :return: The description of this InlineResponse2004Data.  # noqa: E501
        :rtype: Description
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse2004Data.


        :param description: The description of this InlineResponse2004Data.  # noqa: E501
        :type: Description
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def result_list(self):
        """Gets the result_list of this InlineResponse2004Data.  # noqa: E501


        :return: The result_list of this InlineResponse2004Data.  # noqa: E501
        :rtype: list[ExternalUserShare]
        """
        return self._result_list

    @result_list.setter
    def result_list(self, result_list):
        """Sets the result_list of this InlineResponse2004Data.


        :param result_list: The result_list of this InlineResponse2004Data.  # noqa: E501
        :type: list[ExternalUserShare]
        """

        self._result_list = result_list

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
        if issubclass(InlineResponse2004Data, dict):
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
        if not isinstance(other, InlineResponse2004Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
