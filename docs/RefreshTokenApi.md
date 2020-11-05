# douyin_open/Oauth2RefreshToken.RefreshTokenApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_refresh_token_get**](RefreshTokenApi.md#oauth_refresh_token_get) | **GET** /oauth/refresh_token/ | 刷新access_token

# **oauth_refresh_token_get**
> InlineResponse200 oauth_refresh_token_get(client_key, grant_type, refresh_token)

刷新access_token

### Example
```python
from __future__ import print_function
import time
import douyin_open/Oauth2RefreshToken
from douyin_open/Oauth2RefreshToken.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/Oauth2RefreshToken.RefreshTokenApi()
client_key = 'client_key_example' # str | 应用唯一标识
grant_type = 'grant_type_example' # str | 填refresh_token
refresh_token = 'refresh_token_example' # str | 填写通过access_token获取到的refresh_token参数

try:
    # 刷新access_token
    api_response = api_instance.oauth_refresh_token_get(client_key, grant_type, refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefreshTokenApi->oauth_refresh_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| 应用唯一标识 | 
 **grant_type** | **str**| 填refresh_token | 
 **refresh_token** | **str**| 填写通过access_token获取到的refresh_token参数 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

