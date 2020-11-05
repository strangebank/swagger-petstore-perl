# douyin_open/EnterprisePersonaPersonaCreate.EnterpriseImPersonaCreateApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_im_persona_create_post**](EnterpriseImPersonaCreateApi.md#enterprise_im_persona_create_post) | **POST** /enterprise/im/persona/create/ | 客服账号

# **enterprise_im_persona_create_post**
> InlineResponse200 enterprise_im_persona_create_post(body, open_id, access_token)

客服账号

* Scope: `enterprise.im` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterprisePersonaPersonaCreate
from douyin_open/EnterprisePersonaPersonaCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterprisePersonaPersonaCreate.EnterpriseImPersonaCreateApi()
body = douyin_open/EnterprisePersonaPersonaCreate.Body() # Body | 
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 客服账号
    api_response = api_instance.enterprise_im_persona_create_post(body, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseImPersonaCreateApi->enterprise_im_persona_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

