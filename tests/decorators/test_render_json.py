import json

import pytest
from django.utils.timezone import now
from tests.models import FakeModel

from fbv.decorators import (
    DEFAULT_JSON_SEPARATORS,
    MINIFIED_JSON_SEPARATORS,
    render_json,
)


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


def test_render_json_item_separator(request):
    @render_json(item_separator=",  ")
    def _(*args):
        return {"test": 123, "test1": 456}

    response = _(request)

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == '{"test":123,  "test1":456}'


def test_render_json_key_separator(request):
    @render_json(key_separator=":  ")
    def _(*args):
        return {"test": 123, "test1": 456}

    response = _(request)

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == '{"test":  123,"test1":  456}'


def test_render_json_item_key_separator(request):
    @render_json(item_separator=",  ", key_separator=":  ")
    def _(*args):
        return {"test": 123, "test1": 456}

    response = _(request)

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == '{"test":  123,  "test1":  456}'


def test_render_json_datetime(request):
    test_date_time = now()
    dt = test_date_time.isoformat()[:-9]

    expected = json.dumps(
        {"test_date_time": f"{dt}Z"},
        separators=MINIFIED_JSON_SEPARATORS,
    )

    @render_json()
    def _(*args):
        return {"test_date_time": test_date_time}

    response = _(request)
    actual = response.content.decode()

    assert expected == actual


def test_render_json_model(request):
    fake_model = FakeModel(name="test123")

    @render_json()
    def _(*args):
        return fake_model

    response = _(request)

    expected = json.dumps(
        {"pk": None, "name": "test123", "is_valid": False},
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
        {"name": "test789"},
        separators=MINIFIED_JSON_SEPARATORS,
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == expected


def test_render_json_model_fields_with_empty_tuple(request):
    fake_model = FakeModel(id=456, name="test789")

    @render_json(fields=())
    def _(*args):
        return fake_model

    response = _(request)

    expected = json.dumps(
        {},
        separators=MINIFIED_JSON_SEPARATORS,
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == expected


def test_render_json_model_fields_with_pk(request):
    fake_model = FakeModel(id=456, name="test789")

    @render_json(fields=("pk",))
    def _(*args):
        return fake_model

    response = _(request)

    expected = json.dumps(
        {"pk": 456},
        separators=MINIFIED_JSON_SEPARATORS,
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == expected


def test_render_json_model_fields_with_id(request):
    fake_model = FakeModel(id=456, name="test789")

    @render_json(fields=("id",))
    def _(*args):
        return fake_model

    response = _(request)

    expected = json.dumps(
        {"id": 456},
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
            "pk": fake_model.id,
            "name": "test123",
            "is_valid": False,
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
        [
            {"pk": fake_model_one.id, "name": "test123", "is_valid": True},
            {"pk": fake_model_two.id, "name": "test456", "is_valid": False},
        ],
        separators=MINIFIED_JSON_SEPARATORS,
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == expected


@pytest.mark.django_db
def test_render_json_queryset_values(request):
    fake_model_one = FakeModel(name="test123", is_valid=True)
    fake_model_one.save()

    fake_model_two = FakeModel(name="test456", is_valid=False)
    fake_model_two.save()

    @render_json()
    def _(*args):
        return FakeModel.objects.all().values()

    response = _(request)

    expected = json.dumps(
        [
            {"id": 1, "name": "test123", "is_valid": True},
            {"id": 2, "name": "test456", "is_valid": False},
        ],
        separators=MINIFIED_JSON_SEPARATORS,
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == expected


@pytest.mark.django_db
def test_render_json_queryset_values_list(request):
    fake_model_one = FakeModel(name="test123", is_valid=True)
    fake_model_one.save()

    fake_model_two = FakeModel(name="test456", is_valid=False)
    fake_model_two.save()

    @render_json()
    def _(*args):
        return FakeModel.objects.all().values_list()

    response = _(request)

    expected = json.dumps(
        [
            [1, "test123", True],
            [2, "test456", False],
        ],
        separators=MINIFIED_JSON_SEPARATORS,
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == expected


@pytest.mark.django_db
def test_render_json_queryset_values_list_flat(request):
    fake_model_one = FakeModel(name="test123", is_valid=True)
    fake_model_one.save()

    fake_model_two = FakeModel(name="test456", is_valid=False)
    fake_model_two.save()

    @render_json()
    def _(*args):
        return FakeModel.objects.all().values_list("id", flat=True)

    response = _(request)

    expected = json.dumps(
        [1, 2],
        separators=MINIFIED_JSON_SEPARATORS,
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.content.decode() == expected
