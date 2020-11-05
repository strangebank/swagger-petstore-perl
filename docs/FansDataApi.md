# douyin_open/FansDataFansData.FansDataApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fans_data_get**](FansDataApi.md#fans_data_get) | **GET** /fans/data/ | 获取用户粉丝数据

# **fans_data_get**
> InlineResponse200 fans_data_get(open_id, access_token)

获取用户粉丝数据

* Scope: `fans.data` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/FansDataFansData
from douyin_open/FansDataFansData.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/FansDataFansData.FansDataApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 获取用户粉丝数据
    api_response = api_instance.fans_data_get(open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FansDataApi->fans_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

