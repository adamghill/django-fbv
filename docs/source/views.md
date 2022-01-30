# Views

## `html_view`

Directly render a template from `urls.py`, similar to using the generic `TemplateView`.

**`html_view` in `url.py`**

```python
from fbv.views import html_view

urlpatterns = (
    path("sample-html-view", html_view, {"template_name": "sample-html-view-template.html"}),
)
```
