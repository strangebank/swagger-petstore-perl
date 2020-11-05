# douyin_open/PoiProductProduct.PoiSkuApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_ext_hotel_sku_get**](PoiSkuApi.md#poi_ext_hotel_sku_get) | **GET** /poi/ext/hotel/sku/ | sku拉取(该接口由接入方实现)

# **poi_ext_hotel_sku_get**
> InlineResponse2003 poi_ext_hotel_sku_get(spu_ext_id, start_date, end_date)

sku拉取(该接口由接入方实现)

# 该接口由接入方实现 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiProductProduct
from douyin_open/PoiProductProduct.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiProductProduct.PoiSkuApi()
spu_ext_id = ['spu_ext_id_example'] # list[str] | 接入方SPU ID 列表
start_date = 'start_date_example' # str | 拉取价格时间区间[start_date, end_date)
end_date = 'end_date_example' # str | 拉取价格时间区间[start_date, end_date)

try:
    # sku拉取(该接口由接入方实现)
    api_response = api_instance.poi_ext_hotel_sku_get(spu_ext_id, start_date, end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSkuApi->poi_ext_hotel_sku_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spu_ext_id** | [**list[str]**](str.md)| 接入方SPU ID 列表 | 
 **start_date** | **str**| 拉取价格时间区间[start_date, end_date) | 
 **end_date** | **str**| 拉取价格时间区间[start_date, end_date) | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

