# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

from douyin_open.DouyinPayDouyinPay.api.douyin_pay_order_query_api import DouyinPayOrderQueryApi  # noqa: E501


class TestDouyinPayOrderQueryApi(unittest.TestCase):
    """DouyinPayOrderQueryApi unit test stubs"""

    def setUp(self):
        self.api = DouyinPayOrderQueryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_douyin_pay_order_query_get(self):
        """Test case for douyin_pay_order_query_get

        订单查询，可查询一个月内的订单，优先级biz_order_no>pay_order_no  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()