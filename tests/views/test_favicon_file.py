import pytest

from fbv.views import favicon_file


def test_favicon_file(client):
    response = client.get("/favicon-file.ico")
    assert response.status_code == 200
    assert response["Cache-Control"] == "max-age=86400, immutable, public"
    assert response.headers["Content-Type"] == "image/png"

    content = b"".join(response.streaming_content)
    assert len(content) > 0


def test_favicon_missing_file(request):
    request.method = "GET"

    with pytest.raises(FileNotFoundError):
        favicon_file(request, "bad-file-path")
