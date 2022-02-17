
from email.headerregistry import Address
import http.server
#import socketserver

port = 80
Address=("",port)

server=http.server.HTTPServer

handler=http.server.CGIHTTPRequestHandler # OU SimpleHTTPRequestHandler pour serveur simple
#httpd = socketserver.TCPServer(Address,handler)

handler.cgi_directories=["/"]

httpd=server(Address, handler)

print(f"serveur ok {port}")

httpd.serve_forever()
