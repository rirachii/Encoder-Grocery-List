import re
from util.request import Request
from util.response import generate_response

class Router():

    def __init__(self):
        self.routes = []
        self.route_404 = Route('', '', four_oh_four)

    def add_route(self, route):
        self.routes.append(route)

    def handle_request(self, request: Request, handler):
        for route in self.routes:
            if route.is_request_match(request):
                route.handle_request(request, handler)
                return
        self.route_404.handle_request(request, handler)


class Route:
    def __init__(self, method, path, action):
        self.method = method
        self.path = path
        self.action = action

    def is_request_match(self, request: Request):
        if request.method != self.method:
            return False
        search_result = re.search("^" + self.path, request.path)
        if search_result:
            return True
        else:
            return False

    def handle_request(self, request: Request, handler):
        self.action(request, handler)

def four_oh_four(_, handler):
    response = generate_response(b"The requested content does not exist", "text/plain; charset=utf-8", "404 Not Found")
    handler.request.sendall(response)