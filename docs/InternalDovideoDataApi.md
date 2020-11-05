# douyin_open/InternalVideoDataInternalVideoData.InternalDovideoDataApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**internal_video_data_post**](InternalDovideoDataApi.md#internal_video_data_post) | **POST** /internal/video/data/ | 批量获取视频数据信息

# **internal_video_data_post**
> InlineResponse200 internal_video_data_post(body, open_id, access_token)

批量获取视频数据信息

* Scope: `internal.video.data` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/InternalVideoDataInternalVideoData
from douyin_open/InternalVideoDataInternalVideoData.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/InternalVideoDataInternalVideoData.InternalDovideoDataApi()
body = douyin_open/InternalVideoDataInternalVideoData.Body() # Body | 
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 批量获取视频数据信息
    api_response = api_instance.internal_video_data_post(body, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalDovideoDataApi->internal_video_data_post: %s\n" % e)
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

