from tests.utils import assert_response

from fbv.decorators import render_html


def test(request):
    @render_html("test/template.html")
    def _(*args):
        return {"test": 123}

    response = _(request)

    assert_response(response, content="asdf 123")


def test_no_extension(request):
    @render_html("test/template")
    def _(*args):
        return {"test": 123}

    response = _(request)

    assert_response(response, content="asdf 123")


def test_no_template_name(request):
    @render_html()
    def render_view_with_no_template(*args):
        return {"test": 123}

    response = render_view_with_no_template(request)

    assert_response(response, content="zxcv 123")


def test_no_parens(request):
    @render_html
    def render_view_with_no_template(*args):
        return {"test": 123}

    response = render_view_with_no_template(request)

    assert_response(response, content="zxcv 123")
