# douyin_open/ImageCreateImageCreate.ImageApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_create_post**](ImageApi.md#image_create_post) | **POST** /image/create/ | 发布图片
[**image_upload_post**](ImageApi.md#image_upload_post) | **POST** /image/upload/ | 上传图片到文件服务器

# **image_create_post**
> InlineResponse2001 image_create_post(open_id, access_token, body=body)

发布图片

* Scope: `video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ImageCreateImageCreate
from douyin_open/ImageCreateImageCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ImageCreateImageCreate.ImageApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin_open/ImageCreateImageCreate.Body1() # Body1 |  (optional)

try:
    # 发布图片
    api_response = api_instance.image_create_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->image_create_post: %s\n" % e)
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

# **image_upload_post**
> InlineResponse200 image_upload_post(image, open_id, access_token)

上传图片到文件服务器

* Scope: `video.create` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ImageCreateImageCreate
from douyin_open/ImageCreateImageCreate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ImageCreateImageCreate.ImageApi()
image = 'image_example' # str | 
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 上传图片到文件服务器
    api_response = api_instance.image_upload_post(image, open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->image_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **str**|  | 
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

