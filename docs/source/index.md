# Introduction

`django-fbv` includes utilities to make function-based views cleaner, more efficient, and better tasting. 💥

## Why?

The Django community continues to be split about whether to use function-based views or class-based views. This library is intended to provide solutions that address some of the critiques of function-based views.

If you want to read a more detailed critique of class-based views, https://spookylukey.github.io/django-views-the-right-way/ is excellent.

## Installation

`poetry add django-fbv` OR `pip install django-fbv`

The decorators and views can be used by just importing them. The middleware [needs to be installed like typical Django middleware](middleware.md#installation).

## Prior art

- The `render_view` decorator was forked from `render_to` in https://github.com/skorokithakis/django-annoying.

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
