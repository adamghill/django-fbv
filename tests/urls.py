from django.urls import path

from fbv.decorators import render_html
from fbv.views import favicon_emoji, favicon_file, html_view


@render_html("test/template.html")
def test_view(request):
    return {}


urlpatterns = (
    path("test-decorator", test_view),
    path("test-view", html_view, {"template_name": "test/template.html"}),
    path("favicon-file.ico", favicon_file, {"file_path": "static/img/github.png"}),
    path("favicon-emoji.ico", favicon_emoji, {"emoji": "✨"}),
)
