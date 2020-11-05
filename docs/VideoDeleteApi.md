# douyin_open/VideoDeleteAwemeDelete.VideoDeleteApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_delete_post**](VideoDeleteApi.md#video_delete_post) | **POST** /video/delete/ | 删除授权用户发布的视频

# **video_delete_post**
> InlineResponse200 video_delete_post(open_id, access_token, body=body)

删除授权用户发布的视频

* Scope: `video.delete` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoDeleteAwemeDelete
from douyin_open/VideoDeleteAwemeDelete.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoDeleteAwemeDelete.VideoDeleteApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin_open/VideoDeleteAwemeDelete.Body() # Body |  (optional)

try:
    # 删除授权用户发布的视频
    api_response = api_instance.video_delete_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoDeleteApi->video_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

