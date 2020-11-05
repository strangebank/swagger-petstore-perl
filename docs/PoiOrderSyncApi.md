# douyin_open/PoiOrderSyncOrderSync.PoiOrderSyncApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_order_sync_post**](PoiOrderSyncApi.md#poi_order_sync_post) | **POST** /poi/order/sync/ | 订单同步

# **poi_order_sync_post**
> InlineResponse200 poi_order_sync_post(body, access_token)

订单同步

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiOrderSyncOrderSync
from douyin_open/PoiOrderSyncOrderSync.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiOrderSyncOrderSync.PoiOrderSyncApi()
body = douyin_open/PoiOrderSyncOrderSync.Body() # Body | 
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 订单同步
    api_response = api_instance.poi_order_sync_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiOrderSyncApi->poi_order_sync_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

