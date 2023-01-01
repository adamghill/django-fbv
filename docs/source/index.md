# Introduction

`django-fbv` includes utilities to make function-based views cleaner, more efficient, and better tasting. 💥

## Why?

The Django community continues to be split about whether to use function-based views or class-based views. This library is intended to provide solutions that address some of the annoyances of function-based views.

If you want to read a more detailed critique of class-based views, https://spookylukey.github.io/django-views-the-right-way/ is excellent.

## Installation

`poetry add django-fbv` OR `pip install django-fbv`

The [decorators](decorators.md) and [views](views.md) can be used by just importing them. The middleware [needs to be installed like typical Django middleware](middleware.md#installation).

## Features

### decorators

- [`fbv.decorators.render_html`](https://django-fbv.readthedocs.io/en/latest/decorators/#render-html): decorator to specify the template that a view function response should use when rendering
- [`fbv.decorators.render_view`](https://django-fbv.readthedocs.io/en/latest/decorators/#render-view): decorator to specify the template and content type that a view function response should use when rendering
- [`fbv.decorators.render_json`](https://django-fbv.readthedocs.io/en/latest/decorators/#render-json): decorator to automatically render dictionaries, Django Models, or Django QuerySets as a JSON response

### views

- [`fbv.views.html_view`](https://django-fbv.readthedocs.io/en/latest/views/#html-view): directly render a template from `urls.py`
- [`fbv.views.redirect_view`](https://django-fbv.readthedocs.io/en/latest/views/#redirect-view): redirect to a pattern name from `urls.py`
- [`fbv.views.file`](https://django-fbv.readthedocs.io/en/latest/views/#file): serve a file
- [`fbv.views.favicon_file`](https://django-fbv.readthedocs.io/en/latest/views/#favicon-file): serve an image file as the favicon.ico
- [`fbv.views.favicon_emoji`](https://django-fbv.readthedocs.io/en/latest/views/#favicon-emoji): serve an emoji as the favicon.ico

### middleware

- [`fbv.middleware.RequestMethodMiddleware`](https://django-fbv.readthedocs.io/en/latest/middleware/): adds a boolean property to the `request` for the current request's HTTP method

## Prior art

- The `render_view` decorator was forked from `render_to` in the delightful https://github.com/skorokithakis/django-annoying library.
- The `file`, `favicon_file` and `favicon_emoji` code is from the superb https://adamj.eu/tech/2022/01/18/how-to-add-a-favicon-to-your-django-site/ blog post.

```{toctree}
:maxdepth: 2
:hidden:

self
decorators
views
middleware
GitHub <https://github.com/adamghill/django-fbv>
Sponsor <https://github.com/sponsors/adamghill>
```
