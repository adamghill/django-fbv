import json

import pytest
from django.utils.timezone import now

from fbv.decorators import (
    DEFAULT_JSON_SEPARATORS,
    MINIFIED_JSON_SEPARATORS,
    render_json,
)
from tests.models import FakeModel


def test_render_json_no_parens(request):
    @render_json
    def _(*args):
        return {"test": "test123"}

    response = _(request)

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == '{"test":"test123"}'


def test_render_json_not_dictionary(request):
    @render_json()
    def _(*args):
        return "test123"

    response = _(request)

    assert response == "test123"


def test_render_json_dictionary(request):
    @render_json()
    def _(*args):
        return {"test": 123}

    response = _(request)

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == '{"test":123}'


def test_render_json_dictionary_fields(request):
    @render_json(fields=("test"))
    def _(*args):
        return {"test": 123}

    with pytest.raises(AssertionError):
        _(request)


def test_render_json_dictionary_separators(request):
    @render_json(separators=DEFAULT_JSON_SEPARATORS)
    def _(*args):
        return {"test": 123}

    response = _(request)

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == '{"test": 123}'


def test_render_json_datetime(request):
    test_date_time = now()

    @render_json()
    def _(*args):
        return {"test_date_time": test_date_time}

    response = _(request)

    assert response.content.decode() == json.dumps(
        {"test_date_time": test_date_time.isoformat()[:-3]},
        separators=MINIFIED_JSON_SEPARATORS,
    )


def test_render_json_model(request):
    fake_model = FakeModel(name="test123")

    @render_json()
    def _(*args):
        return fake_model

    response = _(request)

    expected = json.dumps(
        {
            "model": "tests.fakemodel",
            "pk": None,
            "fields": {"name": "test123", "is_valid": False},
        },
        separators=MINIFIED_JSON_SEPARATORS,
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == expected


def test_render_json_model_fields(request):
    fake_model = FakeModel(id=456, name="test789")

    @render_json(fields=("name",))
    def _(*args):
        return fake_model

    response = _(request)

    expected = json.dumps(
        {"model": "tests.fakemodel", "pk": 456, "fields": {"name": "test789"}},
        separators=MINIFIED_JSON_SEPARATORS,
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == expected


@pytest.mark.django_db
def test_render_json_saved_model(request):
    fake_model = FakeModel(name="test123")
    fake_model.save()

    @render_json()
    def _(*args):
        return fake_model

    response = _(request)

    expected = json.dumps(
        {
            "model": "tests.fakemodel",
            "pk": fake_model.id,
            "fields": {"name": "test123", "is_valid": False},
        },
        separators=MINIFIED_JSON_SEPARATORS,
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == expected


@pytest.mark.django_db
def test_render_json_queryset(request):
    fake_model_one = FakeModel(name="test123", is_valid=True)
    fake_model_one.save()

    fake_model_two = FakeModel(name="test456", is_valid=False)
    fake_model_two.save()

    @render_json()
    def _(*args):
        return FakeModel.objects.all()

    response = _(request)

    expected = json.dumps(
        {
            "models": [
                {
                    "model": "tests.fakemodel",
                    "pk": fake_model_one.id,
                    "fields": {"name": "test123", "is_valid": True},
                },
                {
                    "model": "tests.fakemodel",
                    "pk": fake_model_two.id,
                    "fields": {"name": "test456", "is_valid": False},
                },
            ]
        },
        separators=MINIFIED_JSON_SEPARATORS,
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == expected
