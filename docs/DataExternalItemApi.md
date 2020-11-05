# douyin_open/ExternalDataItemExternalDataItem.DataExternalItemApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_external_item_base_get**](DataExternalItemApi.md#data_external_item_base_get) | **GET** /data/external/item/base/ | 获取视频基础数据
[**data_external_item_comment_get**](DataExternalItemApi.md#data_external_item_comment_get) | **GET** /data/external/item/comment/ | 获取视频评论数据
[**data_external_item_like_get**](DataExternalItemApi.md#data_external_item_like_get) | **GET** /data/external/item/like/ | 获取视频点赞数据
[**data_external_item_play_get**](DataExternalItemApi.md#data_external_item_play_get) | **GET** /data/external/item/play/ | 获取视频播放数据
[**data_external_item_share_get**](DataExternalItemApi.md#data_external_item_share_get) | **GET** /data/external/item/share/ | 获取视频分享数据

# **data_external_item_base_get**
> InlineResponse200 data_external_item_base_get(open_id, access_token, item_id)

获取视频基础数据

* Scope: `data.external.item` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataItemExternalDataItem
from douyin_open/ExternalDataItemExternalDataItem.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataItemExternalDataItem.DataExternalItemApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
item_id = 'item_id_example' # str | item_id，仅能查询access_token对应用户上传的视频

try:
    # 获取视频基础数据
    api_response = api_instance.data_external_item_base_get(open_id, access_token, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalItemApi->data_external_item_base_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **item_id** | **str**| item_id，仅能查询access_token对应用户上传的视频 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_external_item_comment_get**
> InlineResponse2002 data_external_item_comment_get(open_id, access_token, item_id, date_type)

获取视频评论数据

* Scope: `data.external.item` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataItemExternalDataItem
from douyin_open/ExternalDataItemExternalDataItem.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataItemExternalDataItem.DataExternalItemApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
item_id = 'item_id_example' # str | item_id，仅能查询access_token对应用户上传的视频
date_type = 56 # int | 近7/15天；输入7代表7天、15代表15天

try:
    # 获取视频评论数据
    api_response = api_instance.data_external_item_comment_get(open_id, access_token, item_id, date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalItemApi->data_external_item_comment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **item_id** | **str**| item_id，仅能查询access_token对应用户上传的视频 | 
 **date_type** | **int**| 近7/15天；输入7代表7天、15代表15天 | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_external_item_like_get**
> InlineResponse2001 data_external_item_like_get(open_id, access_token, item_id, date_type)

获取视频点赞数据

* Scope: `data.external.item` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataItemExternalDataItem
from douyin_open/ExternalDataItemExternalDataItem.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataItemExternalDataItem.DataExternalItemApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
item_id = 'item_id_example' # str | item_id，仅能查询access_token对应用户上传的视频
date_type = 56 # int | 近7/15天；输入7代表7天、15代表15天

try:
    # 获取视频点赞数据
    api_response = api_instance.data_external_item_like_get(open_id, access_token, item_id, date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalItemApi->data_external_item_like_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **item_id** | **str**| item_id，仅能查询access_token对应用户上传的视频 | 
 **date_type** | **int**| 近7/15天；输入7代表7天、15代表15天 | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_external_item_play_get**
> InlineResponse2003 data_external_item_play_get(open_id, access_token, item_id, date_type)

获取视频播放数据

* Scope: `data.external.item` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataItemExternalDataItem
from douyin_open/ExternalDataItemExternalDataItem.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataItemExternalDataItem.DataExternalItemApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
item_id = 'item_id_example' # str | item_id，仅能查询access_token对应用户上传的视频
date_type = 56 # int | 近7/15天；输入7代表7天、15代表15天

try:
    # 获取视频播放数据
    api_response = api_instance.data_external_item_play_get(open_id, access_token, item_id, date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalItemApi->data_external_item_play_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **item_id** | **str**| item_id，仅能查询access_token对应用户上传的视频 | 
 **date_type** | **int**| 近7/15天；输入7代表7天、15代表15天 | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_external_item_share_get**
> InlineResponse2004 data_external_item_share_get(open_id, access_token, item_id, date_type)

获取视频分享数据

* Scope: `data.external.item` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataItemExternalDataItem
from douyin_open/ExternalDataItemExternalDataItem.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataItemExternalDataItem.DataExternalItemApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
item_id = 'item_id_example' # str | item_id，仅能查询access_token对应用户上传的视频
date_type = 56 # int | 近7/15天；输入7代表7天、15代表15天

try:
    # 获取视频分享数据
    api_response = api_instance.data_external_item_share_get(open_id, access_token, item_id, date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalItemApi->data_external_item_share_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **item_id** | **str**| item_id，仅能查询access_token对应用户上传的视频 | 
 **date_type** | **int**| 近7/15天；输入7代表7天、15代表15天 | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

