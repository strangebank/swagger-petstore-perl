# douyin_open/PoiBaseBase.PoiBaseApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_base_query_amap_get**](PoiBaseApi.md#poi_base_query_amap_get) | **GET** /poi/base/query/amap/ | 通过高德POI ID获取抖音POI ID

# **poi_base_query_amap_get**
> InlineResponse200 poi_base_query_amap_get(access_token, amap_id)

通过高德POI ID获取抖音POI ID

* Scope: `poi.base` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiBaseBase
from douyin_open/PoiBaseBase.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiBaseBase.PoiBaseApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
amap_id = 'amap_id_example' # str | 高德POI ID

try:
    # 通过高德POI ID获取抖音POI ID
    api_response = api_instance.poi_base_query_amap_get(access_token, amap_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiBaseApi->poi_base_query_amap_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **amap_id** | **str**| 高德POI ID | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

