# Introduction

`django-fbv` includes utilities to make function-based views cleaner, more efficient, and better tasting. 💥

## Why?

The Django community has two ways to build views: class-based and function-based. This library is intended to solve for some of the annoyances of function-based views.

If you want to read a more detailed critique of class-based views, https://spookylukey.github.io/django-views-the-right-way/ is excellent.

## Installation

`pip install django-fbv` OR `uv add django-fbv`

The [decorators](decorators.md) and [views](views.md) can be used by just importing them. The middleware [needs to be installed](middleware.md#installation).

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
