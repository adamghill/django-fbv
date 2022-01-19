from django.urls import path

from fbv.decorators import render_html
from fbv.views import html_view


@render_html("test/template.html")
def test_view(request):
    return {}


urlpatterns = (
    path("test-decorator", test_view),
    path("test-view", html_view, {"template_name": "test/template.html"}),
)
