#!/usr/bin/python
# coding=utf-8
from __future__ import print_function
import time
import douyin_open.ToutiaoOauth2Oauth2
from douyin_open.ToutiaoOauth2Oauth2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin_open/ToutiaoOauth2Oauth2.ToutiaoClientTokenApi()
client_key = 'client_key_example' # str | 应用唯一标识
client_secret = 'client_secret_example' # str | 应用唯一标识对应的密钥
grant_type = 'grant_type_example' # str | 传client_credential

try:
        # 生成client_token
            api_response = api_instance.oauth_client_token_get(client_key, client_secret, grant_type)
            pprint(api_response)
except ApiException as e:
        print("Exception when calling ToutiaoClientTokenApi->oauth_client_token_get: %s\n" % e)
