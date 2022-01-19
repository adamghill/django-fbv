# Decorators

Decorators that can be used on top of existing view functions.

## render_html

Decorator that provides a convienent way to render HTML from a function-based view.

**Built-in `render` function in `views.py`**

```python
from django.shortcuts import render

def sample_html_view(request):
    return render(request, template_name="sample-html-template.html", context={"data": 123})
```

**`render_html` with `template_name` argument in `views.py`**

```python
from fbv.decorators import render_html

@render_html("sample-html-template.html")
def sample_html_view(request):
    return {"data": 123}
```

**`render_html` with `TEMPLATE` dictionary key in `views.py`**

```python
from fbv.decorators import render_html

@render_html()
def sample_html_view(request):
    return {"TEMPLATE": "sample-html-template.html", "data": 123}
```

**`render_html` with no template specified in `views.py`**

This will use the current module and function name as the template name.

For example, the following would look for a `views/sample_html_view.html` template.

```python
from fbv.decorators import render_html

@render_html()
def sample_html_view(request):
    return {"data": 123}
```

```{note}
`render_html` is just an alias for `render_view` below that sets the content type to `text/html; charset=utf-8`.
```

## render_view

Includes all the functionality of the `html_view`, but always the content type to be set.

**Built-in `render` function in `views.py`**

```python
from django.shortcuts import render

def sample_xml_view(request):
    return render(request, template_name="sample-xml-template.html", context={"data": 123}, content_type="application/xml")
```

**`render_view` in `views.py`**

```python
from fbv.decorators import render_view

@render_view("sample-xml-template.xml", content_type="application/xml")
def sample_xml_view(request):
    return {"data": 123}
```
