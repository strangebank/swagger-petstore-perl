# douyin_open/EnterpriseImEnterpriseIm.EnterpriseImMsgEndApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_im_message_send_post**](EnterpriseImMsgEndApi.md#enterprise_im_message_send_post) | **POST** /enterprise/im/message/send/ | 发送消息

# **enterprise_im_message_send_post**
> InlineResponse200 enterprise_im_message_send_post(body, open_id, access_token)

发送消息

* Scope: `enterprise.im` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseImEnterpriseIm
from douyin_open/EnterpriseImEnterpriseIm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseImEnterpriseIm.EnterpriseImMsgEndApi()
body = douyin_open/EnterpriseImEnterpriseIm.Body() # Body | 
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 发送消息
    api_response = api_instance.enterprise_im_message_send_post(body, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseImMsgEndApi->enterprise_im_message_send_post: %s\n" % e)
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

