# coding: utf-8

"""
    券码核销

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Body(object):
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
        'groupon_id': 'str',
        'code': 'str'
    }

    attribute_map = {
        'groupon_id': 'groupon_id',
        'code': 'code'
    }

    def __init__(self, groupon_id=None, code=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501
        self._groupon_id = None
        self._code = None
        self.discriminator = None
        self.groupon_id = groupon_id
        self.code = code

    @property
    def groupon_id(self):
        """Gets the groupon_id of this Body.  # noqa: E501

        团购活动的Id  # noqa: E501

        :return: The groupon_id of this Body.  # noqa: E501
        :rtype: str
        """
        return self._groupon_id

    @groupon_id.setter
    def groupon_id(self, groupon_id):
        """Sets the groupon_id of this Body.

        团购活动的Id  # noqa: E501

        :param groupon_id: The groupon_id of this Body.  # noqa: E501
        :type: str
        """
        if groupon_id is None:
            raise ValueError("Invalid value for `groupon_id`, must not be `None`")  # noqa: E501

        self._groupon_id = groupon_id

    @property
    def code(self):
        """Gets the code of this Body.  # noqa: E501

        券码的列表  # noqa: E501

        :return: The code of this Body.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Body.

        券码的列表  # noqa: E501

        :param code: The code of this Body.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

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
        if issubclass(Body, dict):
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
        if not isinstance(other, Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
