class RequestMethodMiddleware:
    """
    Adds the request method as boolean properties to the request object.

    Example: You can check that a request is a post with `request.is_post` instead
    of using the string equality `request.method == "POST"` which is more error prone.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, "is_post", request.method == "POST")
        setattr(request, "is_get", request.method == "GET")
        setattr(request, "is_patch", request.method == "PATCH")
        setattr(request, "is_head", request.method == "HEAD")
        setattr(request, "is_put", request.method == "PUT")
        setattr(request, "is_delete", request.method == "DELETE")
        setattr(request, "is_connect", request.method == "CONNECT")
        setattr(request, "is_trace", request.method == "TRACE")

        response = self.get_response(request)

        return response
