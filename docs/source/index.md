# Introduction

`django-fbv` includes utilities to make function-based views cleaner, more efficient, and better tasting. 💥

## Why? 🤔

The Django community has two ways to write views: [class-based](https://docs.djangoproject.com/en/stable/topics/class-based-views/) and [function-based](https://docs.djangoproject.com/en/stable/topics/http/views/). One benefit of function-based views is that the [`HttpRequest`](https://docs.djangoproject.com/en/stable/ref/request-response/#httprequest-objects) input and the [`HttpResponse`](https://docs.djangoproject.com/en/stable/ref/request-response/#httpresponse-objects) output is explicit, instead of being hidden within a hierarchy of classes and mixins.

`django-fbv` reduces the boilerplate code required when using function-based views. It also leverages _locality of behavior_ -- the name of the template is clearly associated to the view, instead of being part of the return statement.

Instead of this:

```python
# sample_app/views.py
from django.shortcuts import render

def regular_function_based_view(request):
  return render(request, "template_name.html", {"data": 123})
```

You can write this:

```python
# sample_app/views.py
from fbv.decorators import render_html

@render_html("template_name.html")
def django_fbv_view(request):
  return {"data": 123}
```

```{note}
If you want a more detailed critique of class-based views, I recommend reading https://spookylukey.github.io/django-views-the-right-way/.
```

## Installation ⚙️

`pip install django-fbv` OR `uv add django-fbv`

The [decorators](decorators.md) and [views](views.md) can be used by just importing them. The middleware [needs to be installed](https://django-fbv.adamghill.com/en/latest/middleware/#installation).

## Features 🤩

### Decorators

- [`fbv.decorators.render_html`](https://django-fbv.adamghill.com/en/latest/decorators/#render-html): renders a view as HTML with the specified template
- [`fbv.decorators.render_view`](https://django-fbv.adamghill.com/en/latest/decorators/#render-view): renders a view as a content type with the specified template
- [`fbv.decorators.render_json`](https://django-fbv.adamghill.com/en/latest/decorators/#render-json): 
renders dictionaries, Django `Model`, or Django `QuerySet` as a `JSON` response

### Views

- [`fbv.views.html_view`](https://django-fbv.adamghill.com/en/latest/views/#html-view): directly render a template from `urls.py`
- [`fbv.views.redirect_view`](https://django-fbv.adamghill.com/en/latest/views/#redirect-view): redirect to a pattern name from `urls.py`
- [`fbv.views.file`](https://django-fbv.adamghill.com/en/latest/views/#file): serve a file
- [`fbv.views.favicon_file`](https://django-fbv.adamghill.com/en/latest/views/#favicon-file): serve an image file as the favicon.ico
- [`fbv.views.favicon_emoji`](https://django-fbv.adamghill.com/en/latest/views/#favicon-emoji): serve an emoji as the favicon.ico

### Middleware

- [`fbv.middleware.RequestMethodMiddleware`](https://django-fbv.adamghill.com/en/latest/middleware/): adds a boolean property to the `request` for the current request's HTTP method

## Prior art 🖼️

- The `render_view` decorator was forked from `render_to` in https://github.com/skorokithakis/django-annoying.
- The `file`, `favicon_file` and `favicon_emoji` code is from https://adamj.eu/tech/2022/01/18/how-to-add-a-favicon-to-your-django-site/.


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
