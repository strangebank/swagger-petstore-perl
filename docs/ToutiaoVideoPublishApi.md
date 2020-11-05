# douyin_open/ToutiaoVideoCreateCreate.ToutiaoVideoPublishApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**toutiao_video_create_post**](ToutiaoVideoPublishApi.md#toutiao_video_create_post) | **POST** /toutiao/video/create/ | 创建头条视频
[**toutiao_video_part_complete_post**](ToutiaoVideoPublishApi.md#toutiao_video_part_complete_post) | **POST** /toutiao/video/part/complete/ | 完成上传
[**toutiao_video_part_init_post**](ToutiaoVideoPublishApi.md#toutiao_video_part_init_post) | **POST** /toutiao/video/part/init/ | 初始化上传
[**toutiao_video_part_upload_post**](ToutiaoVideoPublishApi.md#toutiao_video_part_upload_post) | **POST** /toutiao/video/part/upload/ | 上传视频分片到文件服务器
[**toutiao_video_upload_post**](ToutiaoVideoPublishApi.md#toutiao_video_upload_post) | **POST** /toutiao/video/upload/ | 上传视频到文件服务器

# **toutiao_video_create_post**
> InlineResponse2001 toutiao_video_create_post(open_id, access_token, body=body)

创建头条视频

* Scope: `toutiao.video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ToutiaoVideoCreateCreate
from douyin_open/ToutiaoVideoCreateCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ToutiaoVideoCreateCreate.ToutiaoVideoPublishApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin_open/ToutiaoVideoCreateCreate.Body1() # Body1 |  (optional)

try:
    # 创建头条视频
    api_response = api_instance.toutiao_video_create_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToutiaoVideoPublishApi->toutiao_video_create_post: %s\n" % e)
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

# **toutiao_video_part_complete_post**
> InlineResponse2004 toutiao_video_part_complete_post(open_id, access_token, upload_id)

完成上传

* Scope: `toutiao.video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ToutiaoVideoCreateCreate
from douyin_open/ToutiaoVideoCreateCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ToutiaoVideoCreateCreate.ToutiaoVideoPublishApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
upload_id = 'upload_id_example' # str | 分片上传的标记。有限时间为2小时。

try:
    # 完成上传
    api_response = api_instance.toutiao_video_part_complete_post(open_id, access_token, upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToutiaoVideoPublishApi->toutiao_video_part_complete_post: %s\n" % e)
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

# **toutiao_video_part_init_post**
> InlineResponse2002 toutiao_video_part_init_post(open_id, access_token)

初始化上传

* Scope: `toutiao.video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ToutiaoVideoCreateCreate
from douyin_open/ToutiaoVideoCreateCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ToutiaoVideoCreateCreate.ToutiaoVideoPublishApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 初始化上传
    api_response = api_instance.toutiao_video_part_init_post(open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToutiaoVideoPublishApi->toutiao_video_part_init_post: %s\n" % e)
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

# **toutiao_video_part_upload_post**
> InlineResponse2003 toutiao_video_part_upload_post(video, open_id, access_token, upload_id, part_number)

上传视频分片到文件服务器

* Scope: `toutiao.video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ToutiaoVideoCreateCreate
from douyin_open/ToutiaoVideoCreateCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ToutiaoVideoCreateCreate.ToutiaoVideoPublishApi()
video = 'video_example' # str | 
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
upload_id = 'upload_id_example' # str | 分片上传的标记。有限时间为2小时。
part_number = 56 # int | 第几个分片，从1开始 

try:
    # 上传视频分片到文件服务器
    api_response = api_instance.toutiao_video_part_upload_post(video, open_id, access_token, upload_id, part_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToutiaoVideoPublishApi->toutiao_video_part_upload_post: %s\n" % e)
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

# **toutiao_video_upload_post**
> InlineResponse200 toutiao_video_upload_post(video, open_id, access_token)

上传视频到文件服务器

* Scope: `toutiao.video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ToutiaoVideoCreateCreate
from douyin_open/ToutiaoVideoCreateCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ToutiaoVideoCreateCreate.ToutiaoVideoPublishApi()
video = 'video_example' # str | 
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 上传视频到文件服务器
    api_response = api_instance.toutiao_video_upload_post(video, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToutiaoVideoPublishApi->toutiao_video_upload_post: %s\n" % e)
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

