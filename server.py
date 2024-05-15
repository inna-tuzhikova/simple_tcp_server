from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn


class MyTCPHandler(BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        self.request.sendall(data[::-1])


class ThreadedServer(TCPServer, ThreadingMixIn):
    pass


host = 'python_tcp_server'
port = 8080

with ThreadedServer((host, port), MyTCPHandler) as server:
    server.serve_forever()
