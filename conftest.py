from django import setup as django_setup
from django.conf import settings


def pytest_configure():
    databases = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    }

    templates = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ["tests/templates"],
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.request",
                ],
            },
        }
    ]

    installed_apps = [
        "fbv",
        "tests.apps.Config",
    ]

    middlewares = [
        "fbv.middleware.RequestMethodMiddleware",
    ]

    settings.configure(
        SECRET_KEY="this-is-a-secret",
        TEMPLATES=templates,
        ROOT_URLCONF="tests.urls",
        INSTALLED_APPS=installed_apps,
        UNIT_TEST=True,
        MIDDLEWARE=middlewares,
        DATABASES=databases,
    )

    django_setup()
