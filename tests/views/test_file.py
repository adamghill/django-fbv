import pytest

from fbv.views import file


def test(client):
    actual = client.get("/robots.txt")

    assert actual.status_code == 200
    assert actual["Cache-Control"] == "max-age=86400, immutable, public"
    assert actual.headers["Content-Type"] == "text/plain"

    content = b"".join(actual.streaming_content)
    assert len(content) > 0


def test_missing(request):
    request.method = "GET"
    request.META = {}

    with pytest.raises(FileNotFoundError):
        file(request, "bad-file-path")
