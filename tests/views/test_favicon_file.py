import pytest

from fbv.views import favicon_file


def test(client):
    actual = client.get("/favicon-file.ico")

    assert actual.status_code == 200
    assert actual["Cache-Control"] == "max-age=86400, immutable, public"
    assert actual.headers["Content-Type"] == "image/png"

    content = b"".join(actual.streaming_content)
    assert len(content) > 0


def test_missing(request):
    request.method = "GET"
    request.META = {}

    with pytest.raises(FileNotFoundError):
        favicon_file(request, "bad-file-path")
