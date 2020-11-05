# douyin_open/ExternalDataPoiExternalDataPoi.DataExternalPoiBillboardApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_external_poi_billboard_get**](DataExternalPoiBillboardApi.md#data_external_poi_billboard_get) | **GET** /data/external/poi/billboard/ | POI热度榜

# **data_external_poi_billboard_get**
> InlineResponse2003 data_external_poi_billboard_get(access_token, billboard_type)

POI热度榜

* Scope: `data.external.poi` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataPoiExternalDataPoi
from douyin_open/ExternalDataPoiExternalDataPoi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataPoiExternalDataPoi.DataExternalPoiBillboardApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
billboard_type = 56 # int | 10：近30日餐饮类POI的热度TOP500；20：近30日景点类POI的热度TOP500；30：近30日住宿类POI的热度TOP500

try:
    # POI热度榜
    api_response = api_instance.data_external_poi_billboard_get(access_token, billboard_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalPoiBillboardApi->data_external_poi_billboard_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **billboard_type** | **int**| 10：近30日餐饮类POI的热度TOP500；20：近30日景点类POI的热度TOP500；30：近30日住宿类POI的热度TOP500 | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

