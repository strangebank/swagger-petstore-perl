# douyin_open/PoiOrderOrder.PoiOrderApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_ext_hotel_order_cancel_post**](PoiOrderApi.md#poi_ext_hotel_order_cancel_post) | **POST** /poi/ext/hotel/order/cancel/ | 取消订单(该接口由接入方实现)
[**poi_ext_hotel_order_commit_post**](PoiOrderApi.md#poi_ext_hotel_order_commit_post) | **POST** /poi/ext/hotel/order/commit/ | 下单接口(该接口由接入方实现)
[**poi_ext_hotel_order_status_post**](PoiOrderApi.md#poi_ext_hotel_order_status_post) | **POST** /poi/ext/hotel/order/status/ | 支付状态通知(该接口由接入方实现)
[**poi_order_status_post**](PoiOrderApi.md#poi_order_status_post) | **POST** /poi/order/status/ | 订单状态同步接口

# **poi_ext_hotel_order_cancel_post**
> InlineResponse2003 poi_ext_hotel_order_cancel_post(body=body)

取消订单(该接口由接入方实现)

# 该接口由接入方实现 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiOrderOrder
from douyin_open/PoiOrderOrder.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiOrderOrder.PoiOrderApi()
body = douyin_open/PoiOrderOrder.Body3() # Body3 |  (optional)

try:
    # 取消订单(该接口由接入方实现)
    api_response = api_instance.poi_ext_hotel_order_cancel_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiOrderApi->poi_ext_hotel_order_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_ext_hotel_order_commit_post**
> InlineResponse2001 poi_ext_hotel_order_commit_post(body=body)

下单接口(该接口由接入方实现)

# 该接口由接入方实现 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiOrderOrder
from douyin_open/PoiOrderOrder.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiOrderOrder.PoiOrderApi()
body = douyin_open/PoiOrderOrder.Body1() # Body1 |  (optional)

try:
    # 下单接口(该接口由接入方实现)
    api_response = api_instance.poi_ext_hotel_order_commit_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiOrderApi->poi_ext_hotel_order_commit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_ext_hotel_order_status_post**
> InlineResponse2002 poi_ext_hotel_order_status_post(body=body)

支付状态通知(该接口由接入方实现)

# 该接口由接入方实现 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiOrderOrder
from douyin_open/PoiOrderOrder.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiOrderOrder.PoiOrderApi()
body = douyin_open/PoiOrderOrder.Body2() # Body2 |  (optional)

try:
    # 支付状态通知(该接口由接入方实现)
    api_response = api_instance.poi_ext_hotel_order_status_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiOrderApi->poi_ext_hotel_order_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_order_status_post**
> InlineResponse200 poi_order_status_post(body, access_token)

订单状态同步接口

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiOrderOrder
from douyin_open/PoiOrderOrder.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiOrderOrder.PoiOrderApi()
body = douyin_open/PoiOrderOrder.Body() # Body | 
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 订单状态同步接口
    api_response = api_instance.poi_order_status_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiOrderApi->poi_order_status_post: %s\n" % e)
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

