# douyin_open/DouyinPayDouyinPay.DouyinPayAccountTransApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**douyin_pay_account_trans_post**](DouyinPayAccountTransApi.md#douyin_pay_account_trans_post) | **POST** /douyin-pay/account-trans/ | 商户向用户转账

# **douyin_pay_account_trans_post**
> InlineResponse200 douyin_pay_account_trans_post(body, open_id, access_token)

商户向用户转账

* Scope: `douyin.pay` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/DouyinPayDouyinPay
from douyin_open/DouyinPayDouyinPay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/DouyinPayDouyinPay.DouyinPayAccountTransApi()
body = douyin_open/DouyinPayDouyinPay.Body() # Body | 
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 商户向用户转账
    api_response = api_instance.douyin_pay_account_trans_post(body, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DouyinPayAccountTransApi->douyin_pay_account_trans_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

