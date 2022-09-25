# Views

## `html_view`

Directly render a template from `urls.py`, similar to using the generic `TemplateView`.

```python
# urls.py
from fbv.views import html_view

urlpatterns = (
    path("sample-html-view", html_view, {"template_name": "sample-html-view-template.html"}),
)
```

## `redirect_view`

Redirect to a named pattern from `urls.py`, similar to using the `RedirectView`. Can also specify whether the redirect is permanent or not (i.e. a 301 or 302). Defaults to a 302.

```python
# urls.py
from fbv.views import redirect_view

urlpatterns = (
    path("sample-html-view", redirect_view, {"pattern_name": "some-pattern-name"}),
    path("another-html-view", redirect_view, {"pattern_name": "another-pattern-name", permanent=True}),
)
```

## `favicon_file`

Serves an image file as `favicon.ico`.

```{note}
Even though the extension is `ico`, browsers will use other image formats. `PNG` images are widely supported and work great for this purpose. More details at: https://adamj.eu/tech/2022/01/18/how-to-add-a-favicon-to-your-django-site/#what-the-file-type.
```

```python
# urls.py
from fbv.views import favicon_file

urlpatterns = (
    path("favicon.ico", favicon_file, {"file_path": "static/img/favicon.png"}),
)
```

```{note}
`file_path` is relative to Django's `settings.BASE_DIR` path. i.e. the example above would use the file located at `/www/sample-project/static/img/favicon.png` if `settings.BASE_DIR` is `Path("/www/sample-project/")`.
```

## `favicon_emoji`

Serves an emoji as `favicon.ico`.

```{note}
Even though the extension is `ico`, browsers will use other image formats. The emoji will be rendered as an `SVG` which is supported by most modern browsers (other than Safari). More details at: https://adamj.eu/tech/2022/01/18/how-to-add-a-favicon-to-your-django-site/#what-the-file-type.
```

```python
# urls.py
from fbv.views import favicon_emoji

urlpatterns = (
    path("favicon.ico", favicon_emoji, {"emoji": "✨"}),
)
```
