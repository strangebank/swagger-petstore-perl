# douyin_open/ExternalDataPoiExternalDataPoi.DataExternalPoiClaimListApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_external_poi_claim_list_get**](DataExternalPoiClaimListApi.md#data_external_poi_claim_list_get) | **GET** /data/external/poi/claim/list/ | POI认领列表

# **data_external_poi_claim_list_get**
> InlineResponse2004 data_external_poi_claim_list_get(access_token, open_id, count, cursor=cursor)

POI认领列表

* Scope: `data.external.poi` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataPoiExternalDataPoi
from douyin_open/ExternalDataPoiExternalDataPoi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataPoiExternalDataPoi.DataExternalPoiClaimListApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
count = 56 # int | 每页数量
cursor = 56 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)

try:
    # POI认领列表
    api_response = api_instance.data_external_poi_claim_list_get(access_token, open_id, count, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalPoiClaimListApi->data_external_poi_claim_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **count** | **int**| 每页数量 | 
 **cursor** | **int**| 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

