import json
from functools import partial, wraps
from os.path import join
from typing import Any, Dict, Tuple

from django.core import serializers
from django.db import models
from django.http import JsonResponse
from django.shortcuts import render

__all__ = [
    "render_html",
    "render_view",
    "render_json",
]


DEFAULT_JSON_SEPARATORS = (", ", ": ")
MINIFIED_JSON_SEPARATORS = (",", ":")


def render_html(template_name: str = None):
    return render_view(template_name=template_name, content_type=None)


def render_view(template_name: str = None, content_type: str = None) -> Any:
    """
    Decorator for function-based views that renders the passed-in template
    with the returned dictionary.

    Template name can be decorator parameter or `TEMPLATE` key in returned
    dictionary.

    If view doesn't return a `dictionary` then the function output is returned.

    Args:
        template_name: template name to use
        content_type: content type to send in response headers

    Returns:
        A `HttpResponse` or the output of the function if the output
        of the function is not a `dictionary`.
    """

    def renderer(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            context = func(request, *args, **kwargs)

            if not isinstance(context, dict):
                return context

            _template_name = context.pop("TEMPLATE", template_name)

            if _template_name is None:
                # Use a default template based on the current module
                module_name = func.__module__
                template_dir = module_name

                module_names = module_name.split(".")

                if len(module_names) > 1:
                    template_dir = join(*module_names[:-1])

                function_name = func.__name__
                _template_name = join(template_dir, f"{function_name}.html")

            return render(request, _template_name, context, content_type=content_type)

        return wrapper

    return renderer


def _convert_serialized_model(data: Dict, fields=None) -> Dict:
    """
    Converts the Django model dictionary that gets serialized into something
    more reasonable for external use.
    """

    model_data = {}

    if fields is None or "pk" in fields:
        model_data["pk"] = data["pk"]

    if fields is not None and "id" in fields:
        model_data["id"] = data["pk"]

    model_data.update(data["fields"])

    return model_data


def render_json(
    func=None, *, fields: Tuple[str] = None, separators: Tuple[str] = None
) -> Any:
    """
    Decorator for function-based views that returns `JsonResponse` with a serialized
    version of the returned Django `Model`, `QuerySet`, `dictionary`, or `list`.

    If the function doesn't return a `dictionary` or `list`, then the function output is returned.

    Args:
        fields: Tuple of strings to return. Only available when Django `Model` or `QuerySet` is returned.
        separators: Tuple in the form of (), which is passed to `json.dumps` in the `separators` kwarg.
    """

    if func is None:
        return partial(render_json, fields=fields, separators=separators)

    @wraps(func)
    def wrapper(request, *args, fields=fields, separators=separators, **kwargs):
        context = func(request, *args, **kwargs)

        if isinstance(context, models.Model):
            context = json.loads(
                serializers.serialize("json", [context], fields=fields)[1:-1]
            )

            context = _convert_serialized_model(context, fields=fields)
        elif isinstance(context, models.QuerySet):
            try:
                context = json.loads(
                    serializers.serialize("json", context, fields=fields)
                )

                context = [_convert_serialized_model(c, fields=fields) for c in context]
            except AttributeError:
                # `AttributeError: 'dict' object has no attribute '_meta'` gets thrown
                # when the `QuerySet` was created with `.values()` or `.values_list()`
                # which are actually `dictionaries` or `tuples` when iterated over
                context = [c for c in context]
        else:
            assert (
                fields is None
            ), "The `fields` kwarg should only be used when serializing Django models."

        if not isinstance(context, dict) and not isinstance(context, list):
            return context

        if separators is None:
            separators = MINIFIED_JSON_SEPARATORS

        # `safe` is always False because returning a list should be fine with modern browsers
        return JsonResponse(
            context, json_dumps_params={"separators": separators}, safe=False
        )

    return wrapper
