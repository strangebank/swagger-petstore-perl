# douyin_open/EnterpriseGrouponGrouponOrderOrderDetail.EnterpriseGrouponOrderDetailApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_groupon_order_detail_get**](EnterpriseGrouponOrderDetailApi.md#enterprise_groupon_order_detail_get) | **GET** /enterprise/groupon/order/detail/ | 团购活动订单详情

# **enterprise_groupon_order_detail_get**
> InlineResponse200 enterprise_groupon_order_detail_get(access_token, open_id, order_id)

团购活动订单详情

* Scope: `enterprise.groupon` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseGrouponGrouponOrderOrderDetail
from douyin_open/EnterpriseGrouponGrouponOrderOrderDetail.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseGrouponGrouponOrderOrderDetail.EnterpriseGrouponOrderDetailApi()
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
order_id = 'order_id_example' # str | 订单id

try:
    # 团购活动订单详情
    api_response = api_instance.enterprise_groupon_order_detail_get(access_token, open_id, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseGrouponOrderDetailApi->enterprise_groupon_order_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **order_id** | **str**| 订单id | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

