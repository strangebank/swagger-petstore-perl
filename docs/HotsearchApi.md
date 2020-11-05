# douyin_open/HotsearchHotsearch.HotsearchApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hotsearch_sentences_get**](HotsearchApi.md#hotsearch_sentences_get) | **GET** /hotsearch/sentences/ | 获取实时热点词
[**hotsearch_trending_sentences_get**](HotsearchApi.md#hotsearch_trending_sentences_get) | **GET** /hotsearch/trending/sentences/ | 获取上升词
[**hotsearch_videos_get**](HotsearchApi.md#hotsearch_videos_get) | **GET** /hotsearch/videos/ | 获取热点词聚合的视频

# **hotsearch_sentences_get**
> InlineResponse200 hotsearch_sentences_get(access_token)

获取实时热点词

* Scope: `hotsearch` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/HotsearchHotsearch
from douyin_open/HotsearchHotsearch.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/HotsearchHotsearch.HotsearchApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 获取实时热点词
    api_response = api_instance.hotsearch_sentences_get(access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HotsearchApi->hotsearch_sentences_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotsearch_trending_sentences_get**
> InlineResponse2001 hotsearch_trending_sentences_get(access_token, count, cursor=cursor)

获取上升词

* Scope: `hotsearch` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/HotsearchHotsearch
from douyin_open/HotsearchHotsearch.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/HotsearchHotsearch.HotsearchApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
count = 56 # int | 每页数量
cursor = 56 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)

try:
    # 获取上升词
    api_response = api_instance.hotsearch_trending_sentences_get(access_token, count, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HotsearchApi->hotsearch_trending_sentences_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **cursor** | **int**| 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotsearch_videos_get**
> InlineResponse2002 hotsearch_videos_get(access_token, hot_sentence)

获取热点词聚合的视频

* Scope: `hotsearch` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/HotsearchHotsearch
from douyin_open/HotsearchHotsearch.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/HotsearchHotsearch.HotsearchApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
hot_sentence = 'hot_sentence_example' # str | 热点词

try:
    # 获取热点词聚合的视频
    api_response = api_instance.hotsearch_videos_get(access_token, hot_sentence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HotsearchApi->hotsearch_videos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **hot_sentence** | **str**| 热点词 | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

