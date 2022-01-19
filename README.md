<p align="center">
  <a href="https://coltrane.readthedocs.io"><h1 align="center">django-fbv</h1></a>
</p>
<p align="center">Utilities to make Django function-based views cleaner, more efficient, and better tasting. 💥</p>

![PyPI](https://img.shields.io/pypi/v/django-fbv?color=blue&style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/django-fbv?color=blue&style=flat-square)
![GitHub Sponsors](https://img.shields.io/github/sponsors/adamghill?color=blue&style=flat-square)

📖 Complete documentation: https://django-fbv.readthedocs.io

📦 Package located at https://pypi.org/project/django-fbv/

## Features

### decorators

- `fbv.decorators.render_html`: convenience decorator to use instead of `django.shortcut.render` with a specified template
- `fbv.decorators.render_view`: convenience decorator to use instead of `django.shortcut.render` with a specified template and content type

### views

- `fbv.views.html_view`: directly renders a template from `urls.py`

### middleware

- `fbv.middleware.RequestMethodMiddleware`: adds a boolean property to the `request` for the current request's HTTP method

Read all of the documentation at https://django-fbv.readthedocs.io/.
