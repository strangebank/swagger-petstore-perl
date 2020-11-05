# douyin_open/UserUserInfoUserInfo.UserInfoApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_userinfo_get**](UserInfoApi.md#oauth_userinfo_get) | **GET** /oauth/userinfo/ | 获取用户信息

# **oauth_userinfo_get**
> InlineResponse200 oauth_userinfo_get(open_id, access_token)

获取用户信息

* Scope: `user_info` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/UserUserInfoUserInfo
from douyin_open/UserUserInfoUserInfo.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/UserUserInfoUserInfo.UserInfoApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 获取用户信息
    api_response = api_instance.oauth_userinfo_get(open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInfoApi->oauth_userinfo_get: %s\n" % e)
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

