# douyin_open/EnterpriseLeadsLeadsUser.EnterpriseLeadsApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_leads_tag_create_post**](EnterpriseLeadsApi.md#enterprise_leads_tag_create_post) | **POST** /enterprise/leads/tag/create/ | 创建标签
[**enterprise_leads_tag_delete_post**](EnterpriseLeadsApi.md#enterprise_leads_tag_delete_post) | **POST** /enterprise/leads/tag/delete/ | 删除标签
[**enterprise_leads_tag_list_get**](EnterpriseLeadsApi.md#enterprise_leads_tag_list_get) | **GET** /enterprise/leads/tag/list/ | 获取标签列表
[**enterprise_leads_tag_update_post**](EnterpriseLeadsApi.md#enterprise_leads_tag_update_post) | **POST** /enterprise/leads/tag/update/ | 编辑标签
[**enterprise_leads_tag_user_list_get**](EnterpriseLeadsApi.md#enterprise_leads_tag_user_list_get) | **GET** /enterprise/leads/tag/user/list/ | 获取打标签的用户列表
[**enterprise_leads_tag_user_update_post**](EnterpriseLeadsApi.md#enterprise_leads_tag_user_update_post) | **POST** /enterprise/leads/tag/user/update/ | 给用户设置标签
[**enterprise_leads_user_action_list_get**](EnterpriseLeadsApi.md#enterprise_leads_user_action_list_get) | **GET** /enterprise/leads/user/action/list/ | 获取意向用户互动记录
[**enterprise_leads_user_detail_get**](EnterpriseLeadsApi.md#enterprise_leads_user_detail_get) | **GET** /enterprise/leads/user/detail/ | 获取意向用户详情
[**enterprise_leads_user_list_get**](EnterpriseLeadsApi.md#enterprise_leads_user_list_get) | **GET** /enterprise/leads/user/list/ | 获取意向用户列表

# **enterprise_leads_tag_create_post**
> InlineResponse2005 enterprise_leads_tag_create_post(open_id, access_token, body=body)

创建标签

* Scope: `enterprise.data` * 一个企业号最多创建100个标签 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseLeadsLeadsUser
from douyin_open/EnterpriseLeadsLeadsUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseLeadsLeadsUser.EnterpriseLeadsApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin_open/EnterpriseLeadsLeadsUser.Body() # Body |  (optional)

try:
    # 创建标签
    api_response = api_instance.enterprise_leads_tag_create_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_tag_delete_post**
> InlineResponse2006 enterprise_leads_tag_delete_post(open_id, access_token, body=body)

删除标签

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseLeadsLeadsUser
from douyin_open/EnterpriseLeadsLeadsUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseLeadsLeadsUser.EnterpriseLeadsApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin_open/EnterpriseLeadsLeadsUser.Body2() # Body2 |  (optional)

try:
    # 删除标签
    api_response = api_instance.enterprise_leads_tag_delete_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_tag_list_get**
> InlineResponse2003 enterprise_leads_tag_list_get(open_id, access_token, count, cursor=cursor)

获取标签列表

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseLeadsLeadsUser
from douyin_open/EnterpriseLeadsLeadsUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseLeadsLeadsUser.EnterpriseLeadsApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 56 # int | 每页数量
cursor = 1 # int | 分页游标 (optional) (default to 1)

try:
    # 获取标签列表
    api_response = api_instance.enterprise_leads_tag_list_get(open_id, access_token, count, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **cursor** | **int**| 分页游标 | [optional] [default to 1]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_tag_update_post**
> InlineResponse2005 enterprise_leads_tag_update_post(open_id, access_token, body=body)

编辑标签

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseLeadsLeadsUser
from douyin_open/EnterpriseLeadsLeadsUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseLeadsLeadsUser.EnterpriseLeadsApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin_open/EnterpriseLeadsLeadsUser.Body1() # Body1 |  (optional)

try:
    # 编辑标签
    api_response = api_instance.enterprise_leads_tag_update_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_tag_user_list_get**
> InlineResponse2004 enterprise_leads_tag_user_list_get(open_id, access_token, count, tag_id, cursor=cursor)

获取打标签的用户列表

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseLeadsLeadsUser
from douyin_open/EnterpriseLeadsLeadsUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseLeadsLeadsUser.EnterpriseLeadsApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 56 # int | 每页数量
tag_id = 56 # int | 
cursor = 1 # int | 分页游标 (optional) (default to 1)

try:
    # 获取打标签的用户列表
    api_response = api_instance.enterprise_leads_tag_user_list_get(open_id, access_token, count, tag_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_user_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **tag_id** | **int**|  | 
 **cursor** | **int**| 分页游标 | [optional] [default to 1]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_tag_user_update_post**
> InlineResponse2006 enterprise_leads_tag_user_update_post(open_id, access_token, body=body)

给用户设置标签

* Scope: `enterprise.data` * 一个用户最多设置5个标签 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseLeadsLeadsUser
from douyin_open/EnterpriseLeadsLeadsUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseLeadsLeadsUser.EnterpriseLeadsApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin_open/EnterpriseLeadsLeadsUser.Body3() # Body3 |  (optional)

try:
    # 给用户设置标签
    api_response = api_instance.enterprise_leads_tag_user_update_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_tag_user_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_user_action_list_get**
> InlineResponse2002 enterprise_leads_user_action_list_get(open_id, access_token, count, user_id, cursor=cursor, action_type=action_type)

获取意向用户互动记录

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseLeadsLeadsUser
from douyin_open/EnterpriseLeadsLeadsUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseLeadsLeadsUser.EnterpriseLeadsApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 56 # int | 每页数量
user_id = 'user_id_example' # str | 
cursor = 'cursor_example' # str |  (optional)
action_type = 56 # int |  (optional)

try:
    # 获取意向用户互动记录
    api_response = api_instance.enterprise_leads_user_action_list_get(open_id, access_token, count, user_id, cursor=cursor, action_type=action_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_user_action_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **user_id** | **str**|  | 
 **cursor** | **str**|  | [optional] 
 **action_type** | **int**|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_user_detail_get**
> InlineResponse2001 enterprise_leads_user_detail_get(open_id, access_token, user_id)

获取意向用户详情

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseLeadsLeadsUser
from douyin_open/EnterpriseLeadsLeadsUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseLeadsLeadsUser.EnterpriseLeadsApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
user_id = 'user_id_example' # str | 

try:
    # 获取意向用户详情
    api_response = api_instance.enterprise_leads_user_detail_get(open_id, access_token, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_user_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **user_id** | **str**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_leads_user_list_get**
> InlineResponse200 enterprise_leads_user_list_get(open_id, access_token, count, start_time, end_time, action_type, cursor=cursor, leads_level=leads_level)

获取意向用户列表

* Scope: `enterprise.data` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/EnterpriseLeadsLeadsUser
from douyin_open/EnterpriseLeadsLeadsUser.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/EnterpriseLeadsLeadsUser.EnterpriseLeadsApi()
open_id = 'open_id_example' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'access_token_example' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
count = 56 # int | 每页数量
start_time = 56 # int | 
end_time = 56 # int | 
action_type = 56 # int | 分类:   * `0` - 全部   * `1` - 私信互动   * `2` - 组件互动   * `3` - 主页互动 
cursor = 1 # int | 分页游标 (optional) (default to 1)
leads_level = 56 # int | 用户状态:   * `-1` - 没兴趣   * `0` - 了解   * `1` - 有兴趣   * `2` - 有意愿   * `10` - 已转化  (optional)

try:
    # 获取意向用户列表
    api_response = api_instance.enterprise_leads_user_list_get(open_id, access_token, count, start_time, end_time, action_type, cursor=cursor, leads_level=leads_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseLeadsApi->enterprise_leads_user_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_id** | **str**| 通过/oauth/access_token/获取，用户唯一标志 | 
 **access_token** | **str**| 调用/oauth/access_token/生成的token，此token需要用户授权。 | 
 **count** | **int**| 每页数量 | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **action_type** | **int**| 分类:   * &#x60;0&#x60; - 全部   * &#x60;1&#x60; - 私信互动   * &#x60;2&#x60; - 组件互动   * &#x60;3&#x60; - 主页互动  | 
 **cursor** | **int**| 分页游标 | [optional] [default to 1]
 **leads_level** | **int**| 用户状态:   * &#x60;-1&#x60; - 没兴趣   * &#x60;0&#x60; - 了解   * &#x60;1&#x60; - 有兴趣   * &#x60;2&#x60; - 有意愿   * &#x60;10&#x60; - 已转化  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

