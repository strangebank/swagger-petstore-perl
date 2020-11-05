# douyin_open/DouyinPayDouyinPay.DouyinPayAccountQueryApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**douyin_pay_account_query_get**](DouyinPayAccountQueryApi.md#douyin_pay_account_query_get) | **GET** /douyin-pay/account-query/ | 账户余额查询

# **douyin_pay_account_query_get**
> InlineResponse2002 douyin_pay_account_query_get(access_token, merchant_id, live_id)

账户余额查询

* Scope: `douyin.pay.op` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/DouyinPayDouyinPay
from douyin_open/DouyinPayDouyinPay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/DouyinPayDouyinPay.DouyinPayAccountQueryApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
merchant_id = 56 # int | 商户id
live_id = 56 # int | 业务id

try:
    # 账户余额查询
    api_response = api_instance.douyin_pay_account_query_get(access_token, merchant_id, live_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DouyinPayAccountQueryApi->douyin_pay_account_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **merchant_id** | **int**| 商户id | 
 **live_id** | **int**| 业务id | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

