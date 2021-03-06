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


class CardModule(object):
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
        'module_type': 'str',
        'text': 'str',
        'image': 'CardModuleImage',
        'action': 'ModuleAction',
        'modules': 'list[CardSubModule]',
        'props': 'str'
    }

    attribute_map = {
        'module_type': 'module_type',
        'text': 'text',
        'image': 'image',
        'action': 'action',
        'modules': 'modules',
        'props': 'props'
    }

    def __init__(self, module_type=None, text=None, image=None, action=None, modules=None, props=None):  # noqa: E501
        """CardModule - a model defined in Swagger"""  # noqa: E501
        self._module_type = None
        self._text = None
        self._image = None
        self._action = None
        self._modules = None
        self._props = None
        self.discriminator = None
        self.module_type = module_type
        if text is not None:
            self.text = text
        if image is not None:
            self.image = image
        if action is not None:
            self.action = action
        if modules is not None:
            self.modules = modules
        if props is not None:
            self.props = props

    @property
    def module_type(self):
        """Gets the module_type of this CardModule.  # noqa: E501


        :return: The module_type of this CardModule.  # noqa: E501
        :rtype: str
        """
        return self._module_type

    @module_type.setter
    def module_type(self, module_type):
        """Sets the module_type of this CardModule.


        :param module_type: The module_type of this CardModule.  # noqa: E501
        :type: str
        """
        if module_type is None:
            raise ValueError("Invalid value for `module_type`, must not be `None`")  # noqa: E501
        allowed_values = ["text", "image", "image_text", "buttons", "phone_leads", "button", "div_line", ""]  # noqa: E501
        if module_type not in allowed_values:
            raise ValueError(
                "Invalid value for `module_type` ({0}), must be one of {1}"  # noqa: E501
                .format(module_type, allowed_values)
            )

        self._module_type = module_type

    @property
    def text(self):
        """Gets the text of this CardModule.  # noqa: E501

        文本  # noqa: E501

        :return: The text of this CardModule.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CardModule.

        文本  # noqa: E501

        :param text: The text of this CardModule.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def image(self):
        """Gets the image of this CardModule.  # noqa: E501


        :return: The image of this CardModule.  # noqa: E501
        :rtype: CardModuleImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CardModule.


        :param image: The image of this CardModule.  # noqa: E501
        :type: CardModuleImage
        """

        self._image = image

    @property
    def action(self):
        """Gets the action of this CardModule.  # noqa: E501


        :return: The action of this CardModule.  # noqa: E501
        :rtype: ModuleAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CardModule.


        :param action: The action of this CardModule.  # noqa: E501
        :type: ModuleAction
        """

        self._action = action

    @property
    def modules(self):
        """Gets the modules of this CardModule.  # noqa: E501

        子模块  # noqa: E501

        :return: The modules of this CardModule.  # noqa: E501
        :rtype: list[CardSubModule]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        """Sets the modules of this CardModule.

        子模块  # noqa: E501

        :param modules: The modules of this CardModule.  # noqa: E501
        :type: list[CardSubModule]
        """

        self._modules = modules

    @property
    def props(self):
        """Gets the props of this CardModule.  # noqa: E501

        卡片属性 json string  # noqa: E501

        :return: The props of this CardModule.  # noqa: E501
        :rtype: str
        """
        return self._props

    @props.setter
    def props(self, props):
        """Sets the props of this CardModule.

        卡片属性 json string  # noqa: E501

        :param props: The props of this CardModule.  # noqa: E501
        :type: str
        """

        self._props = props

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
        if issubclass(CardModule, dict):
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
        if not isinstance(other, CardModule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
