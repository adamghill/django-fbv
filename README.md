<p align="center">
  <a href="https://django-fbv.adamghill.com"><h1 align="center">django-fbv</h1></a>
</p>
<p align="center">Utilities to make Django function-based views cleaner, more efficient, and better tasting. 💥</p>

![PyPI](https://img.shields.io/pypi/v/django-fbv?color=blue&style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/django-fbv?color=blue&style=flat-square)
![GitHub Sponsors](https://img.shields.io/github/sponsors/adamghill?color=blue&style=flat-square)

📖 Complete documentation: https://django-fbv.adamghill.com

📦 Package located at https://pypi.org/project/django-fbv/

## Features

## Features

### Decorators

- [`fbv.decorators.render_html`](https://django-fbv.adamghill.com/en/latest/decorators/#render-html): renders a view as HTML with the specified template
- [`fbv.decorators.render_view`](https://django-fbv.adamghill.com/en/latest/decorators/#render-view): renders a view as a content type with the specified template
- [`fbv.decorators.render_json`](https://django-fbv.adamghill.com/en/latest/decorators/#render-json): 
renders dictionaries, Django Models, or Django QuerySets as a JSON response

### Views

- [`fbv.views.html_view`](https://django-fbv.adamghill.com/en/latest/views/#html-view): directly render a template from `urls.py`
- [`fbv.views.redirect_view`](https://django-fbv.adamghill.com/en/latest/views/#redirect-view): redirect to a pattern name from `urls.py`
- [`fbv.views.file`](https://django-fbv.adamghill.com/en/latest/views/#file): serve a file
- [`fbv.views.favicon_file`](https://django-fbv.adamghill.com/en/latest/views/#favicon-file): serve an image file as the favicon.ico
- [`fbv.views.favicon_emoji`](https://django-fbv.adamghill.com/en/latest/views/#favicon-emoji): serve an emoji as the favicon.ico

### Middleware

- [`fbv.middleware.RequestMethodMiddleware`](https://django-fbv.adamghill.com/en/latest/middleware/): adds a boolean property to the `request` for the current request's HTTP method

Read all of the documentation at https://django-fbv.adamghill.com/.
