# Copyright (C) 2022 CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

import os.path as osp
import requests
from cvat_sdk.api_client import ApiClient, Configuration

ROOT_DIR = __file__[:__file__.rfind(osp.join("utils", ""))]
ASSETS_DIR = osp.abspath(osp.join(ROOT_DIR, 'assets'))
# Suppress the warning from Bandit about hardcoded passwords
USER_PASS = '!Q@W#E$R' # nosec
BASE_URL = 'http://localhost:8080'
API_URL = BASE_URL + '/api/'

# MiniIO settings
MINIO_KEY = 'minio_access_key'
MINIO_SECRET_KEY =  'minio_secret_key' # nosec
MINIO_ENDPOINT_URL = 'http://localhost:9000'

def _to_query_params(**kwargs):
    return '&'.join([f'{k}={v}' for k,v in kwargs.items()])

def get_server_url(endpoint, **kwargs):
    return BASE_URL + '/' + endpoint + '?' + _to_query_params(**kwargs)

def get_api_url(endpoint, **kwargs):
    return API_URL + endpoint + '?' + _to_query_params(**kwargs)

def get_method(username, endpoint, **kwargs):
    return requests.get(get_api_url(endpoint, **kwargs), auth=(username, USER_PASS))

def options_method(username, endpoint, **kwargs):
    return requests.options(get_api_url(endpoint, **kwargs), auth=(username, USER_PASS))

def delete_method(username, endpoint, **kwargs):
    return requests.delete(get_api_url(endpoint, **kwargs), auth=(username, USER_PASS))

def patch_method(username, endpoint, data, **kwargs):
    return requests.patch(get_api_url(endpoint, **kwargs), json=data, auth=(username, USER_PASS))

def post_method(username, endpoint, data, **kwargs):
    return requests.post(get_api_url(endpoint, **kwargs), json=data, auth=(username, USER_PASS))

def post_files_method(username, endpoint, data, files, **kwargs):
    return requests.post(get_api_url(endpoint, **kwargs), data=data, files=files, auth=(username, USER_PASS))

def server_get(username, endpoint, **kwargs):
    return requests.get(get_server_url(endpoint, **kwargs), auth=(username, USER_PASS))

def make_api_client(user: str) -> ApiClient:
    return ApiClient(configuration=Configuration(host=BASE_URL, username=user, password=USER_PASS))
