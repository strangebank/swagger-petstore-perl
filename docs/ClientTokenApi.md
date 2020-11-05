# douyin_open/Oauth2ClientToken.ClientTokenApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_client_token_get**](ClientTokenApi.md#oauth_client_token_get) | **GET** /oauth/client_token/ | 生成client_token

# **oauth_client_token_get**
> InlineResponse200 oauth_client_token_get(client_key, client_secret, grant_type)

生成client_token

### Example
```python
from __future__ import print_function
import time
import douyin_open/Oauth2ClientToken
from douyin_open/Oauth2ClientToken.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/Oauth2ClientToken.ClientTokenApi()
client_key = 'client_key_example' # str | 应用唯一标识
client_secret = 'client_secret_example' # str | 应用唯一标识对应的密钥
grant_type = 'grant_type_example' # str | 传client_credential

try:
    # 生成client_token
    api_response = api_instance.oauth_client_token_get(client_key, client_secret, grant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientTokenApi->oauth_client_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| 应用唯一标识 | 
 **client_secret** | **str**| 应用唯一标识对应的密钥 | 
 **grant_type** | **str**| 传client_credential | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

