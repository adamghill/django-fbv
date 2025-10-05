from unittest.mock import patch

from tests.utils import assert_response

from fbv.views import html_view


def test_template_name_and_context(request):
    response = html_view(request, template_name="test/template.html", context={"test": 123})

    assert_response(response, content="asdf 123")


def test_template_name_and_empty_context(request):
    response = html_view(request, template_name="test/template.html", context={})

    assert_response(response, content="asdf ")


def test_template_name(request):
    response = html_view(request, template_name="test/template.html")

    assert_response(response, content="asdf ")


def test_template_name_without_extension(request):
    response = html_view(request, template_name="test/template")

    assert_response(response, content="asdf ")


def test_template_name_in_context(request):
    response = html_view(request, context={"TEMPLATE": "test/template.html", "test": 123})

    assert_response(response, content="asdf 123")


@patch("django.template.loader.get_template")
def test_no_template_name(get_template, request):
    html_view(request)

    get_template.assert_called_once_with("fbv/html_view.html", using=None)
