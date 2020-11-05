# douyin_open/ExternalDataPoiExternalDataPoi.DataExternalPoiServiceBaseApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_external_poi_service_base_get**](DataExternalPoiServiceBaseApi.md#data_external_poi_service_base_get) | **GET** /data/external/poi/service_base/ | POI服务基础数据

# **data_external_poi_service_base_get**
> InlineResponse2002 data_external_poi_service_base_get(access_token, poi_id, begin_date, end_date, service_type=service_type)

POI服务基础数据

* Scope: `data.external.poi` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataPoiExternalDataPoi
from douyin_open/ExternalDataPoiExternalDataPoi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataPoiExternalDataPoi.DataExternalPoiServiceBaseApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
poi_id = 'poi_id_example' # str | 抖音poi_id
begin_date = 'begin_date_example' # str | 最近30天，开始日期(yyyy-MM-dd)
end_date = 'end_date_example' # str | 最近30天，结束日期(yyyy-MM-dd)
service_type = 56 # int | 服务类型，40:民宿 (optional)

try:
    # POI服务基础数据
    api_response = api_instance.data_external_poi_service_base_get(access_token, poi_id, begin_date, end_date, service_type=service_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalPoiServiceBaseApi->data_external_poi_service_base_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **poi_id** | **str**| 抖音poi_id | 
 **begin_date** | **str**| 最近30天，开始日期(yyyy-MM-dd) | 
 **end_date** | **str**| 最近30天，结束日期(yyyy-MM-dd) | 
 **service_type** | **int**| 服务类型，40:民宿 | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

