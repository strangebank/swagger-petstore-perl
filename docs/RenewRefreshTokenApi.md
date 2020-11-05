# douyin_open/Oauth2NewRefreshToken.RenewRefreshTokenApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_renew_refresh_token_get**](RenewRefreshTokenApi.md#oauth_renew_refresh_token_get) | **GET** /oauth/renew_refresh_token/ | 刷新refresh_token

# **oauth_renew_refresh_token_get**
> InlineResponse200 oauth_renew_refresh_token_get(client_key, refresh_token)

刷新refresh_token

### Example
```python
from __future__ import print_function
import time
import douyin_open/Oauth2NewRefreshToken
from douyin_open/Oauth2NewRefreshToken.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/Oauth2NewRefreshToken.RenewRefreshTokenApi()
client_key = 'client_key_example' # str | 应用唯一标识
refresh_token = 'refresh_token_example' # str | 填写通过access_token获取到的refresh_token参数

try:
    # 刷新refresh_token
    api_response = api_instance.oauth_renew_refresh_token_get(client_key, refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RenewRefreshTokenApi->oauth_renew_refresh_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| 应用唯一标识 | 
 **refresh_token** | **str**| 填写通过access_token获取到的refresh_token参数 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

