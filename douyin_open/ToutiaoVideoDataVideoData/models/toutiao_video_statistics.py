# coding: utf-8

"""

    通过头条视频id批量获取已分享视频数据信息  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ToutiaoVideoStatistics(object):
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
        'comment_count': 'int',
        'digg_count': 'int',
        'play_count': 'int',
        'share_count': 'int',
        'forward_count': 'int'
    }

    attribute_map = {
        'comment_count': 'comment_count',
        'digg_count': 'digg_count',
        'play_count': 'play_count',
        'share_count': 'share_count',
        'forward_count': 'forward_count'
    }

    def __init__(self, comment_count=None, digg_count=None, play_count=None, share_count=None, forward_count=None):  # noqa: E501
        """ToutiaoVideoStatistics - a model defined in Swagger"""  # noqa: E501
        self._comment_count = None
        self._digg_count = None
        self._play_count = None
        self._share_count = None
        self._forward_count = None
        self.discriminator = None
        self.comment_count = comment_count
        self.digg_count = digg_count
        self.play_count = play_count
        self.share_count = share_count
        self.forward_count = forward_count

    @property
    def comment_count(self):
        """Gets the comment_count of this ToutiaoVideoStatistics.  # noqa: E501

        评论数  # noqa: E501

        :return: The comment_count of this ToutiaoVideoStatistics.  # noqa: E501
        :rtype: int
        """
        return self._comment_count

    @comment_count.setter
    def comment_count(self, comment_count):
        """Sets the comment_count of this ToutiaoVideoStatistics.

        评论数  # noqa: E501

        :param comment_count: The comment_count of this ToutiaoVideoStatistics.  # noqa: E501
        :type: int
        """
        if comment_count is None:
            raise ValueError("Invalid value for `comment_count`, must not be `None`")  # noqa: E501

        self._comment_count = comment_count

    @property
    def digg_count(self):
        """Gets the digg_count of this ToutiaoVideoStatistics.  # noqa: E501

        点赞数  # noqa: E501

        :return: The digg_count of this ToutiaoVideoStatistics.  # noqa: E501
        :rtype: int
        """
        return self._digg_count

    @digg_count.setter
    def digg_count(self, digg_count):
        """Sets the digg_count of this ToutiaoVideoStatistics.

        点赞数  # noqa: E501

        :param digg_count: The digg_count of this ToutiaoVideoStatistics.  # noqa: E501
        :type: int
        """
        if digg_count is None:
            raise ValueError("Invalid value for `digg_count`, must not be `None`")  # noqa: E501

        self._digg_count = digg_count

    @property
    def play_count(self):
        """Gets the play_count of this ToutiaoVideoStatistics.  # noqa: E501

        播放数  # noqa: E501

        :return: The play_count of this ToutiaoVideoStatistics.  # noqa: E501
        :rtype: int
        """
        return self._play_count

    @play_count.setter
    def play_count(self, play_count):
        """Sets the play_count of this ToutiaoVideoStatistics.

        播放数  # noqa: E501

        :param play_count: The play_count of this ToutiaoVideoStatistics.  # noqa: E501
        :type: int
        """
        if play_count is None:
            raise ValueError("Invalid value for `play_count`, must not be `None`")  # noqa: E501

        self._play_count = play_count

    @property
    def share_count(self):
        """Gets the share_count of this ToutiaoVideoStatistics.  # noqa: E501

        分享数  # noqa: E501

        :return: The share_count of this ToutiaoVideoStatistics.  # noqa: E501
        :rtype: int
        """
        return self._share_count

    @share_count.setter
    def share_count(self, share_count):
        """Sets the share_count of this ToutiaoVideoStatistics.

        分享数  # noqa: E501

        :param share_count: The share_count of this ToutiaoVideoStatistics.  # noqa: E501
        :type: int
        """
        if share_count is None:
            raise ValueError("Invalid value for `share_count`, must not be `None`")  # noqa: E501

        self._share_count = share_count

    @property
    def forward_count(self):
        """Gets the forward_count of this ToutiaoVideoStatistics.  # noqa: E501

        转发数  # noqa: E501

        :return: The forward_count of this ToutiaoVideoStatistics.  # noqa: E501
        :rtype: int
        """
        return self._forward_count

    @forward_count.setter
    def forward_count(self, forward_count):
        """Sets the forward_count of this ToutiaoVideoStatistics.

        转发数  # noqa: E501

        :param forward_count: The forward_count of this ToutiaoVideoStatistics.  # noqa: E501
        :type: int
        """
        if forward_count is None:
            raise ValueError("Invalid value for `forward_count`, must not be `None`")  # noqa: E501

        self._forward_count = forward_count

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
        if issubclass(ToutiaoVideoStatistics, dict):
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
        if not isinstance(other, ToutiaoVideoStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
