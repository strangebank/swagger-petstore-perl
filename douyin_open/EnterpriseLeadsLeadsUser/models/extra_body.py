# coding: utf-8

"""
    企业号意向用户管理

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ExtraBody(object):
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
        'logid': 'str',
        'now': 'int'
    }

    attribute_map = {
        'logid': 'logid',
        'now': 'now'
    }

    def __init__(self, logid=None, now=None):  # noqa: E501
        """ExtraBody - a model defined in Swagger"""  # noqa: E501
        self._logid = None
        self._now = None
        self.discriminator = None
        if logid is not None:
            self.logid = logid
        if now is not None:
            self.now = now

    @property
    def logid(self):
        """Gets the logid of this ExtraBody.  # noqa: E501

        标识请求的唯一id  # noqa: E501

        :return: The logid of this ExtraBody.  # noqa: E501
        :rtype: str
        """
        return self._logid

    @logid.setter
    def logid(self, logid):
        """Sets the logid of this ExtraBody.

        标识请求的唯一id  # noqa: E501

        :param logid: The logid of this ExtraBody.  # noqa: E501
        :type: str
        """

        self._logid = logid

    @property
    def now(self):
        """Gets the now of this ExtraBody.  # noqa: E501

        毫秒级时间戳  # noqa: E501

        :return: The now of this ExtraBody.  # noqa: E501
        :rtype: int
        """
        return self._now

    @now.setter
    def now(self, now):
        """Sets the now of this ExtraBody.

        毫秒级时间戳  # noqa: E501

        :param now: The now of this ExtraBody.  # noqa: E501
        :type: int
        """

        self._now = now

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
        if issubclass(ExtraBody, dict):
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
        if not isinstance(other, ExtraBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
