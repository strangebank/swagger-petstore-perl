# douyin_open/UserFollowingFollowing.FollowingListApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**following_list_get**](FollowingListApi.md#following_list_get) | **GET** /following/list/ | 获取关注列表

# **following_list_get**
> InlineResponse200 following_list_get(open_id, access_token, count, cursor=cursor)

获取关注列表

* Scope: `following.list` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/UserFollowingFollowing
from douyin_open/UserFollowingFollowing.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/UserFollowingFollowing.FollowingListApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 56 # int | 每页数量
cursor = 56 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)

try:
    # 获取关注列表
    api_response = api_instance.following_list_get(open_id, access_token, count, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FollowingListApi->following_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **cursor** | **int**| 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

