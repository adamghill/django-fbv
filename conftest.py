from django import setup as django_setup
from django.conf import settings


def pytest_configure():
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
        # "fbv",
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
    )

    django_setup()
