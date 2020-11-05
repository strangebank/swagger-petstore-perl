# douyin_open/DouyinPayDouyinPay.DouyinPayOrderQueryApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**douyin_pay_order_query_get**](DouyinPayOrderQueryApi.md#douyin_pay_order_query_get) | **GET** /douyin-pay/order-query/ | 订单查询，可查询一个月内的订单，优先级biz_order_no&gt;pay_order_no

# **douyin_pay_order_query_get**
> InlineResponse2001 douyin_pay_order_query_get(access_token, merchant_id, live_id, biz_order_no=biz_order_no, pay_order_no=pay_order_no)

订单查询，可查询一个月内的订单，优先级biz_order_no>pay_order_no

* Scope: `douyin.pay.op` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/DouyinPayDouyinPay
from douyin_open/DouyinPayDouyinPay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/DouyinPayDouyinPay.DouyinPayOrderQueryApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
merchant_id = 56 # int | 商户id
live_id = 56 # int | 业务id
biz_order_no = 'biz_order_no_example' # str | 外部订单号，由调用方生成 (optional)
pay_order_no = 'pay_order_no_example' # str | 抖音订单号，由抖音生成 (optional)

try:
    # 订单查询，可查询一个月内的订单，优先级biz_order_no>pay_order_no
    api_response = api_instance.douyin_pay_order_query_get(access_token, merchant_id, live_id, biz_order_no=biz_order_no, pay_order_no=pay_order_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DouyinPayOrderQueryApi->douyin_pay_order_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **merchant_id** | **int**| 商户id | 
 **live_id** | **int**| 业务id | 
 **biz_order_no** | **str**| 外部订单号，由调用方生成 | [optional] 
 **pay_order_no** | **str**| 抖音订单号，由抖音生成 | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

