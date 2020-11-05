# douyin_open/EnterpriseImFancyCardCardDetail.EnterpriseImFancyCardDetailApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_im_fancy_card_detail_get**](EnterpriseImFancyCardDetailApi.md#enterprise_im_fancy_card_detail_get) | **GET** /enterprise/im/fancy/card/detail/ | 获取指定动态卡片模版

# **enterprise_im_fancy_card_detail_get**
> InlineResponse200 enterprise_im_fancy_card_detail_get(open_id, access_token, card_id)

获取指定动态卡片模版

* Scope: `enterprise.im` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseImFancyCardCardDetail
from douyin_open/EnterpriseImFancyCardCardDetail.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseImFancyCardCardDetail.EnterpriseImFancyCardDetailApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
card_id = 'card_id_example' # str | 卡片id

try:
    # 获取指定动态卡片模版
    api_response = api_instance.enterprise_im_fancy_card_detail_get(open_id, access_token, card_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseImFancyCardDetailApi->enterprise_im_fancy_card_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **card_id** | **str**| 卡片id | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

