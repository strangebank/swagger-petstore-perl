# douyin_open/EnterpriseGrouponGrouponGrouponList.EnterpriseGrouponListApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_groupon_list_get**](EnterpriseGrouponListApi.md#enterprise_groupon_list_get) | **GET** /enterprise/groupon/list/ | 团购活动列表

# **enterprise_groupon_list_get**
> InlineResponse200 enterprise_groupon_list_get(access_token, open_id, count, cursor=cursor, status=status)

团购活动列表

* Scope: `enterprise.groupon` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseGrouponGrouponGrouponList
from douyin_open/EnterpriseGrouponGrouponGrouponList.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseGrouponGrouponGrouponList.EnterpriseGrouponListApi()
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
count = 56 # int | 每页数量
cursor = 56 # int | 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 (optional)
status = 56 # int | * 状态筛选   * 1: 有效   * 2: 审核中   * 3: 审核失败   * 4: 中止  (optional)

try:
    # 团购活动列表
    api_response = api_instance.enterprise_groupon_list_get(access_token, open_id, count, cursor=cursor, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseGrouponListApi->enterprise_groupon_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **count** | **int**| 每页数量 | 
 **cursor** | **int**| 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。 | [optional] 
 **status** | **int**| * 状态筛选   * 1: 有效   * 2: 审核中   * 3: 审核失败   * 4: 中止  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

