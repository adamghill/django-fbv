# 0.7.0

- Default to ".html" as the template extension if an extension is not specified.
- Add ability to call `render_view` or `render_html` decorators without parenthesis.

## Breaking Changes

- Require Python 3.10+.

# 0.6.0

- Add `fbv.views.file` method.

# 0.5.0

- Add `redirect_view`.

# 0.4.0

- Add support for Django `QuerySet.values()`, `QuerySet.values_list()`, and `list` to `render_json` decorator.

- **Breaking changes**

- Django `Model` and `QuerySet` are serialized into JSON with less internal information leakage.

# 0.3.0

- Add `favicon_file`, `favicon_emoji` views.

# 0.2.0

- Add `render_json` decorator.

# 0.1.0

- Add `render_html`, `render_view` decorators.
- Add `RequestMethodMiddleware` middleware.
- Add `html_view` view.
