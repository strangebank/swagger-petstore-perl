# douyin_open/VideoSearchVideoSearch.VideoSearchApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_search_get**](VideoSearchApi.md#video_search_get) | **GET** /video/search/ | 关键词视频搜索

# **video_search_get**
> InlineResponse200 video_search_get(open_id, access_token, count, keyword, cursor=cursor)

关键词视频搜索

* Scope: `video.search` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoSearchVideoSearch
from douyin_open/VideoSearchVideoSearch.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoSearchVideoSearch.VideoSearchApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 56 # int | 每页数量
keyword = 'keyword_example' # str | 关键词
cursor = 56 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)

try:
    # 关键词视频搜索
    api_response = api_instance.video_search_get(open_id, access_token, count, keyword, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoSearchApi->video_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **keyword** | **str**| 关键词 | 
 **cursor** | **int**| 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

