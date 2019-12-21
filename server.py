from http.server import BaseHTTPRequestHandler
from datetime import datetime
import socket

class Server(BaseHTTPRequestHandler):

  def do_GET(self):
      self.resp(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} @ {socket.gethostname()}')

  def resp(self, msg):
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write(bytes(msg, 'UTF-8'))

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('0.0.0.0', 80), Server)
    print('Starting server @ 80, use <Ctrl-C> to stop')
    server.serve_forever()
