# Decorators

## render_html

Decorator that provides a convienent way to render HTML from a function-based view.

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

Includes all the functionality of the `html_view`, but allows the response content type to be set.

**`render_view` in `views.py`**

```python
from fbv.decorators import render_view

@render_view("sample-xml-template.xml", content_type="application/xml")
def sample_xml_view(request):
    return {"data": 123}
```

## render_json

Decorator that provides a convienent way to return a `JSONResponse` from a function-based view. `dictionary`, Django `Model`, and Django `QuerySet` objects are all rendered automatically by `render_json`.

````{note}
By default, the rendered JSON won't have whitespaces between keys and values for the most compact representation as possible. However, you can override that functionality by passing in a `tuple` as `(item_separator, key_separator)`.

**`render_json` in `views.py`**

```python
from fbv.decorators import render_json

@render_json()
def sample_json_view(request):
    return {"data": 123, "test": 456}
```

**Default JSON response**

```json
{"data":123,"test":456}
```

**`render_json` with `separators` in `views.py`**

```python
from fbv.decorators import render_json

@render_json(separators=(", ", ": "))
def sample_json_view(request):
    return {"data": 123, "test":456}
```

**Separators JSON response**

```json
{"data": 123, "test": 456}
```

````

### dictionary

**`render_json` in `views.py`**

```python
from fbv.decorators import render_json

@render_json()
def sample_json_view(request):
    return {"data": 123}
```

**`dictionary` JSON response**

```json
{ "data": 123 }
```

### Django `Model`

**`render_json` Django `Model` in `views.py`**

```python
from django.contrib.auth.models import User
from fbv.decorators import render_json

@render_json()
def sample_json_model_view(request):
    user = User.objects.get(id=1)

    return user
```

**Django `Model` JSON response**

```json
{
  "pk": 1,
  "username": "testuser1",
  "first_name": "Test 1",
  "last_name": "User 1",
  "email": "testuser1@test.com"
}
```

### Specifying model fields

To only return some of the model fields, pass in a `fields` kwarg with a `tuple` of field names.

**`render_json` Django `Model` in `views.py`**

```python
from django.contrib.auth.models import User
from fbv.decorators import render_json

@render_json(fields=("username", ))
def sample_json_model_view(request):
    user = User.objects.get(id=1)

    return user
```

**Django `Model` JSON response**

```json
{
  "username": "testuser"
}
```

### Django `QuerySet`

**`render_json` Django `QuerySet` in `views.py`**

```python
from django.contrib.auth.models import User
from fbv.decorators import render_json

@render_json()
def sample_json_queryset_view(request):
    users = User.objects.all()

    return users
```

**Django `QuerySet` JSON response**

```json
[
  {
    "pk": 1,
    "username": "testuser1",
    "first_name": "Test 1",
    "last_name": "User 1",
    "email": "testuser1@test.com"
  },
  {
    "pk": 2,
    "username": "testuser2",
    "first_name": "Test 2",
    "last_name": "User 2",
    "email": "testuser2@test.com"
  }
]
```

### Specifying QuerySet model fields

To only return some of the QuerySet's model fields, pass in a `fields` kwarg with a `tuple` of field names.

**`render_json` Django `QuerySet` with fields in `views.py`**

```python
from django.contrib.auth.models import User
from fbv.decorators import render_json

@render_json(fields=("username",))
def sample_json_queryset_view(request):
    users = User.objects.all()

    return users
```

**Django `QuerySet` with fields JSON response**

```json
[
  {
    "username": "testuser1"
  },
  {
    "username": "testuser2"
  }
]
```

### Using `QuerySet.values()`

To only return some of the QuerySet's model fields, call `QuerySet.values()` with the field names.

**`render_json` Django `QuerySet.values()` in `views.py`**

```python
from django.contrib.auth.models import User
from fbv.decorators import render_json

@render_json()
def sample_json_queryset_view(request):
    users = User.objects.all().values("first_name")

    return users
```

**Django `QuerySet.values()` JSON response**

```json
[
  {
    "first_name": "Test "
  },
  {
    "first_name": "Test 2"
  }
]
```
