import pytest

from fbv.views import file


def test_file(client):
    response = client.get("/robots.txt")
    assert response.status_code == 200
    assert response["Cache-Control"] == "max-age=86400, immutable, public"
    assert response.headers["Content-Type"] == "text/plain"

    content = b"".join(response.streaming_content)
    assert len(content) > 0


def test_missing_file(request):
    request.method = "GET"

    with pytest.raises(FileNotFoundError):
        file(request, "bad-file-path")
