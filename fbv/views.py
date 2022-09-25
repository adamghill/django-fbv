from typing import Any, Dict

from django.conf import settings
from django.http import (
    FileResponse,
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

from .decorators import render_html


@render_html()
def html_view(
    request: HttpRequest, template_name: str = None, context: Dict = None
) -> Dict[Any, Any]:
    """
    Serves an HTML template directly from urls.py.
    """

    if context is None:
        context = {}

    if template_name is not None:
        context["TEMPLATE"] = template_name

    return context


def redirect_view(
    request: HttpRequest, *args, pattern_name=None, permanent=False, **kwargs
) -> HttpResponse:
    """
    Redirect to a named pattern directly from urls.py.

    Based on code in https://spookylukey.github.io/django-views-the-right-way/redirects.html#additional-keyword-parameters.
    """
    url = reverse(pattern_name, args=args, kwargs=kwargs)

    if permanent:
        return HttpResponsePermanentRedirect(url)

    return HttpResponseRedirect(url)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)
def favicon_file(request: HttpRequest, file_path: str) -> FileResponse:
    """
    Serves a favicon from the file path.

    Based on code in https://adamj.eu/tech/2022/01/18/how-to-add-a-favicon-to-your-django-site/#what-the-file-type.
    """

    # Don't use context manager to open the file because it will be closed automatically
    # per https://docs.djangoproject.com/en/4.0/ref/request-response/#fileresponse-objects
    file = (settings.BASE_DIR / file_path).open("rb")

    return FileResponse(file)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)
def favicon_emoji(request: HttpRequest, emoji: str) -> HttpResponse:
    """
    Serves an emoji favicon.

    Based on code in https://adamj.eu/tech/2022/01/18/how-to-add-a-favicon-to-your-django-site/#what-the-file-type.
    """

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
<text y=".9em" font-size="90">{emoji}</text>
</svg>"""

    return HttpResponse(svg, content_type="image/svg+xml")
