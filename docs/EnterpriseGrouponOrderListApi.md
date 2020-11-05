# douyin_open/EnterpriseGrouponGrouponOrderOrderList.EnterpriseGrouponOrderListApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_groupon_order_list_get**](EnterpriseGrouponOrderListApi.md#enterprise_groupon_order_list_get) | **GET** /enterprise/groupon/order/list/ | 团购活动订单详情

# **enterprise_groupon_order_list_get**
> InlineResponse200 enterprise_groupon_order_list_get(access_token, open_id, count, start_time, end_time, cursor=cursor, filter_status=filter_status)

团购活动订单详情

* Scope: `enterprise.groupon` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseGrouponGrouponOrderOrderList
from douyin_open/EnterpriseGrouponGrouponOrderOrderList.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseGrouponGrouponOrderOrderList.EnterpriseGrouponOrderListApi()
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
count = 56 # int | 每页数量
start_time = 56 # int | 订单创建开始时间，unix时间戳
end_time = 56 # int | 订单创建结束时间，unix时间戳
cursor = 56 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)
filter_status = 'filter_status_example' # str | 过滤订单状态，用\",\"分隔，不传默认下发所有状态 (optional)

try:
    # 团购活动订单详情
    api_response = api_instance.enterprise_groupon_order_list_get(access_token, open_id, count, start_time, end_time, cursor=cursor, filter_status=filter_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseGrouponOrderListApi->enterprise_groupon_order_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **count** | **int**| 每页数量 | 
 **start_time** | **int**| 订单创建开始时间，unix时间戳 | 
 **end_time** | **int**| 订单创建结束时间，unix时间戳 | 
 **cursor** | **int**| 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 | [optional] 
 **filter_status** | **str**| 过滤订单状态，用\&quot;,\&quot;分隔，不传默认下发所有状态 | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

