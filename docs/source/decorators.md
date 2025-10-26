# Decorators

## render_html

Decorator that provides a convienent way to render HTML from a function-based view.

```{note}
`render_html` is an alias for `render_view` that sets the content type to `text/html; charset=utf-8`.
```

### Decorator argument

The following would look for `decorator-arg.html` as the template.

```python
# sample_app/views.py
from fbv.decorators import render_html

@render_html("decorator-arg.html")
def sample_html_view(request):
    return {"data": 123}
```

### Context key

The following would look for `context-key.html` as the template.

```python
# sample_app/views.py
from fbv.decorators import render_html

@render_html()
def sample_html_view(request):
    return {"TEMPLATE": "context-key.html", "data": 123}
```

### Derived template

If no template is specified, the current module and function name are used for the template.

The following would look for `derived_template.html` as the template.

```python
# sample_app/views.py
from fbv.decorators import render_html

@render_html()
def derived_template(request):
    return {}
```

For nested view files, the following would look for `example/derived_template_2.html` as the template.

```python
# sample_app/views/example.py
from fbv.decorators import render_html

@render_html()
def derived_template_2(request):
    return {}
```

## render_view

Similar to `render_html`, but allows the response content type to be set.

```python
# sample_app/views.py
from fbv.decorators import render_view

@render_view("sample-xml-template.xml", content_type="application/xml")
def xml_view(request):
    return {"data": 123}
```

## render_json

Returns a `JSONResponse` from a function-based view. `dictionary`, Django `Model`, and Django `QuerySet` objects are all rendered automatically.

````{note}
By default, the rendered JSON won't have whitespaces between keys and values for the most compact representation possible. However, you can override that functionality by passing in a `tuple` as `(item_separator, key_separator)`.

```python
# sample_app/views.py
from fbv.decorators import render_json

@render_json(separators=(", ", ": "))
def sample_json_view(request):
    return {"data": 123,"test":456}
```

Or overriding just the item or key separators.

```python
# sample_app/views.py
from fbv.decorators import render_json

@render_json(item_separator=", ", key_separator=": ")
def sample_json_view(request):
    return {"data": 123,"test":456}
```

```json
{"data": 123, "test": 456}
```

````

### Dictionary

```python
# sample_app/views.py
from fbv.decorators import render_json

@render_json()
def dictionary_json_view(request):
    return {"data": 123}
```

```json
{
  "data": 123
}
```

### `Model`

```python
# sample_app/views.py
from django.contrib.auth.models import User
from fbv.decorators import render_json

@render_json()
def model_json_view(request):
    user = User.objects.get(id=1)

    return user
```

```json
{
  "pk": 1,
  "username": "testuser1",
  "first_name": "Test 1",
  "last_name": "User 1",
  "email": "testuser1@test.com"
}
```

### `Model` fields

To only return some of the model fields, pass in a `fields` kwarg with a `tuple` of field names.

```python
# sample_app/views.py
from django.contrib.auth.models import User
from fbv.decorators import render_json

@render_json(fields=("username",))
def model_fields_json_view(request):
    user = User.objects.get(id=1)

    return user
```

```json
{
  "username": "testuser"
}
```

### `QuerySet`

```python
# sample_app/views.py
from django.contrib.auth.models import User
from fbv.decorators import render_json

@render_json()
def queryset_json_view(request):
    users = User.objects.all()

    return users
```

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

### `QuerySet` fields

To only return some of the QuerySet's model fields, pass in a `fields` kwarg with a `tuple` of field names.

```python
# sample_app/views.py
from django.contrib.auth.models import User
from fbv.decorators import render_json

@render_json(fields=("username",))
def sample_json_queryset_view(request):
    users = User.objects.all()

    return users
```

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

### `QuerySet` values

To only return some of the QuerySet's model fields, call `QuerySet.values()` with the field names.

```python
# sample_app/views.py
from django.contrib.auth.models import User
from fbv.decorators import render_json

@render_json()
def sample_json_queryset_view(request):
    users = User.objects.all().values("first_name")

    return users
```

```json
[
  {
    "first_name": "Test 1"
  },
  {
    "first_name": "Test 2"
  }
]
```
