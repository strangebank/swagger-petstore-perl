# douyin_open/ExternalDataSdkShareExternalDataSdkShare.DataShareSdkShareApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_external_sdk_share_get**](DataShareSdkShareApi.md#data_external_sdk_share_get) | **GET** /data/external/sdk_share/ | 获取SDK分享视频数据

# **data_external_sdk_share_get**
> InlineResponse200 data_external_sdk_share_get(access_token, begin_date, end_date)

获取SDK分享视频数据

* Scope: `data.external.sdk_share` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataSdkShareExternalDataSdkShare
from douyin_open/ExternalDataSdkShareExternalDataSdkShare.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataSdkShareExternalDataSdkShare.DataShareSdkShareApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
begin_date = 'begin_date_example' # str | 最近30天，开始日期(yyyy-MM-dd)
end_date = 'end_date_example' # str | 最近30天，结束日期(yyyy-MM-dd)

try:
    # 获取SDK分享视频数据
    api_response = api_instance.data_external_sdk_share_get(access_token, begin_date, end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataShareSdkShareApi->data_external_sdk_share_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **begin_date** | **str**| 最近30天，开始日期(yyyy-MM-dd) | 
 **end_date** | **str**| 最近30天，结束日期(yyyy-MM-dd) | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

