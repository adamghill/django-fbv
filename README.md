# django-fbv

Utilities to make Django function-based views cleaner, more efficient, and better tasting.

## decorators

- `fbv.decorators.render_html`: convenience decorator to use instead of `django.shortcut.render` with a specified template
- `fbv.decorators.render_view`: convenience decorator to use instead of `django.shortcut.render` with a specified template and content type

## views

- `fbv.views.html_view`: directly renders a template from `urls.py`

## middleware

- `fbv.middleware.RequestMethodMiddleware`: adds a boolean property to the `request` for the current request's HTTP method

Complete documentation: https://django-fbv.readthedocs.org
