from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class PackageNotFoundError(ValueError):
    pass


def find_package(name):
    raise PackageNotFoundError(name)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        name = self.path.s
        package = find_package()
        self.send
