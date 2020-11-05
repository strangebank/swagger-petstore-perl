# coding: utf-8

"""
    创建团购活动

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class GrouponItem(object):
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
        'use_type': 'int',
        'code_type': 'int',
        'merchant_name': 'str',
        'service_number': 'str',
        'title': 'str',
        'cover_images': 'list[str]',
        'original_amount': 'int',
        'actual_amount': 'int',
        'notification': 'str',
        'order_limit': 'int',
        'stock': 'int',
        'poi_ids': 'list[str]',
        'groupon_goods': 'list[GrouponItemGrouponGoods]',
        'start_time': 'int',
        'end_time': 'int',
        'h5_url': 'str',
        'status': 'int',
        'sold_count': 'int',
        'audit_msg': 'str'
    }

    attribute_map = {
        'groupon_id': 'groupon_id',
        'use_type': 'use_type',
        'code_type': 'code_type',
        'merchant_name': 'merchant_name',
        'service_number': 'service_number',
        'title': 'title',
        'cover_images': 'cover_images',
        'original_amount': 'original_amount',
        'actual_amount': 'actual_amount',
        'notification': 'notification',
        'order_limit': 'order_limit',
        'stock': 'stock',
        'poi_ids': 'poi_ids',
        'groupon_goods': 'groupon_goods',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'h5_url': 'h5_url',
        'status': 'status',
        'sold_count': 'sold_count',
        'audit_msg': 'audit_msg'
    }

    def __init__(self, groupon_id=None, use_type=None, code_type=Code_typeEnum._1, merchant_name=None, service_number=None, title=None, cover_images=None, original_amount=None, actual_amount=None, notification=None, order_limit=None, stock=None, poi_ids=None, groupon_goods=None, start_time=None, end_time=None, h5_url=None, status=None, sold_count=None, audit_msg=None):  # noqa: E501
        """GrouponItem - a model defined in Swagger"""  # noqa: E501
        self._groupon_id = None
        self._use_type = None
        self._code_type = None
        self._merchant_name = None
        self._service_number = None
        self._title = None
        self._cover_images = None
        self._original_amount = None
        self._actual_amount = None
        self._notification = None
        self._order_limit = None
        self._stock = None
        self._poi_ids = None
        self._groupon_goods = None
        self._start_time = None
        self._end_time = None
        self._h5_url = None
        self._status = None
        self._sold_count = None
        self._audit_msg = None
        self.discriminator = None
        if groupon_id is not None:
            self.groupon_id = groupon_id
        self.use_type = use_type
        self.code_type = code_type
        self.merchant_name = merchant_name
        self.service_number = service_number
        self.title = title
        self.cover_images = cover_images
        self.original_amount = original_amount
        self.actual_amount = actual_amount
        self.notification = notification
        self.order_limit = order_limit
        self.stock = stock
        if poi_ids is not None:
            self.poi_ids = poi_ids
        self.groupon_goods = groupon_goods
        self.start_time = start_time
        self.end_time = end_time
        self.h5_url = h5_url
        if status is not None:
            self.status = status
        if sold_count is not None:
            self.sold_count = sold_count
        if audit_msg is not None:
            self.audit_msg = audit_msg

    @property
    def groupon_id(self):
        """Gets the groupon_id of this GrouponItem.  # noqa: E501

        团购活动Id，审核失败修改用  # noqa: E501

        :return: The groupon_id of this GrouponItem.  # noqa: E501
        :rtype: str
        """
        return self._groupon_id

    @groupon_id.setter
    def groupon_id(self, groupon_id):
        """Sets the groupon_id of this GrouponItem.

        团购活动Id，审核失败修改用  # noqa: E501

        :param groupon_id: The groupon_id of this GrouponItem.  # noqa: E501
        :type: str
        """

        self._groupon_id = groupon_id

    @property
    def use_type(self):
        """Gets the use_type of this GrouponItem.  # noqa: E501

        * 团购使用方式   * 1: 到店核销   # noqa: E501

        :return: The use_type of this GrouponItem.  # noqa: E501
        :rtype: int
        """
        return self._use_type

    @use_type.setter
    def use_type(self, use_type):
        """Sets the use_type of this GrouponItem.

        * 团购使用方式   * 1: 到店核销   # noqa: E501

        :param use_type: The use_type of this GrouponItem.  # noqa: E501
        :type: int
        """
        if use_type is None:
            raise ValueError("Invalid value for `use_type`, must not be `None`")  # noqa: E501
        allowed_values = [1, ""]  # noqa: E501
        if use_type not in allowed_values:
            raise ValueError(
                "Invalid value for `use_type` ({0}), must be one of {1}"  # noqa: E501
                .format(use_type, allowed_values)
            )

        self._use_type = use_type

    @property
    def code_type(self):
        """Gets the code_type of this GrouponItem.  # noqa: E501

        * 券码生成的方式   * 1: 系统生成   * 2: 自定义上传   # noqa: E501

        :return: The code_type of this GrouponItem.  # noqa: E501
        :rtype: int
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this GrouponItem.

        * 券码生成的方式   * 1: 系统生成   * 2: 自定义上传   # noqa: E501

        :param code_type: The code_type of this GrouponItem.  # noqa: E501
        :type: int
        """
        if code_type is None:
            raise ValueError("Invalid value for `code_type`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2, ""]  # noqa: E501
        if code_type not in allowed_values:
            raise ValueError(
                "Invalid value for `code_type` ({0}), must be one of {1}"  # noqa: E501
                .format(code_type, allowed_values)
            )

        self._code_type = code_type

    @property
    def merchant_name(self):
        """Gets the merchant_name of this GrouponItem.  # noqa: E501

        商户名称  # noqa: E501

        :return: The merchant_name of this GrouponItem.  # noqa: E501
        :rtype: str
        """
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, merchant_name):
        """Sets the merchant_name of this GrouponItem.

        商户名称  # noqa: E501

        :param merchant_name: The merchant_name of this GrouponItem.  # noqa: E501
        :type: str
        """
        if merchant_name is None:
            raise ValueError("Invalid value for `merchant_name`, must not be `None`")  # noqa: E501

        self._merchant_name = merchant_name

    @property
    def service_number(self):
        """Gets the service_number of this GrouponItem.  # noqa: E501

        联系电话  # noqa: E501

        :return: The service_number of this GrouponItem.  # noqa: E501
        :rtype: str
        """
        return self._service_number

    @service_number.setter
    def service_number(self, service_number):
        """Sets the service_number of this GrouponItem.

        联系电话  # noqa: E501

        :param service_number: The service_number of this GrouponItem.  # noqa: E501
        :type: str
        """
        if service_number is None:
            raise ValueError("Invalid value for `service_number`, must not be `None`")  # noqa: E501

        self._service_number = service_number

    @property
    def title(self):
        """Gets the title of this GrouponItem.  # noqa: E501

        卡券标题  # noqa: E501

        :return: The title of this GrouponItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GrouponItem.

        卡券标题  # noqa: E501

        :param title: The title of this GrouponItem.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def cover_images(self):
        """Gets the cover_images of this GrouponItem.  # noqa: E501

        封面图  # noqa: E501

        :return: The cover_images of this GrouponItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._cover_images

    @cover_images.setter
    def cover_images(self, cover_images):
        """Sets the cover_images of this GrouponItem.

        封面图  # noqa: E501

        :param cover_images: The cover_images of this GrouponItem.  # noqa: E501
        :type: list[str]
        """
        if cover_images is None:
            raise ValueError("Invalid value for `cover_images`, must not be `None`")  # noqa: E501

        self._cover_images = cover_images

    @property
    def original_amount(self):
        """Gets the original_amount of this GrouponItem.  # noqa: E501

        原价(单位分)  # noqa: E501

        :return: The original_amount of this GrouponItem.  # noqa: E501
        :rtype: int
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        """Sets the original_amount of this GrouponItem.

        原价(单位分)  # noqa: E501

        :param original_amount: The original_amount of this GrouponItem.  # noqa: E501
        :type: int
        """
        if original_amount is None:
            raise ValueError("Invalid value for `original_amount`, must not be `None`")  # noqa: E501

        self._original_amount = original_amount

    @property
    def actual_amount(self):
        """Gets the actual_amount of this GrouponItem.  # noqa: E501

        实际金额(单位分)  # noqa: E501

        :return: The actual_amount of this GrouponItem.  # noqa: E501
        :rtype: int
        """
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, actual_amount):
        """Sets the actual_amount of this GrouponItem.

        实际金额(单位分)  # noqa: E501

        :param actual_amount: The actual_amount of this GrouponItem.  # noqa: E501
        :type: int
        """
        if actual_amount is None:
            raise ValueError("Invalid value for `actual_amount`, must not be `None`")  # noqa: E501

        self._actual_amount = actual_amount

    @property
    def notification(self):
        """Gets the notification of this GrouponItem.  # noqa: E501

        团购须知  # noqa: E501

        :return: The notification of this GrouponItem.  # noqa: E501
        :rtype: str
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this GrouponItem.

        团购须知  # noqa: E501

        :param notification: The notification of this GrouponItem.  # noqa: E501
        :type: str
        """
        if notification is None:
            raise ValueError("Invalid value for `notification`, must not be `None`")  # noqa: E501

        self._notification = notification

    @property
    def order_limit(self):
        """Gets the order_limit of this GrouponItem.  # noqa: E501

        单用户购买数量上限  # noqa: E501

        :return: The order_limit of this GrouponItem.  # noqa: E501
        :rtype: int
        """
        return self._order_limit

    @order_limit.setter
    def order_limit(self, order_limit):
        """Sets the order_limit of this GrouponItem.

        单用户购买数量上限  # noqa: E501

        :param order_limit: The order_limit of this GrouponItem.  # noqa: E501
        :type: int
        """
        if order_limit is None:
            raise ValueError("Invalid value for `order_limit`, must not be `None`")  # noqa: E501

        self._order_limit = order_limit

    @property
    def stock(self):
        """Gets the stock of this GrouponItem.  # noqa: E501

        团购活动库存总数  # noqa: E501

        :return: The stock of this GrouponItem.  # noqa: E501
        :rtype: int
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this GrouponItem.

        团购活动库存总数  # noqa: E501

        :param stock: The stock of this GrouponItem.  # noqa: E501
        :type: int
        """
        if stock is None:
            raise ValueError("Invalid value for `stock`, must not be `None`")  # noqa: E501

        self._stock = stock

    @property
    def poi_ids(self):
        """Gets the poi_ids of this GrouponItem.  # noqa: E501

        * 绑定的POI 列表 默认展示全部门店   # noqa: E501

        :return: The poi_ids of this GrouponItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._poi_ids

    @poi_ids.setter
    def poi_ids(self, poi_ids):
        """Sets the poi_ids of this GrouponItem.

        * 绑定的POI 列表 默认展示全部门店   # noqa: E501

        :param poi_ids: The poi_ids of this GrouponItem.  # noqa: E501
        :type: list[str]
        """

        self._poi_ids = poi_ids

    @property
    def groupon_goods(self):
        """Gets the groupon_goods of this GrouponItem.  # noqa: E501

        团购商品  # noqa: E501

        :return: The groupon_goods of this GrouponItem.  # noqa: E501
        :rtype: list[GrouponItemGrouponGoods]
        """
        return self._groupon_goods

    @groupon_goods.setter
    def groupon_goods(self, groupon_goods):
        """Sets the groupon_goods of this GrouponItem.

        团购商品  # noqa: E501

        :param groupon_goods: The groupon_goods of this GrouponItem.  # noqa: E501
        :type: list[GrouponItemGrouponGoods]
        """
        if groupon_goods is None:
            raise ValueError("Invalid value for `groupon_goods`, must not be `None`")  # noqa: E501

        self._groupon_goods = groupon_goods

    @property
    def start_time(self):
        """Gets the start_time of this GrouponItem.  # noqa: E501

        * 活动开始时间 unix time   # noqa: E501

        :return: The start_time of this GrouponItem.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this GrouponItem.

        * 活动开始时间 unix time   # noqa: E501

        :param start_time: The start_time of this GrouponItem.  # noqa: E501
        :type: int
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this GrouponItem.  # noqa: E501

        * 活动截止时间 unix time   # noqa: E501

        :return: The end_time of this GrouponItem.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this GrouponItem.

        * 活动截止时间 unix time   # noqa: E501

        :param end_time: The end_time of this GrouponItem.  # noqa: E501
        :type: int
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def h5_url(self):
        """Gets the h5_url of this GrouponItem.  # noqa: E501

        团购活动详情页链接  # noqa: E501

        :return: The h5_url of this GrouponItem.  # noqa: E501
        :rtype: str
        """
        return self._h5_url

    @h5_url.setter
    def h5_url(self, h5_url):
        """Sets the h5_url of this GrouponItem.

        团购活动详情页链接  # noqa: E501

        :param h5_url: The h5_url of this GrouponItem.  # noqa: E501
        :type: str
        """
        if h5_url is None:
            raise ValueError("Invalid value for `h5_url`, must not be `None`")  # noqa: E501

        self._h5_url = h5_url

    @property
    def status(self):
        """Gets the status of this GrouponItem.  # noqa: E501

        * 活动状态 创建时可以忽略  * 1：有效  * 2：审核中  * 3：审核失败  * 4：中止   # noqa: E501

        :return: The status of this GrouponItem.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GrouponItem.

        * 活动状态 创建时可以忽略  * 1：有效  * 2：审核中  * 3：审核失败  * 4：中止   # noqa: E501

        :param status: The status of this GrouponItem.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4, ""]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def sold_count(self):
        """Gets the sold_count of this GrouponItem.  # noqa: E501

        已售出数量  # noqa: E501

        :return: The sold_count of this GrouponItem.  # noqa: E501
        :rtype: int
        """
        return self._sold_count

    @sold_count.setter
    def sold_count(self, sold_count):
        """Sets the sold_count of this GrouponItem.

        已售出数量  # noqa: E501

        :param sold_count: The sold_count of this GrouponItem.  # noqa: E501
        :type: int
        """

        self._sold_count = sold_count

    @property
    def audit_msg(self):
        """Gets the audit_msg of this GrouponItem.  # noqa: E501

        审核失败原因  # noqa: E501

        :return: The audit_msg of this GrouponItem.  # noqa: E501
        :rtype: str
        """
        return self._audit_msg

    @audit_msg.setter
    def audit_msg(self, audit_msg):
        """Sets the audit_msg of this GrouponItem.

        审核失败原因  # noqa: E501

        :param audit_msg: The audit_msg of this GrouponItem.  # noqa: E501
        :type: str
        """

        self._audit_msg = audit_msg

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
        if issubclass(GrouponItem, dict):
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
        if not isinstance(other, GrouponItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
