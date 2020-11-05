# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Body1(object):
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
        'extra': 'ExtraBody',
        'video_id': 'str',
        'text': 'str'
    }

    attribute_map = {
        'extra': 'extra',
        'video_id': 'video_id',
        'text': 'text'
    }

    def __init__(self, extra=None, video_id=None, text=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501
        self._extra = None
        self._video_id = None
        self._text = None
        self.discriminator = None
        if extra is not None:
            self.extra = extra
        self.video_id = video_id
        if text is not None:
            self.text = text

    @property
    def extra(self):
        """Gets the extra of this Body1.  # noqa: E501


        :return: The extra of this Body1.  # noqa: E501
        :rtype: ExtraBody
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this Body1.


        :param extra: The extra of this Body1.  # noqa: E501
        :type: ExtraBody
        """

        self._extra = extra

    @property
    def video_id(self):
        """Gets the video_id of this Body1.  # noqa: E501

        video_id, 通过/toutiao/video/upload/接口得到  # noqa: E501

        :return: The video_id of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this Body1.

        video_id, 通过/toutiao/video/upload/接口得到  # noqa: E501

        :param video_id: The video_id of this Body1.  # noqa: E501
        :type: str
        """
        if video_id is None:
            raise ValueError("Invalid value for `video_id`, must not be `None`")  # noqa: E501

        self._video_id = video_id

    @property
    def text(self):
        """Gets the text of this Body1.  # noqa: E501

        视频标题不要超过30个字符  # noqa: E501

        :return: The text of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Body1.

        视频标题不要超过30个字符  # noqa: E501

        :param text: The text of this Body1.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(Body1, dict):
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
        if not isinstance(other, Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other