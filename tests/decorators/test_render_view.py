import pytest
from django.template.exceptions import TemplateDoesNotExist
from tests.utils import assert_response
from tests.views.example import three_segment_default

from fbv.decorators import render_view


def test(request):
    @render_view("test/template.html")
    def _(*args):
        return {"test": 123}

    response = _(request)

    assert_response(response, content="asdf 123")


def test_no_extension(request):
    @render_view("test/template")
    def _(*args):
        return {"test": 123}

    response = _(request)

    assert_response(response, content="asdf 123")


def test_no_parens(request):
    @render_view
    def render_view_with_no_template(*args):
        return {"test": 123}

    response = render_view_with_no_template(request)

    assert_response(response, content="hjkl 123")


def test_not_dictionary(request):
    @render_view("test/template.html")
    def _(*args):
        return "test123"

    response = _(request)

    assert response == "test123"


def test_custom_content_type(request):
    @render_view("test/template.html", content_type="application/json")
    def _(*args):
        return {"test": 123}

    response = _(request)

    assert_response(response, content="asdf 123", content_type="application/json")


def test_empty_context(request):
    @render_view("test/template.html")
    def _(*args):
        return {}

    response = _(request)

    assert_response(response, content="asdf ")


def test_template_in_dictionary(request):
    @render_view()
    def _(*args):
        return {"TEMPLATE": "test/template.html", "test": 123}

    response = _(request)

    assert_response(response, content="asdf 123")


@render_view()
def render_view_with_no_template(*args):
    return {"test": 456}


def test_no_template(request):
    response = render_view_with_no_template(request)

    assert_response(response, content="hjkl 456")


def test_missing_template(request):
    @render_view("test/template1.html")
    def _(*args):
        return {}

    with pytest.raises(TemplateDoesNotExist):
        _(request)


def test_with_client(client):
    response = client.get("/test-decorator")

    assert_response(response, content="asdf ")


def test_default_template_three_segment_module(request):
    response = three_segment_default(request)

    # Expects template at: tests/templates/test_render_view/three_segment_default.html
    assert_response(response, content="drop-last 789")
