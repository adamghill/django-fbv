def test(client):
    expected = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
<text y=".9em" font-size="90">✨</text>
</svg>"""

    actual = client.get("/favicon-emoji.ico")

    assert actual.status_code == 200
    assert actual["Cache-Control"] == "max-age=86400, immutable, public"
    assert actual.headers["Content-Type"] == "image/svg+xml"
    assert expected == actual.content.decode()
