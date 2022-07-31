from time import time


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path.startswith('/book/') or request.path.startswith('/tabs/'):
            start = time()
            response = self.get_response(request)
            end = time()
            print('url :', request.path)
            print('Time of getting answer = ', end - start)
        else:
            response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response