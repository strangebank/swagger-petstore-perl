# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

from douyin_open.PoiSupplierSupplier.api.poi_supplier_api import PoiSupplierApi  # noqa: E501


class TestPoiSupplierApi(unittest.TestCase):
    """PoiSupplierApi unit test stubs"""

    def setUp(self):
        self.api = PoiSupplierApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_poi_query_get(self):
        """Test case for poi_query_get

        获取抖音POI ID  # noqa: E501
        """
        pass

    def test_poi_supplier_match_post(self):
        """Test case for poi_supplier_match_post

        店铺匹配  # noqa: E501
        """
        pass

    def test_poi_supplier_match_query_get(self):
        """Test case for poi_supplier_match_query_get

        店铺匹配结果查询  # noqa: E501
        """
        pass

    def test_poi_supplier_query_get(self):
        """Test case for poi_supplier_query_get

        查询店铺  # noqa: E501
        """
        pass

    def test_poi_supplier_sync_post(self):
        """Test case for poi_supplier_sync_post

        商铺同步  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()