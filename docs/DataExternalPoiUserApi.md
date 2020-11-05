# douyin_open/ExternalDataPoiExternalDataPoi.DataExternalPoiUserApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_external_poi_user_get**](DataExternalPoiUserApi.md#data_external_poi_user_get) | **GET** /data/external/poi/user/ | POI用户数据

# **data_external_poi_user_get**
> InlineResponse2001 data_external_poi_user_get(access_token, poi_id, date_type)

POI用户数据

* Scope: `data.external.poi` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataPoiExternalDataPoi
from douyin_open/ExternalDataPoiExternalDataPoi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataPoiExternalDataPoi.DataExternalPoiUserApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
poi_id = 'poi_id_example' # str | 抖音poi_id
date_type = 56 # int | 近7/15/30天

try:
    # POI用户数据
    api_response = api_instance.data_external_poi_user_get(access_token, poi_id, date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalPoiUserApi->data_external_poi_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **poi_id** | **str**| 抖音poi_id | 
 **date_type** | **int**| 近7/15/30天 | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

