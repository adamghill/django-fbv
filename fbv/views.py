from typing import Dict

from django.http import HttpRequest

from .decorators import render_html


@render_html()
def html_view(request: HttpRequest, template_name: str = None, context: Dict = None):
    if context is None:
        context = {}

    if template_name is not None:
        context["TEMPLATE"] = template_name

    return context
