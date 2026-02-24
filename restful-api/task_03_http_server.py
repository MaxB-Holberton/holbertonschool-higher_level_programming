#!/usr/bin/env python3
"""
    module to show the basics for http.server
"""
import http.server
import json


class BasicServer(http.server.BaseHTTPRequestHandler):
    """
        the BasicServer class
    """
    def do_GET(self):
        """
            the http.server GET Method with different paths
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Hello, this is a simple API!'.encode())

        elif self.path == '/data':
            simple_dataset = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(simple_dataset).encode())

        elif self.path == '/info':
            dataset = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(dataset).encode())

        elif self.path == '/status':
            dataset = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
            self.send_response(200)
            self.wfile.write('Ok'.encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('404 Not Found'.encode())



if __name__ == '__main__':
    new_server = http.server.HTTPServer(('', 8000), BasicServer)
    new_server.serve_forever()
