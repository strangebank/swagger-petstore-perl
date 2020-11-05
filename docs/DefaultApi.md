# douyin_open/ToutiaoOauth2Oauth2.DefaultApi

All URIs are relative to *https://open.snssdk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_access_token_get**](DefaultApi.md#oauth_access_token_get) | **GET** /oauth/access_token/ | 获取access_token
[**oauth_refresh_token_get**](DefaultApi.md#oauth_refresh_token_get) | **GET** /oauth/refresh_token/ | 刷新access_token

# **oauth_access_token_get**
> InlineResponse200 oauth_access_token_get(client_key, client_secret, code, grant_type)

获取access_token

### Example
```python
from __future__ import print_function
import time
import douyin_open/ToutiaoOauth2Oauth2
from douyin_open/ToutiaoOauth2Oauth2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ToutiaoOauth2Oauth2.DefaultApi()
client_key = 'client_key_example' # str | 应用唯一标识
client_secret = 'client_secret_example' # str | 应用唯一标识对应的密钥
code = 'code_example' # str | 授权码
grant_type = 'grant_type_example' # str | 写死\"authorization_code\"即可

try:
    # 获取access_token
    api_response = api_instance.oauth_access_token_get(client_key, client_secret, code, grant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->oauth_access_token_get: %s\n" % e)
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

# **oauth_refresh_token_get**
> InlineResponse2001 oauth_refresh_token_get(client_key, grant_type, refresh_token)

刷新access_token

### Example
```python
from __future__ import print_function
import time
import douyin_open/ToutiaoOauth2Oauth2
from douyin_open/ToutiaoOauth2Oauth2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ToutiaoOauth2Oauth2.DefaultApi()
client_key = 'client_key_example' # str | 应用唯一标识
grant_type = 'grant_type_example' # str | 填refresh_token
refresh_token = 'refresh_token_example' # str | 填写通过access_token获取到的refresh_token参数

try:
    # 刷新access_token
    api_response = api_instance.oauth_refresh_token_get(client_key, grant_type, refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->oauth_refresh_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| 应用唯一标识 | 
 **grant_type** | **str**| 填refresh_token | 
 **refresh_token** | **str**| 填写通过access_token获取到的refresh_token参数 | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

