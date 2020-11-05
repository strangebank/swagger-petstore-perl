# douyin_open/EnterpriseGrouponGrouponCodeCodeVerification.EnterpriseGrouponCodeCertApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_groupon_code_verification_post**](EnterpriseGrouponCodeCertApi.md#enterprise_groupon_code_verification_post) | **POST** /enterprise/groupon/code/verification/ | 券码核销

# **enterprise_groupon_code_verification_post**
> InlineResponse200 enterprise_groupon_code_verification_post(access_token, open_id, body=body)

券码核销

* Scope: `enterprise.groupon` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseGrouponGrouponCodeCodeVerification
from douyin_open/EnterpriseGrouponGrouponCodeCodeVerification.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseGrouponGrouponCodeCodeVerification.EnterpriseGrouponCodeCertApi()
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
body = douyin_open/EnterpriseGrouponGrouponCodeCodeVerification.Body() # Body |  (optional)

try:
    # 券码核销
    api_response = api_instance.enterprise_groupon_code_verification_post(access_token, open_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseGrouponCodeCertApi->enterprise_groupon_code_verification_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

