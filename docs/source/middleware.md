# Middleware

## RequestMethodMiddleware

Adds a boolean property to the `request` for the current request's HTTP method.

### Installation

Add `"fbv.middleware.RequestMethodMiddleware"` to the `MIDDLEWARE` list in `settings.py`. It doesn't matter where in the list it is added, but it [probably shouldn't be first](https://docs.djangoproject.com/en/stable/ref/middleware/#middleware-ordering).

```python
# settings.py
MIDDLEWARE = [
    # other middleware
    "fbv.middleware.RequestMethodMiddleware",
    # other middleware
]
```

### `request` properties

Once the middleware is installed every `request` object will now have a boolean property for each of the following HTTP methods:

- `is_post`
- `is_get`
- `is_patch`
- `is_head`
- `is_put`
- `is_delete`
- `is_connect`
- `is_trace`

```python
# views.py
from fbv.decorators import render_html

@render_html("sample-html-template.html")
def sample_html_view(request):
    if request.is_get:  # instead of `request.method == "GET"`
        return {"http_method": "GET"}
    elif request.is_post:  # instead of `request.method == "POST"`
        return {"http_method": "POST"}
```
