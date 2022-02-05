import pytest
from django.template.exceptions import TemplateDoesNotExist

from fbv.decorators import render_view
from tests.utils import assert_response


@pytest.mark.skip("Parens are required at least for now")
def test_render_view_no_parens(request):
    @render_view
    def _(*args):
        return {"test": 123}

    response = _(request)

    assert_response(response, content="asdf 123")


def test_render_view_default_content_type(request):
    @render_view("test/template.html")
    def _(*args):
        return {"test": 123}

    response = _(request)

    assert_response(response, content="asdf 123")


def test_render_view_not_dictionary(request):
    @render_view("test/template.html")
    def _(*args):
        return "test123"

    response = _(request)

    assert response == "test123"


def test_render_view_custom_content_type(request):
    @render_view("test/template.html", content_type="application/json")
    def _(*args):
        return {"test": 123}

    response = _(request)

    assert_response(response, content="asdf 123", content_type="application/json")


def test_render_view_empty_context(request):
    @render_view("test/template.html")
    def _(*args):
        return {}

    response = _(request)

    assert_response(response, content="asdf ")


def test_render_view_template_in_dictionary(request):
    @render_view()
    def _(*args):
        return {"TEMPLATE": "test/template.html", "test": 123}

    response = _(request)

    assert_response(response, content="asdf 123")


@render_view()
def render_view_with_no_template(*args):
    return {"test": 456}


def test_render_view_no_template(request):
    response = render_view_with_no_template(request)

    assert_response(response, content="hjkl 456")


def test_render_view_missing_template(request):
    @render_view("test/template1.html")
    def _(*args):
        return {}

    with pytest.raises(TemplateDoesNotExist):
        _(request)


def test_render_view_with_client(client):
    response = client.get("/test-decorator")

    assert_response(response, content="asdf ")
