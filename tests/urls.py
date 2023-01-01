from django.urls import path

from fbv.decorators import render_html
from fbv.views import favicon_emoji, favicon_file, file, html_view, redirect_view


@render_html("test/template.html")
def test_view(request):
    return {}


urlpatterns = (
    path("test-decorator", test_view, name="test_decorator"),
    path("test-view", html_view, {"template_name": "test/template.html"}),
    path("robots.txt", file, {"file_path": "robots.txt"}),
    path("favicon-file.ico", favicon_file, {"file_path": "static/img/github.png"}),
    path("favicon-emoji.ico", favicon_emoji, {"emoji": "✨"}),
    path("test-redirect-302", redirect_view, {"pattern_name": "test_decorator"}),
    path(
        "test-redirect-301",
        redirect_view,
        {"pattern_name": "test_decorator", "permanent": True},
    ),
)
