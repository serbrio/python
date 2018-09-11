#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)

from http.server import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser

name = "some"


def ml_sorter(line):
    try:
        final = []
        others = []
        items = [pair.strip() for pair in line.split('\t') if pair]
        for item in items:
            if "type:" in item:
                final.insert(0, item)
            elif "label:" in item:
                final.append(item)
            else:
                others.append(item)
        others.sort()
        final.extend(others)
        return final
    except:
        return line


class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        request_path = self.path

        if name in request_path:
            print("\n----- Request Start ----->\n")
            print("Request path:", request_path)
            print("Request headers:", self.headers)
            print("<----- Request End -----\n")
        
        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")
        self.end_headers()
        
    def do_POST(self):
        
        request_path = self.path

        if name in request_path:
            print("\n----- Request Start ----->\n")
            print("Request path:", request_path)
        
        request_headers = self.headers
        content_length = request_headers.get('Content-Length')
        length = int(content_length) if content_length else 0

        if name in request_path:
            print("Content Length:", length)
            print("Request headers:", request_headers)
            body_raw = self.rfile.read(length)
            body_str = body_raw.decode("utf-8")
            body_lines = body_str.split('\n')
            for line in body_lines:
                print(ml_sorter(line))
            #print("Request payload:", self.rfile.read(length))
            print("<----- Request End -----\n")
        
        self.send_response(200)
        self.end_headers()
    
    do_PUT = do_POST
    do_DELETE = do_GET
        
def main():
    port = 5555
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

        
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()
    
    main()
