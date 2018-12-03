from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    return ["Hello my friend!\n".encode("utf-8"), "Second sentence".encode("utf-8")]


server = make_server('localhost', 8080, application)
server.serve_forever()

import numpy as np

x = np.arange(10.4)