# douyin_open/StarDataStarData.StarHotListApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**star_hot_list_get**](StarHotListApi.md#star_hot_list_get) | **GET** /star/hot_list/ | 获取抖音星图达人热榜

# **star_hot_list_get**
> InlineResponse200 star_hot_list_get(access_token, hot_list_type)

获取抖音星图达人热榜

* Scope: `star_tops` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/StarDataStarData
from douyin_open/StarDataStarData.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/StarDataStarData.StarHotListApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
hot_list_type = 56 # int | 达人热榜类型 * `1` - 星图指数榜 * `2` - 涨粉指数榜 * `3` - 性价比指数榜 * `4` - 种草指数榜 * `5` - 精选指数榜 * `6` - 传播指数榜

try:
    # 获取抖音星图达人热榜
    api_response = api_instance.star_hot_list_get(access_token, hot_list_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StarHotListApi->star_hot_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **hot_list_type** | **int**| 达人热榜类型 * &#x60;1&#x60; - 星图指数榜 * &#x60;2&#x60; - 涨粉指数榜 * &#x60;3&#x60; - 性价比指数榜 * &#x60;4&#x60; - 种草指数榜 * &#x60;5&#x60; - 精选指数榜 * &#x60;6&#x60; - 传播指数榜 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

