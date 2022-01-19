from functools import wraps
from os.path import join

from django.shortcuts import render

__all__ = [
    "render_html",
    "render_view",
]


def render_html(template_name: str = None):
    return render_view(template_name, content_type=None)


def render_view(template_name: str = None, content_type: str = None):
    """
    Decorator for Django function-based views that renders the passed-in template
    with the returned dictionary.

    Template name can be decorator parameter or `TEMPLATE` key in returned
    dictionary.  If view doesn't return dict then decorator simply returns output.

    Parameters:
     - template_name: template name to use
     - content_type: content type to send in response headers
    """

    def renderer(function):
        @wraps(function)
        def wrapper(request, *args, **kwargs):
            context = function(request, *args, **kwargs)

            if not isinstance(context, dict):
                return context

            _template_name = context.pop("TEMPLATE", template_name)

            if _template_name is None:
                module_name = function.__module__
                template_dir = module_name

                module_names = module_name.split(".")

                if len(module_names) > 1:
                    template_dir = join(*module_names[:-1])

                function_name = function.__name__
                _template_name = join(template_dir, f"{function_name}.html")

            return render(request, _template_name, context, content_type=content_type)

        return wrapper

    return renderer
