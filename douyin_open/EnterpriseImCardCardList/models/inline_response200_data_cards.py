# coding: utf-8

"""
    消息卡片列表

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse200DataCards(object):
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
        'card_id': 'str',
        'card_type': 'str',
        'content': 'str',
        'status': 'str',
        'reject_reason': 'str'
    }

    attribute_map = {
        'card_id': 'card_id',
        'card_type': 'card_type',
        'content': 'content',
        'status': 'status',
        'reject_reason': 'reject_reason'
    }

    def __init__(self, card_id=None, card_type=None, content=None, status=None, reject_reason=None):  # noqa: E501
        """InlineResponse200DataCards - a model defined in Swagger"""  # noqa: E501
        self._card_id = None
        self._card_type = None
        self._content = None
        self._status = None
        self._reject_reason = None
        self.discriminator = None
        self.card_id = card_id
        self.card_type = card_type
        self.content = content
        self.status = status
        if reject_reason is not None:
            self.reject_reason = reject_reason

    @property
    def card_id(self):
        """Gets the card_id of this InlineResponse200DataCards.  # noqa: E501

        卡片id  # noqa: E501

        :return: The card_id of this InlineResponse200DataCards.  # noqa: E501
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this InlineResponse200DataCards.

        卡片id  # noqa: E501

        :param card_id: The card_id of this InlineResponse200DataCards.  # noqa: E501
        :type: str
        """
        if card_id is None:
            raise ValueError("Invalid value for `card_id`, must not be `None`")  # noqa: E501

        self._card_id = card_id

    @property
    def card_type(self):
        """Gets the card_type of this InlineResponse200DataCards.  # noqa: E501

        卡片类型  # noqa: E501

        :return: The card_type of this InlineResponse200DataCards.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this InlineResponse200DataCards.

        卡片类型  # noqa: E501

        :param card_type: The card_type of this InlineResponse200DataCards.  # noqa: E501
        :type: str
        """
        if card_type is None:
            raise ValueError("Invalid value for `card_type`, must not be `None`")  # noqa: E501

        self._card_type = card_type

    @property
    def content(self):
        """Gets the content of this InlineResponse200DataCards.  # noqa: E501

        卡片内容  # noqa: E501

        :return: The content of this InlineResponse200DataCards.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this InlineResponse200DataCards.

        卡片内容  # noqa: E501

        :param content: The content of this InlineResponse200DataCards.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def status(self):
        """Gets the status of this InlineResponse200DataCards.  # noqa: E501

        审核状态（avaliable可使用,review审核中,reject审核不通过)  # noqa: E501

        :return: The status of this InlineResponse200DataCards.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200DataCards.

        审核状态（avaliable可使用,review审核中,reject审核不通过)  # noqa: E501

        :param status: The status of this InlineResponse200DataCards.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["avaliable", "review", "reject", ""]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def reject_reason(self):
        """Gets the reject_reason of this InlineResponse200DataCards.  # noqa: E501

        审核不通过理由  # noqa: E501

        :return: The reject_reason of this InlineResponse200DataCards.  # noqa: E501
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this InlineResponse200DataCards.

        审核不通过理由  # noqa: E501

        :param reject_reason: The reject_reason of this InlineResponse200DataCards.  # noqa: E501
        :type: str
        """

        self._reject_reason = reject_reason

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
        if issubclass(InlineResponse200DataCards, dict):
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
        if not isinstance(other, InlineResponse200DataCards):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
