# douyin_open/PoiProductProduct.PoiSpuApi

All URIs are relative to *https://open.douyin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_sku_sync_post**](PoiSpuApi.md#poi_sku_sync_post) | **POST** /poi/sku/sync/ | SKU同步
[**poi_spu_query_get**](PoiSpuApi.md#poi_spu_query_get) | **GET** /poi/spu/query/ | 查询SPU
[**poi_spu_sync_post**](PoiSpuApi.md#poi_spu_sync_post) | **POST** /poi/spu/sync/ | SPU同步

# **poi_sku_sync_post**
> InlineResponse2002 poi_sku_sync_post(body, access_token)

SKU同步

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiProductProduct
from douyin_open/PoiProductProduct.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiProductProduct.PoiSpuApi()
body = douyin_open/PoiProductProduct.Body1() # Body1 | 
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # SKU同步
    api_response = api_instance.poi_sku_sync_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSpuApi->poi_sku_sync_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | 
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_spu_query_get**
> InlineResponse2001 poi_spu_query_get(access_token, spu_ext_id)

查询SPU

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiProductProduct
from douyin_open/PoiProductProduct.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiProductProduct.PoiSpuApi()
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。
spu_ext_id = 'spu_ext_id_example' # str | 

try:
    # 查询SPU
    api_response = api_instance.poi_spu_query_get(access_token, spu_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSpuApi->poi_spu_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 调用/oauth/client_token/生成的token，此token不需要用户授权。 | 
 **spu_ext_id** | **str**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_spu_sync_post**
> InlineResponse200 poi_spu_sync_post(body, access_token)

SPU同步

* Scope: `poi.product` 

### Example
```python
from __future__ import print_function
import time
import douyin_open/PoiProductProduct
from douyin_open/PoiProductProduct.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/PoiProductProduct.PoiSpuApi()
body = douyin_open/PoiProductProduct.Body() # Body | 
access_token = 'access_token_example' # str | 调用/oauth/client_token/生成的token，此token不需要用户授权。

try:
    # SPU同步
    api_response = api_instance.poi_spu_sync_post(body, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiSpuApi->poi_spu_sync_post: %s\n" % e)
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

