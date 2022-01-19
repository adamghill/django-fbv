from unittest.mock import patch

from fbv.views import html_view
from tests.utils import assert_response


def test_html_view_with_template_name_and_context(request):
    response = html_view(
        request, template_name="test/template.html", context={"test": 123}
    )
    assert_response(response, content="asdf 123")


def test_html_view_with_template_name_and_empty_context(request):
    response = html_view(request, template_name="test/template.html", context={})
    assert_response(response, content="asdf ")


def test_html_view_with_template_name(request):
    response = html_view(request, template_name="test/template.html")
    assert_response(response, content="asdf ")


def test_html_view_with_template_name(request):
    response = html_view(
        request, context={"TEMPLATE": "test/template.html", "test": 123}
    )
    assert_response(response, content="asdf 123")


@patch("django.template.loader.get_template")
def test_html_view_with_no_template_name(get_template, request):
    html_view(request)
    get_template.assert_called_once_with("fbv/html_view.html", using=None)


def test_render_view_with_client(client):
    response = client.get("/test-view")
    assert_response(response, content="asdf ")
