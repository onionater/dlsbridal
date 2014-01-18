#!/usr/bin/env python
import sys
print sys.version
print sys.path
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ['/cgi-bin', '/htbin']
print "amy's server is serving..."
httpd = server(server_address, handler)
httpd.serve_forever()
