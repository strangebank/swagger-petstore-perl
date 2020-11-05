# douyin_open/Oauth2SilentLogin.AuthorizeV2Api

All URIs are relative to *https://aweme.snssdk.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_authorize_v2_get**](AuthorizeV2Api.md#oauth_authorize_v2_get) | **GET** /oauth/authorize/v2/ | 获取授权码(code)

# **oauth_authorize_v2_get**
> oauth_authorize_v2_get(client_key, response_type, scope, redirect_uri, state=state)

获取授权码(code)

注意该URL要在抖音端内的h5页面请求，这样才能带上抖音的登录态来获取用户的OpenId。 一旦clientKey有静默授权权限login_id，接口会以重定向的方式跳转到redirect_uri，并返回code。 拿到code之后再去调用https://open.douyin.com/oauth/access_token/。

### Example
```python
from __future__ import print_function
import time
import douyin_open/Oauth2SilentLogin
from douyin_open/Oauth2SilentLogin.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/Oauth2SilentLogin.AuthorizeV2Api()
client_key = 'client_key_example' # str | 应用唯一标识
response_type = 'response_type_example' # str | 填写code
scope = 'scope_example' # str | 填login_id
redirect_uri = 'redirect_uri_example' # str | 授权成功后的回调地址，必须以http/https开头。域名要跟申请应用时填写的授权回调域一致。用于调用https://open.douyin.com/oauth/access_token/换token。
state = 'state_example' # str | 用于保持请求和回调状态，授权请求后会原样返回给接入方,如果是App则不用传该参数 (optional)

try:
    # 获取授权码(code)
    api_instance.oauth_authorize_v2_get(client_key, response_type, scope, redirect_uri, state=state)
except ApiException as e:
    print("Exception when calling AuthorizeV2Api->oauth_authorize_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| 应用唯一标识 | 
 **response_type** | **str**| 填写code | 
 **scope** | **str**| 填login_id | 
 **redirect_uri** | **str**| 授权成功后的回调地址，必须以http/https开头。域名要跟申请应用时填写的授权回调域一致。用于调用https://open.douyin.com/oauth/access_token/换token。 | 
 **state** | **str**| 用于保持请求和回调状态，授权请求后会原样返回给接入方,如果是App则不用传该参数 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

