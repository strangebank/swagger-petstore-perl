# douyin_open/EnterpriseGrouponGrouponOrderOrderOverview.EnterpriseGrouponOrderOverviewApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_groupon_order_overview_get**](EnterpriseGrouponOrderOverviewApi.md#enterprise_groupon_order_overview_get) | **GET** /enterprise/groupon/order/overview/ | 团购活动订单汇总信息

# **enterprise_groupon_order_overview_get**
> InlineResponse200 enterprise_groupon_order_overview_get(access_token, open_id, start_time, end_time)

团购活动订单汇总信息

* Scope: `enterprise.groupon` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseGrouponGrouponOrderOrderOverview
from douyin_open/EnterpriseGrouponGrouponOrderOrderOverview.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseGrouponGrouponOrderOrderOverview.EnterpriseGrouponOrderOverviewApi()
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
start_time = 56 # int | 订单开始时间，unix时间戳
end_time = 56 # int | 订单结束时间，unix时间戳

try:
    # 团购活动订单汇总信息
    api_response = api_instance.enterprise_groupon_order_overview_get(access_token, open_id, start_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseGrouponOrderOverviewApi->enterprise_groupon_order_overview_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **start_time** | **int**| 订单开始时间，unix时间戳 | 
 **end_time** | **int**| 订单结束时间，unix时间戳 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

