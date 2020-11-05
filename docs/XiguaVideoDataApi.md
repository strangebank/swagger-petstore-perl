# douyin_open/XiguaDataVideoData.XiguaVideoDataApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**xigua_video_data_post**](XiguaVideoDataApi.md#xigua_video_data_post) | **POST** /xigua/video/data/ | 查询特定视频的视频数据

# **xigua_video_data_post**
> InlineResponse200 xigua_video_data_post(body, open_id, access_token)

查询特定视频的视频数据

* Scope: `xigua.video.data` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/XiguaDataVideoData
from douyin_open/XiguaDataVideoData.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/XiguaDataVideoData.XiguaVideoDataApi()
body = douyin_open/XiguaDataVideoData.Body() # Body | 
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 查询特定视频的视频数据
    api_response = api_instance.xigua_video_data_post(body, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XiguaVideoDataApi->xigua_video_data_post: %s\n" % e)
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

