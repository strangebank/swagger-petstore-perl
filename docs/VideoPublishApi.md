# douyin_open/VideoCreateAwemeCreate.VideoPublishApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_create_post**](VideoPublishApi.md#video_create_post) | **POST** /video/create/ | 创建抖音视频
[**video_part_complete_post**](VideoPublishApi.md#video_part_complete_post) | **POST** /video/part/complete/ | 完成上传
[**video_part_init_post**](VideoPublishApi.md#video_part_init_post) | **POST** /video/part/init/ | 初始化上传
[**video_part_upload_post**](VideoPublishApi.md#video_part_upload_post) | **POST** /video/part/upload/ | 上传视频分片到文件服务器
[**video_upload_post**](VideoPublishApi.md#video_upload_post) | **POST** /video/upload/ | 上传视频到文件服务器

# **video_create_post**
> InlineResponse2001 video_create_post(open_id, access_token, body=body)

创建抖音视频

* Scope: `video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoCreateAwemeCreate
from douyin_open/VideoCreateAwemeCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoCreateAwemeCreate.VideoPublishApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin_open/VideoCreateAwemeCreate.Body1() # Body1 |  (optional)

try:
    # 创建抖音视频
    api_response = api_instance.video_create_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoPublishApi->video_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_part_complete_post**
> InlineResponse2004 video_part_complete_post(open_id, access_token, upload_id)

完成上传

* Scope: `video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoCreateAwemeCreate
from douyin_open/VideoCreateAwemeCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoCreateAwemeCreate.VideoPublishApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
upload_id = 'upload_id_example' # str | 分片上传的标记。有限时间为2小时。

try:
    # 完成上传
    api_response = api_instance.video_part_complete_post(open_id, access_token, upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoPublishApi->video_part_complete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **upload_id** | **str**| 分片上传的标记。有限时间为2小时。 | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_part_init_post**
> InlineResponse2002 video_part_init_post(open_id, access_token)

初始化上传

* Scope: `video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoCreateAwemeCreate
from douyin_open/VideoCreateAwemeCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoCreateAwemeCreate.VideoPublishApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 初始化上传
    api_response = api_instance.video_part_init_post(open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoPublishApi->video_part_init_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_part_upload_post**
> InlineResponse2003 video_part_upload_post(video, open_id, access_token, upload_id, part_number)

上传视频分片到文件服务器

* Scope: `video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoCreateAwemeCreate
from douyin_open/VideoCreateAwemeCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoCreateAwemeCreate.VideoPublishApi()
video = 'video_example' # str | 
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
upload_id = 'upload_id_example' # str | 分片上传的标记。有限时间为2小时。
part_number = 56 # int | 第几个分片，从1开始 

try:
    # 上传视频分片到文件服务器
    api_response = api_instance.video_part_upload_post(video, open_id, access_token, upload_id, part_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoPublishApi->video_part_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video** | **str**|  | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **upload_id** | **str**| 分片上传的标记。有限时间为2小时。 | 
 **part_number** | **int**| 第几个分片，从1开始  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_upload_post**
> InlineResponse200 video_upload_post(video, open_id, access_token)

上传视频到文件服务器

* Scope: `video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoCreateAwemeCreate
from douyin_open/VideoCreateAwemeCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoCreateAwemeCreate.VideoPublishApi()
video = 'video_example' # str | 
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 上传视频到文件服务器
    api_response = api_instance.video_upload_post(video, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoPublishApi->video_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video** | **str**|  | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

