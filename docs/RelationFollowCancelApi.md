# douyin_open/RelationRelationFollow.RelationFollowCancelApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**relation_following_cancel_post**](RelationFollowCancelApi.md#relation_following_cancel_post) | **POST** /relation/following/cancel/ | 取消关注指定抖音号

# **relation_following_cancel_post**
> CommonResponse relation_following_cancel_post(open_id, access_token)

取消关注指定抖音号

* Scope: `relation.follow` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/RelationRelationFollow
from douyin_open/RelationRelationFollow.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/RelationRelationFollow.RelationFollowCancelApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 取消关注指定抖音号
    api_response = api_instance.relation_following_cancel_post(open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationFollowCancelApi->relation_following_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

