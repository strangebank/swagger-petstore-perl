# douyin_open/VideoPoiVideoPoi.PoiSearchApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_search_keyword_get**](PoiSearchApi.md#poi_search_keyword_get) | **GET** /poi/search/keyword/ | 查询POI信息

# **poi_search_keyword_get**
> InlineResponse200 poi_search_keyword_get(access_token, count, keyword, cursor=cursor, city=city)

查询POI信息

* Scope: `poi.search` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/VideoPoiVideoPoi
from douyin_open/VideoPoiVideoPoi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/VideoPoiVideoPoi.PoiSearchApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
count = 56 # int | 每页数量
keyword = 'keyword_example' # str | 查询关键字，例如美食
cursor = 56 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)
city = 'city_example' # str | 查询城市，例如上海、北京 (optional)

try:
    # 查询POI信息
    api_response = api_instance.poi_search_keyword_get(access_token, count, keyword, cursor=cursor, city=city)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSearchApi->poi_search_keyword_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **keyword** | **str**| 查询关键字，例如美食 | 
 **cursor** | **int**| 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 | [optional] 
 **city** | **str**| 查询城市，例如上海、北京 | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

