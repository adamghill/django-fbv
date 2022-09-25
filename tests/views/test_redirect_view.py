from unittest.mock import patch

from fbv.views import redirect_view
from tests.utils import assert_response


def test_redirect_view_not_permanent(request):
    response = redirect_view(request, pattern_name="test_decorator", permanent=False)
    assert_response(response, status_code=302)


def test_redirect_view_permanent(request):
    response = redirect_view(request, pattern_name="test_decorator", permanent=True)
    assert_response(response, status_code=301)


def test_render_redirect_view_301(client):
    response = client.get("/test-redirect-301")
    assert_response(response, status_code=301)

    assert response.url == "/test-decorator"


def test_render_redirect_view_302(client):
    response = client.get("/test-redirect-302")
    assert_response(response, status_code=302)

    assert response.url == "/test-decorator"
