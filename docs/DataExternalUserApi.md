# douyin_open/ExternalDataUserExternalDataUser.DataExternalUserApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_external_user_comment_get**](DataExternalUserApi.md#data_external_user_comment_get) | **GET** /data/external/user/comment/ | 获取用户评论数
[**data_external_user_fans_get**](DataExternalUserApi.md#data_external_user_fans_get) | **GET** /data/external/user/fans/ | 获取用户粉丝数
[**data_external_user_item_get**](DataExternalUserApi.md#data_external_user_item_get) | **GET** /data/external/user/item/ | 获取用户视频情况
[**data_external_user_like_get**](DataExternalUserApi.md#data_external_user_like_get) | **GET** /data/external/user/like/ | 获取用户点赞数
[**data_external_user_profile_get**](DataExternalUserApi.md#data_external_user_profile_get) | **GET** /data/external/user/profile/ | 获取用户主页访问数
[**data_external_user_share_get**](DataExternalUserApi.md#data_external_user_share_get) | **GET** /data/external/user/share/ | 获取用户分享数

# **data_external_user_comment_get**
> InlineResponse2003 data_external_user_comment_get(open_id, access_token, date_type)

获取用户评论数

* Scope: `data.external.user` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataUserExternalDataUser
from douyin_open/ExternalDataUserExternalDataUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataUserExternalDataUser.DataExternalUserApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
date_type = 56 # int | 近7/15天；输入7代表7天、15代表15天、30代表30天

try:
    # 获取用户评论数
    api_response = api_instance.data_external_user_comment_get(open_id, access_token, date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalUserApi->data_external_user_comment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **date_type** | **int**| 近7/15天；输入7代表7天、15代表15天、30代表30天 | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_external_user_fans_get**
> InlineResponse2001 data_external_user_fans_get(open_id, access_token, date_type)

获取用户粉丝数

* Scope: `data.external.user` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataUserExternalDataUser
from douyin_open/ExternalDataUserExternalDataUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataUserExternalDataUser.DataExternalUserApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
date_type = 56 # int | 近7/15天；输入7代表7天、15代表15天、30代表30天

try:
    # 获取用户粉丝数
    api_response = api_instance.data_external_user_fans_get(open_id, access_token, date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalUserApi->data_external_user_fans_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **date_type** | **int**| 近7/15天；输入7代表7天、15代表15天、30代表30天 | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_external_user_item_get**
> InlineResponse200 data_external_user_item_get(open_id, access_token, date_type)

获取用户视频情况

* Scope: `data.external.user` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataUserExternalDataUser
from douyin_open/ExternalDataUserExternalDataUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataUserExternalDataUser.DataExternalUserApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
date_type = 56 # int | 近7/15天；输入7代表7天、15代表15天、30代表30天

try:
    # 获取用户视频情况
    api_response = api_instance.data_external_user_item_get(open_id, access_token, date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalUserApi->data_external_user_item_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **date_type** | **int**| 近7/15天；输入7代表7天、15代表15天、30代表30天 | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_external_user_like_get**
> InlineResponse2002 data_external_user_like_get(open_id, access_token, date_type)

获取用户点赞数

* Scope: `data.external.user` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataUserExternalDataUser
from douyin_open/ExternalDataUserExternalDataUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataUserExternalDataUser.DataExternalUserApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
date_type = 56 # int | 近7/15天；输入7代表7天、15代表15天、30代表30天

try:
    # 获取用户点赞数
    api_response = api_instance.data_external_user_like_get(open_id, access_token, date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalUserApi->data_external_user_like_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **date_type** | **int**| 近7/15天；输入7代表7天、15代表15天、30代表30天 | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_external_user_profile_get**
> InlineResponse2005 data_external_user_profile_get(open_id, access_token, date_type)

获取用户主页访问数

* Scope: `data.external.user` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataUserExternalDataUser
from douyin_open/ExternalDataUserExternalDataUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataUserExternalDataUser.DataExternalUserApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
date_type = 56 # int | 近7/15天；输入7代表7天、15代表15天、30代表30天

try:
    # 获取用户主页访问数
    api_response = api_instance.data_external_user_profile_get(open_id, access_token, date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalUserApi->data_external_user_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **date_type** | **int**| 近7/15天；输入7代表7天、15代表15天、30代表30天 | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_external_user_share_get**
> InlineResponse2004 data_external_user_share_get(open_id, access_token, date_type)

获取用户分享数

* Scope: `data.external.user` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/ExternalDataUserExternalDataUser
from douyin_open/ExternalDataUserExternalDataUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ExternalDataUserExternalDataUser.DataExternalUserApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
date_type = 56 # int | 近7/15天；输入7代表7天、15代表15天、30代表30天

try:
    # 获取用户分享数
    api_response = api_instance.data_external_user_share_get(open_id, access_token, date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExternalUserApi->data_external_user_share_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **date_type** | **int**| 近7/15天；输入7代表7天、15代表15天、30代表30天 | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

