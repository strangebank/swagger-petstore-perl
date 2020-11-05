# douyin_open/EnterpriseGrouponGrouponCodeCodeDeposit.EnterpriseGrouponCodeDepositApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_groupon_code_deposit_post**](EnterpriseGrouponCodeDepositApi.md#enterprise_groupon_code_deposit_post) | **POST** /enterprise/groupon/code/deposit/ | 自定义卷码预存

# **enterprise_groupon_code_deposit_post**
> InlineResponse200 enterprise_groupon_code_deposit_post(access_token, open_id, body=body)

自定义卷码预存

* Scope: `enterprise.groupon` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseGrouponGrouponCodeCodeDeposit
from douyin_open/EnterpriseGrouponGrouponCodeCodeDeposit.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseGrouponGrouponCodeCodeDeposit.EnterpriseGrouponCodeDepositApi()
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
body = douyin_open/EnterpriseGrouponGrouponCodeCodeDeposit.Body() # Body |  (optional)

try:
    # 自定义卷码预存
    api_response = api_instance.enterprise_groupon_code_deposit_post(access_token, open_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseGrouponCodeDepositApi->enterprise_groupon_code_deposit_post: %s\n" % e)
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

