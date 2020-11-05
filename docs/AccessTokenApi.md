# douyin_open/Oauth2UserToken.AccessTokenApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_access_token_get**](AccessTokenApi.md#oauth_access_token_get) | **GET** /oauth/access_token/ | 获取access_token

# **oauth_access_token_get**
> InlineResponse200 oauth_access_token_get(client_key, client_secret, code, grant_type)

获取access_token

### Example
```python
from __future__ import print_function
import time
import douyin_open/Oauth2UserToken
from douyin_open/Oauth2UserToken.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/Oauth2UserToken.AccessTokenApi()
client_key = 'client_key_example' # str | 应用唯一标识
client_secret = 'client_secret_example' # str | 应用唯一标识对应的密钥
code = 'code_example' # str | 授权码
grant_type = 'grant_type_example' # str | 写死\"authorization_code\"即可

try:
    # 获取access_token
    api_response = api_instance.oauth_access_token_get(client_key, client_secret, code, grant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokenApi->oauth_access_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| 应用唯一标识 | 
 **client_secret** | **str**| 应用唯一标识对应的密钥 | 
 **code** | **str**| 授权码 | 
 **grant_type** | **str**| 写死\&quot;authorization_code\&quot;即可 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

