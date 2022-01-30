<p align="center">
  <a href="https://django-fbv.readthedocs.io"><h1 align="center">django-fbv</h1></a>
</p>
<p align="center">Utilities to make Django function-based views cleaner, more efficient, and better tasting. 💥</p>

![PyPI](https://img.shields.io/pypi/v/django-fbv?color=blue&style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/django-fbv?color=blue&style=flat-square)
![GitHub Sponsors](https://img.shields.io/github/sponsors/adamghill?color=blue&style=flat-square)

📖 Complete documentation: https://django-fbv.readthedocs.io

📦 Package located at https://pypi.org/project/django-fbv/

## Features

### decorators

- [`fbv.decorators.render_html`](https://django-fbv.readthedocs.io/en/latest/decorators/#render-html): decorator to specify the template that a view function response should use when rendering
- [`fbv.decorators.render_view`](https://django-fbv.readthedocs.io/en/latest/decorators/#render-view): decorator to specify the template and content type that a view function response should use when rendering
- [`fbv.decorators.render_json`](https://django-fbv.readthedocs.io/en/latest/decorators/#render-json): decorator to automatically render dictionaries, Django Models, or Django QuerySets as a JSON response

### views

- [`fbv.views.html_view`](https://django-fbv.readthedocs.io/en/latest/views/#html-view): directly render a template from `urls.py`
- [`fbv.views.favicon_file`](https://django-fbv.readthedocs.io/en/latest/views/#favicon-file): serve an image file as the favicon.ico
- [`fbv.views.favicon_emoji`](https://django-fbv.readthedocs.io/en/latest/views/#favicon-emoji): serve an emoji as the favicon.ico

### middleware

- [`fbv.middleware.RequestMethodMiddleware`](https://django-fbv.readthedocs.io/en/latest/middleware/): adds a boolean property to the `request` for the current request's HTTP method

Read all of the documentation at https://django-fbv.readthedocs.io/.
