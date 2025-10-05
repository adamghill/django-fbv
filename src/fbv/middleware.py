class RequestMethodMiddleware:
    """
    Adds the request method as boolean properties to the request object.

    Example: You can check that a request is a post with `request.is_post` instead
    of using the string equality `request.method == "POST"` which is more error prone.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.is_post = request.method == "POST"
        request.is_get = request.method == "GET"
        request.is_patch = request.method == "PATCH"
        request.is_head = request.method == "HEAD"
        request.is_put = request.method == "PUT"
        request.is_delete = request.method == "DELETE"
        request.is_connect = request.method == "CONNECT"
        request.is_trace = request.method == "TRACE"

        response = self.get_response(request)

        return response
