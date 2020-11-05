# douyin_open/StarAuthorStarAuthor.StarAuthorScoreApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**star_author_score_get**](StarAuthorScoreApi.md#star_author_score_get) | **GET** /star/author_score/ | 获取抖音星图达人指数
[**star_author_score_v2_get**](StarAuthorScoreApi.md#star_author_score_v2_get) | **GET** /star/author_score_v2/ | 获取抖音星图达人指数数据V2

# **star_author_score_get**
> InlineResponse200 star_author_score_get(open_id, access_token)

获取抖音星图达人指数

* Scope: `star_top_score_display` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/StarAuthorStarAuthor
from douyin_open/StarAuthorStarAuthor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/StarAuthorStarAuthor.StarAuthorScoreApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。

try:
    # 获取抖音星图达人指数
    api_response = api_instance.star_author_score_get(open_id, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StarAuthorScoreApi->star_author_score_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **star_author_score_v2_get**
> InlineResponse2001 star_author_score_v2_get(access_token, unique_id)

获取抖音星图达人指数数据V2

* Scope: `star_author_score_display` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/StarAuthorStarAuthor
from douyin_open/StarAuthorStarAuthor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/StarAuthorStarAuthor.StarAuthorScoreApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
unique_id = 'unique_id_example' # str | 达人抖音号

try:
    # 获取抖音星图达人指数数据V2
    api_response = api_instance.star_author_score_v2_get(access_token, unique_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StarAuthorScoreApi->star_author_score_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **unique_id** | **str**| 达人抖音号 | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

