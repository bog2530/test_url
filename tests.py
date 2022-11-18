import pytest

from response import (
    method_request,
    url_request,
    url_verification,
)

DATA_ERROR = 'https://bog2530.com'
DATA_OK = 'https://ru.wikipedia.org/wiki/HTTP'

def test_url_verification_error():
    assert not url_verification('temp.com')

def test_url_verification_ok():
    assert url_verification('https://ru.wikipedia.org/wiki/HTTP')

def test_method_request_error():
    assert None is method_request('https://bog2530.com')

def test_method_request_ok():
    assert method_request('https://ru.wikipedia.org/wiki/HTTP') == {
        'get': 200,
        'post': 200,
        'put': 200,
        'delete': 200,
        'head': 200
    }

def test_url_request_error():
    assert {} == url_request(['https://bog2530.com'])

def test_url_request_ok():
    assert {
        'https://ru.wikipedia.org/wiki/HTTP':{
            'delete': 200,
            'get': 200,
            'head': 200,
            'post': 200,
            'put': 200
            }
        } == url_request([
        'https://ru.wikipedia.org/wiki/HTTP',
    ])
