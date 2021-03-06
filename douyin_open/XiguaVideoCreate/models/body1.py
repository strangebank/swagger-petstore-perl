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
        'video_id': 'str',
        'text': 'str',
        'praise': 'bool',
        'claim_origin': 'bool',
        'abstract': 'str',
        'cover_tsp': 'int'
    }

    attribute_map = {
        'video_id': 'video_id',
        'text': 'text',
        'praise': 'praise',
        'claim_origin': 'claim_origin',
        'abstract': 'abstract',
        'cover_tsp': 'cover_tsp'
    }

    def __init__(self, video_id=None, text=None, praise=False, claim_origin=False, abstract='', cover_tsp=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501
        self._video_id = None
        self._text = None
        self._praise = None
        self._claim_origin = None
        self._abstract = None
        self._cover_tsp = None
        self.discriminator = None
        self.video_id = video_id
        self.text = text
        self.praise = praise
        self.claim_origin = claim_origin
        self.abstract = abstract
        if cover_tsp is not None:
            self.cover_tsp = cover_tsp

    @property
    def video_id(self):
        """Gets the video_id of this Body1.  # noqa: E501

        video_id, 通过/xigua/video/upload/接口得到  # noqa: E501

        :return: The video_id of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this Body1.

        video_id, 通过/xigua/video/upload/接口得到  # noqa: E501

        :param video_id: The video_id of this Body1.  # noqa: E501
        :type: str
        """
        if video_id is None:
            raise ValueError("Invalid value for `video_id`, must not be `None`")  # noqa: E501

        self._video_id = video_id

    @property
    def text(self):
        """Gets the text of this Body1.  # noqa: E501

        标题长度应该在5-30字之间  # noqa: E501

        :return: The text of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Body1.

        标题长度应该在5-30字之间  # noqa: E501

        :param text: The text of this Body1.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def praise(self):
        """Gets the praise of this Body1.  # noqa: E501

        是否给视频开通可以赞赏的入口  # noqa: E501

        :return: The praise of this Body1.  # noqa: E501
        :rtype: bool
        """
        return self._praise

    @praise.setter
    def praise(self, praise):
        """Sets the praise of this Body1.

        是否给视频开通可以赞赏的入口  # noqa: E501

        :param praise: The praise of this Body1.  # noqa: E501
        :type: bool
        """
        if praise is None:
            raise ValueError("Invalid value for `praise`, must not be `None`")  # noqa: E501

        self._praise = praise

    @property
    def claim_origin(self):
        """Gets the claim_origin of this Body1.  # noqa: E501

        是否声明原创  # noqa: E501

        :return: The claim_origin of this Body1.  # noqa: E501
        :rtype: bool
        """
        return self._claim_origin

    @claim_origin.setter
    def claim_origin(self, claim_origin):
        """Sets the claim_origin of this Body1.

        是否声明原创  # noqa: E501

        :param claim_origin: The claim_origin of this Body1.  # noqa: E501
        :type: bool
        """
        if claim_origin is None:
            raise ValueError("Invalid value for `claim_origin`, must not be `None`")  # noqa: E501

        self._claim_origin = claim_origin

    @property
    def abstract(self):
        """Gets the abstract of this Body1.  # noqa: E501

        视频简介，400字以内  # noqa: E501

        :return: The abstract of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._abstract

    @abstract.setter
    def abstract(self, abstract):
        """Sets the abstract of this Body1.

        视频简介，400字以内  # noqa: E501

        :param abstract: The abstract of this Body1.  # noqa: E501
        :type: str
        """
        if abstract is None:
            raise ValueError("Invalid value for `abstract`, must not be `None`")  # noqa: E501

        self._abstract = abstract

    @property
    def cover_tsp(self):
        """Gets the cover_tsp of this Body1.  # noqa: E501

        从视频中截取封面的时间，用该帧作为封面（单位为毫秒）  # noqa: E501

        :return: The cover_tsp of this Body1.  # noqa: E501
        :rtype: int
        """
        return self._cover_tsp

    @cover_tsp.setter
    def cover_tsp(self, cover_tsp):
        """Sets the cover_tsp of this Body1.

        从视频中截取封面的时间，用该帧作为封面（单位为毫秒）  # noqa: E501

        :param cover_tsp: The cover_tsp of this Body1.  # noqa: E501
        :type: int
        """

        self._cover_tsp = cover_tsp

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
