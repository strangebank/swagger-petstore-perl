# coding: utf-8

"""
    查询指定动态消息卡片

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CardModuleImage(object):
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
        'media_id': 'str',
        'url': 'str'
    }

    attribute_map = {
        'media_id': 'media_id',
        'url': 'url'
    }

    def __init__(self, media_id=None, url=None):  # noqa: E501
        """CardModuleImage - a model defined in Swagger"""  # noqa: E501
        self._media_id = None
        self._url = None
        self.discriminator = None
        if media_id is not None:
            self.media_id = media_id
        if url is not None:
            self.url = url

    @property
    def media_id(self):
        """Gets the media_id of this CardModuleImage.  # noqa: E501

        素材库id，保存卡片时需传  # noqa: E501

        :return: The media_id of this CardModuleImage.  # noqa: E501
        :rtype: str
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        """Sets the media_id of this CardModuleImage.

        素材库id，保存卡片时需传  # noqa: E501

        :param media_id: The media_id of this CardModuleImage.  # noqa: E501
        :type: str
        """

        self._media_id = media_id

    @property
    def url(self):
        """Gets the url of this CardModuleImage.  # noqa: E501

        图片url  # noqa: E501

        :return: The url of this CardModuleImage.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CardModuleImage.

        图片url  # noqa: E501

        :param url: The url of this CardModuleImage.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(CardModuleImage, dict):
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
        if not isinstance(other, CardModuleImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
