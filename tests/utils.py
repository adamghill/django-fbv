def assert_response(
    response,
    content: str = "",
    status_code: int = 200,
    content_type: str = "text/html; charset=utf-8",
):
    try:
        assert response.status_code == status_code
    except AssertionError:
        print("actual:", response.status_code)
        print("expected:", status_code)
        raise

    try:
        assert response.headers["Content-Type"] == content_type
    except AssertionError:
        print("actual:", response.headers["Content-Type"])
        print("expected:", content_type)
        raise

    try:
        assert response.content.decode() == content
    except AssertionError:
        print("actual:", response.content.decode())
        print("expected:", content)
        raise
