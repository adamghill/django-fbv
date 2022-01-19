from unittest.mock import Mock

import pytest
from django.http import HttpResponse

from fbv.middleware import RequestMethodMiddleware


@pytest.fixture
def response():
    res = Mock(spec=HttpResponse)

    return res


http_methods = ["get", "post", "patch", "head", "put", "delete", "connect", "trace"]


@pytest.mark.parametrize("http_method", http_methods)
def test_request_method_middleware(request, response, http_method: str):
    setattr(request, "method", http_method.upper())
    middleware = RequestMethodMiddleware(response)
    middleware(request)

    for method in http_methods:
        http_method_property_name = f"is_{method}"
        assert hasattr(request, http_method_property_name)

        if method == http_method:
            assert getattr(request, http_method_property_name) is True
        else:
            assert getattr(request, http_method_property_name) is False


def test_request_method_middleware_with_client(client):
    response = client.get("/test-view")
    request = response.wsgi_request
    assert request.is_get
