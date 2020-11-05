# douyin_open/DiscoveryEntRankRank.DiscoveryApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discovery_ent_rank_item_get**](DiscoveryApi.md#discovery_ent_rank_item_get) | **GET** /discovery/ent/rank/item/ | 获取抖音电影榜、抖音电视剧榜、抖音综艺榜
[**discovery_ent_rank_version_get**](DiscoveryApi.md#discovery_ent_rank_version_get) | **GET** /discovery/ent/rank/version/ | 获取抖音影视综榜单版本

# **discovery_ent_rank_item_get**
> InlineResponse200 discovery_ent_rank_item_get(access_token, type, version=version)

获取抖音电影榜、抖音电视剧榜、抖音综艺榜

* Scope: `discovery.ent` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/DiscoveryEntRankRank
from douyin_open/DiscoveryEntRankRank.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/DiscoveryEntRankRank.DiscoveryApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
type = 56 # int | 榜单类型：   * 1 - 电影    * 2 - 电视剧    * 3 - 综艺 
version = 56 # int | 榜单版本：空值默认为本周榜单 (optional)

try:
    # 获取抖音电影榜、抖音电视剧榜、抖音综艺榜
    api_response = api_instance.discovery_ent_rank_item_get(access_token, type, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->discovery_ent_rank_item_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **type** | **int**| 榜单类型：   * 1 - 电影    * 2 - 电视剧    * 3 - 综艺  | 
 **version** | **int**| 榜单版本：空值默认为本周榜单 | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_ent_rank_version_get**
> InlineResponse2001 discovery_ent_rank_version_get(access_token, count, type, cursor=cursor)

获取抖音影视综榜单版本

* Scope: `discovery.ent` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/DiscoveryEntRankRank
from douyin_open/DiscoveryEntRankRank.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/DiscoveryEntRankRank.DiscoveryApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
count = 56 # int | 每页数量
type = 56 # int | 榜单类型：   * 1 - 电影    * 2 - 电视剧    * 3 - 综艺 
cursor = 56 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)

try:
    # 获取抖音影视综榜单版本
    api_response = api_instance.discovery_ent_rank_version_get(access_token, count, type, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->discovery_ent_rank_version_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **type** | **int**| 榜单类型：   * 1 - 电影    * 2 - 电视剧    * 3 - 综艺  | 
 **cursor** | **int**| 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

