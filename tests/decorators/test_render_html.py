from fbv.decorators import render_html
from tests.utils import assert_response


def test_render_html(request):
    @render_html("test/template.html")
    def _(*args):
        return {"test": 123}

    response = _(request)

    assert_response(response, content="asdf 123")
