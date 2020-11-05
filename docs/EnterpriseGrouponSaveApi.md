# douyin_open/EnterpriseGrouponGrouponGrouponSave.EnterpriseGrouponSaveApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_groupon_save_post**](EnterpriseGrouponSaveApi.md#enterprise_groupon_save_post) | **POST** /enterprise/groupon/save/ | 创建团购活动

# **enterprise_groupon_save_post**
> InlineResponse200 enterprise_groupon_save_post(access_token, open_id, body=body)

创建团购活动

* Scope: `enterprise.groupon` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseGrouponGrouponGrouponSave
from douyin_open/EnterpriseGrouponGrouponGrouponSave.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseGrouponGrouponGrouponSave.EnterpriseGrouponSaveApi()
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
body = douyin_open/EnterpriseGrouponGrouponGrouponSave.GrouponItem() # GrouponItem |  (optional)

try:
    # 创建团购活动
    api_response = api_instance.enterprise_groupon_save_post(access_token, open_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseGrouponSaveApi->enterprise_groupon_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **body** | [**GrouponItem**](GrouponItem.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

