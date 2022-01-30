def test_favicon_file(client):
    response = client.get("/favicon-file.ico")
    assert response.status_code == 200
    assert response["Cache-Control"] == "max-age=86400, immutable, public"
    assert response.headers["Content-Type"] == "image/png"

    content = b"".join(response.streaming_content)
    assert len(content) > 0


def test_favicon_emoji(client):
    response = client.get("/favicon-emoji.ico")
    assert response.status_code == 200
    assert response["Cache-Control"] == "max-age=86400, immutable, public"
    assert response.headers["Content-Type"] == "image/svg+xml"

    expected = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
<text y=".9em" font-size="90">✨</text>
</svg>"""
    actual = response.content.decode()

    assert actual == expected
