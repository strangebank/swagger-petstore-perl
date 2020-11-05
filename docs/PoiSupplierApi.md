# douyin_open/PoiSupplierSupplier.PoiSupplierApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_query_get**](PoiSupplierApi.md#poi_query_get) | **GET** /poi/query/ | 获取抖音POI ID
[**poi_supplier_match_post**](PoiSupplierApi.md#poi_supplier_match_post) | **POST** /poi/supplier/match/ | 店铺匹配
[**poi_supplier_match_query_get**](PoiSupplierApi.md#poi_supplier_match_query_get) | **GET** /poi/supplier/match/query/ | 店铺匹配结果查询
[**poi_supplier_query_get**](PoiSupplierApi.md#poi_supplier_query_get) | **GET** /poi/supplier/query/ | 查询店铺
[**poi_supplier_sync_post**](PoiSupplierApi.md#poi_supplier_sync_post) | **POST** /poi/supplier/sync/ | 商铺同步

# **poi_query_get**
> InlineResponse2002 poi_query_get(access_token, amap_id)

获取抖音POI ID

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiSupplierSupplier
from douyin_open/PoiSupplierSupplier.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiSupplierSupplier.PoiSupplierApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
amap_id = 'amap_id_example' # str | 

try:
    # 获取抖音POI ID
    api_response = api_instance.poi_query_get(access_token, amap_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSupplierApi->poi_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **amap_id** | **str**|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_supplier_match_post**
> InlineResponse2003 poi_supplier_match_post(body, access_token)

店铺匹配

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiSupplierSupplier
from douyin_open/PoiSupplierSupplier.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiSupplierSupplier.PoiSupplierApi()
body = douyin_open/PoiSupplierSupplier.Body1() # Body1 | 
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 店铺匹配
    api_response = api_instance.poi_supplier_match_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSupplierApi->poi_supplier_match_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | 
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_supplier_match_query_get**
> InlineResponse2004 poi_supplier_match_query_get(body, access_token)

店铺匹配结果查询

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiSupplierSupplier
from douyin_open/PoiSupplierSupplier.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiSupplierSupplier.PoiSupplierApi()
body = douyin_open/PoiSupplierSupplier.Body2() # Body2 | 
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 店铺匹配结果查询
    api_response = api_instance.poi_supplier_match_query_get(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSupplierApi->poi_supplier_match_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)|  | 
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_supplier_query_get**
> InlineResponse2001 poi_supplier_query_get(access_token, supplier_ext_id)

查询店铺

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiSupplierSupplier
from douyin_open/PoiSupplierSupplier.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiSupplierSupplier.PoiSupplierApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
supplier_ext_id = 'supplier_ext_id_example' # str | 

try:
    # 查询店铺
    api_response = api_instance.poi_supplier_query_get(access_token, supplier_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSupplierApi->poi_supplier_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **supplier_ext_id** | **str**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_supplier_sync_post**
> InlineResponse200 poi_supplier_sync_post(body, access_token)

商铺同步

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiSupplierSupplier
from douyin_open/PoiSupplierSupplier.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiSupplierSupplier.PoiSupplierApi()
body = douyin_open/PoiSupplierSupplier.Body() # Body | 
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # 商铺同步
    api_response = api_instance.poi_supplier_sync_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSupplierApi->poi_supplier_sync_post: %s\n" % e)
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

