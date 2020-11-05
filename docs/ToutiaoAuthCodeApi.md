# douyin_open/ToutiaoOauth2Oauth2.ToutiaoAuthCodeApi

All URIs are relative to *https://open.snssdk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_authorize_get**](ToutiaoAuthCodeApi.md#oauth_authorize_get) | **GET** /oauth/authorize/ | 获取授权码(code)

# **oauth_authorize_get**
> oauth_authorize_get(client_key, response_type, scope, redirect_uri, state=state)

获取授权码(code)

注意该URL不是用来请求的, 需要展示给用户用于扫码。  在抖音APP支持端内唤醒的版本内打开的话会弹出客户端原生授权页面。  使用本接口前提:    1. 首先你需要去官网申请，使你的应用可以使用特定的Scope，具体需要哪些Scope，请查看各接口定义。    2. 其次你需要在本URL的scope字段中填上用户需要授权给你的Scope。    3. 用户授权通过后，你才可以调用相应的接口。 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ToutiaoOauth2Oauth2
from douyin_open/ToutiaoOauth2Oauth2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ToutiaoOauth2Oauth2.ToutiaoAuthCodeApi()
client_key = 'client_key_example' # str | 应用唯一标识
response_type = 'response_type_example' # str | 填写code
scope = 'scope_example' # str | 应用授权作用域,多个授权作用域以英文逗号（,）分隔
redirect_uri = 'redirect_uri_example' # str | 授权成功后的回调地址，必须以http/https开头。
state = 'state_example' # str | 用于保持请求和回调的状态 (optional)

try:
    # 获取授权码(code)
    api_instance.oauth_authorize_get(client_key, response_type, scope, redirect_uri, state=state)
except ApiException as e:
    print("Exception when calling ToutiaoAuthCodeApi->oauth_authorize_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| 应用唯一标识 | 
 **response_type** | **str**| 填写code | 
 **scope** | **str**| 应用授权作用域,多个授权作用域以英文逗号（,）分隔 | 
 **redirect_uri** | **str**| 授权成功后的回调地址，必须以http/https开头。 | 
 **state** | **str**| 用于保持请求和回调的状态 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

