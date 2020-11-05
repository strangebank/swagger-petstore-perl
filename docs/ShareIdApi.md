# douyin_open/ShareIdShareId.ShareIdApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**share_id_get**](ShareIdApi.md#share_id_get) | **GET** /share-id/ | 获取share-id

# **share_id_get**
> InlineResponse200 share_id_get(access_token, need_callback=need_callback, source_style_id=source_style_id, default_hashtag=default_hashtag, link_param=link_param)

获取share-id

* Scope: `aweme.share` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ShareIdShareId
from douyin_open/ShareIdShareId.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ShareIdShareId.ShareIdApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
need_callback = true # bool | 如果需要知道视频分享成功的结果，need_callback设置为true (optional)
source_style_id = 'source_style_id_example' # str | 多来源样式id（暂未开放） (optional)
default_hashtag = 'default_hashtag_example' # str | 追踪分享默认hashtag (optional)
link_param = 'link_param_example' # str | 分享来源url附加参数（暂未开放） (optional)

try:
    # 获取share-id
    api_response = api_instance.share_id_get(access_token, need_callback=need_callback, source_style_id=source_style_id, default_hashtag=default_hashtag, link_param=link_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShareIdApi->share_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **need_callback** | **bool**| 如果需要知道视频分享成功的结果，need_callback设置为true | [optional] 
 **source_style_id** | **str**| 多来源样式id（暂未开放） | [optional] 
 **default_hashtag** | **str**| 追踪分享默认hashtag | [optional] 
 **link_param** | **str**| 分享来源url附加参数（暂未开放） | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

