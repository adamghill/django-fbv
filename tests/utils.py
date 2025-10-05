def assert_response(
    response,
    content: str = "",
    status_code: int = 200,
    content_type: str = "text/html; charset=utf-8",
):
    try:
        assert response.status_code == status_code
    except AssertionError:
        print("actual:", response.status_code)  # noqa: T201
        print("expected:", status_code)  # noqa: T201
        raise

    try:
        assert response.headers["Content-Type"] == content_type
    except AssertionError:
        print("actual:", response.headers["Content-Type"])  # noqa: T201
        print("expected:", content_type)  # noqa: T201
        raise

    try:
        assert response.content.decode() == content
    except AssertionError:
        print("actual:", response.content.decode())  # noqa: T201
        print("expected:", content)  # noqa: T201
        raise
