import json
from collections.abc import Callable
from functools import partial, wraps
from os.path import join

from django.core import serializers
from django.db import models
from django.http import JsonResponse
from django.shortcuts import render

__all__ = [
    "render_html",
    "render_json",
    "render_view",
]


DEFAULT_JSON_SEPARATORS = (", ", ": ")
MINIFIED_JSON_SEPARATORS = (",", ":")


def render_html(template_name: str | None = None) -> Callable:
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

    return render_view(template_name=template_name, content_type=None)


def render_view(template_name: str | None = None, content_type: str | None = None) -> Callable:
    """
    Decorator for function-based views that renders the passed-in template
    with the returned dictionary.

    Template name can be decorator parameter or `TEMPLATE` key in returned
    dictionary. `TEMPLATE` key in context will override passed-in template name.

    If there does not appear to be an extension for the template name, ".html" will be appended.

    If view doesn't return a `dictionary` then the function output is returned.

    Args:
        template_name: template name to use
        content_type: content type to send in response headers

    Returns:
        A `HttpResponse` or the output of the function if the output
        of the function is not a `dictionary`.
    """

    # Handle the case when the decorator is used without parentheses
    if callable(template_name):
        func = template_name
        template_name = None
        return render_view()(func)

    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            context = func(request, *args, **kwargs)

            if not isinstance(context, dict):
                return context

            _template_name = context.pop("TEMPLATE", template_name)

            if _template_name is None:
                # Use a default template based on the current module and function name
                module_name = func.__module__
                template_dir = module_name

                module_names = module_name.split(".")

                if len(module_names) > 2:  # noqa: PLR2004
                    template_dir = join(*[m for m in module_names if m != "views"])
                elif len(module_names) > 1:
                    template_dir = join(*module_names[:-1])

                function_name = func.__name__
                _template_name = join(template_dir, f"{function_name}")

            if "." not in _template_name:
                _template_name = f"{_template_name}.html"

            return render(request, _template_name, context, content_type=content_type)

        return wrapper

    return decorator


def _convert_serialized_model(data: dict, fields: tuple[str] | None = None) -> dict:
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
    func=None,
    *,
    fields: tuple[str] | None = None,
    separators: tuple[str] | None = None,
    item_separator: str | None = None,
    key_separator: str | None = None,
):
    """
    Decorator for function-based views that returns `JsonResponse` with a serialized
    version of the returned Django `Model`, `QuerySet`, `dictionary`, or `list`.

    If the function doesn't return a `dictionary` or `list`, then the function output is returned.

    Args:
        fields: Tuple of strings to return. Only available when Django `Model` or `QuerySet` is returned.
        separators: Tuple in the form of (), which is passed to `json.dumps` in the `separators` kwarg.
        item_separator: override the default item separator passed to `json.dumps` in the `separators` kwarg.
        key_separator: override the default key separator passed to `json.dumps` in the `separators` kwarg.
    """

    if func is None:
        return partial(
            render_json,
            fields=fields,
            separators=separators,
            item_separator=item_separator,
            key_separator=key_separator,
        )

    @wraps(func)
    def wrapper(
        request,
        *args,
        fields=fields,
        separators=separators,
        item_separator=item_separator,
        key_separator=key_separator,
        **kwargs,
    ):
        context = func(request, *args, **kwargs)

        if isinstance(context, models.Model):
            context = json.loads(serializers.serialize("json", [context], fields=fields)[1:-1])

            context = _convert_serialized_model(context, fields=fields)
        elif isinstance(context, models.QuerySet):
            try:
                context = json.loads(serializers.serialize("json", context, fields=fields))

                context = [_convert_serialized_model(c, fields=fields) for c in context]
            except AttributeError:
                # `AttributeError: 'dict' object has no attribute '_meta'` gets thrown
                # when the `QuerySet` was created with `.values()` or `.values_list()`
                # which are actually `dictionaries` or `tuples` when iterated over
                context = list(context)
        elif fields is not None:
            raise AssertionError("The `fields` kwarg should only be used when serializing Django models.")

        if not isinstance(context, dict) and not isinstance(context, list):
            return context

        if separators is None:
            separators = MINIFIED_JSON_SEPARATORS

        if item_separator:
            separators = (item_separator, separators[1])

        if key_separator:
            separators = (separators[0], key_separator)

        # `safe` is always False because returning a list should be fine with modern browsers
        return JsonResponse(context, json_dumps_params={"separators": separators}, safe=False)

    return wrapper
