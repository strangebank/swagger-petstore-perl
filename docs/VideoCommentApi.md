# douyin_open/VideoCommentVideoComment.VideoCommentApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_comment_list_get**](VideoCommentApi.md#video_comment_list_get) | **GET** /video/comment/list/ | 评论列表
[**video_comment_reply_list_get**](VideoCommentApi.md#video_comment_reply_list_get) | **GET** /video/comment/reply/list/ | 评论回复列表
[**video_comment_reply_post**](VideoCommentApi.md#video_comment_reply_post) | **POST** /video/comment/reply/ | 回复视频评论
[**video_comment_top_post**](VideoCommentApi.md#video_comment_top_post) | **POST** /video/comment/top/ | 置顶视频评论(企业号)

# **video_comment_list_get**
> InlineResponse200 video_comment_list_get(open_id, access_token, count, item_id, cursor=cursor)

评论列表

* Scope: `video.comment` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoCommentVideoComment
from douyin_open/VideoCommentVideoComment.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoCommentVideoComment.VideoCommentApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 56 # int | 每页数量
item_id = 'item_id_example' # str | 视频id
cursor = 56 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)

try:
    # 评论列表
    api_response = api_instance.video_comment_list_get(open_id, access_token, count, item_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoCommentApi->video_comment_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **item_id** | **str**| 视频id | 
 **cursor** | **int**| 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_comment_reply_list_get**
> InlineResponse200 video_comment_reply_list_get(open_id, access_token, count, item_id, comment_id, cursor=cursor)

评论回复列表

* Scope: `video.comment` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoCommentVideoComment
from douyin_open/VideoCommentVideoComment.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoCommentVideoComment.VideoCommentApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 56 # int | 每页数量
item_id = 'item_id_example' # str | 视频id
comment_id = 'comment_id_example' # str | 评论id
cursor = 56 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)

try:
    # 评论回复列表
    api_response = api_instance.video_comment_reply_list_get(open_id, access_token, count, item_id, comment_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoCommentApi->video_comment_reply_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **item_id** | **str**| 视频id | 
 **comment_id** | **str**| 评论id | 
 **cursor** | **int**| 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_comment_reply_post**
> CommonResponse video_comment_reply_post(open_id, access_token, body=body)

回复视频评论

* Scope: `video.comment` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoCommentVideoComment
from douyin_open/VideoCommentVideoComment.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoCommentVideoComment.VideoCommentApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin_open/VideoCommentVideoComment.Body() # Body |  (optional)

try:
    # 回复视频评论
    api_response = api_instance.video_comment_reply_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoCommentApi->video_comment_reply_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_comment_top_post**
> CommonResponse video_comment_top_post(open_id, access_token, body=body)

置顶视频评论(企业号)

* Scope: `video.comment` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoCommentVideoComment
from douyin_open/VideoCommentVideoComment.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoCommentVideoComment.VideoCommentApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin_open/VideoCommentVideoComment.Body1() # Body1 |  (optional)

try:
    # 置顶视频评论(企业号)
    api_response = api_instance.video_comment_top_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoCommentApi->video_comment_top_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

