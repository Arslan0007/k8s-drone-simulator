# main.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Change this variable for the v2 update later
VERSION = "v1.0 - FLIGHT NORMAL"

class DroneHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # The response includes the pod name so we see which drone is answering
        pod_name = os.getenv('HOSTNAME', 'unknown-drone')
        message = f"Drone ID: {pod_name} | Status: {VERSION}\n"
        self.wfile.write(message.encode())

def run():
    print('Starting Drone System...')
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, DroneHandler)
    print(f'Drone Radio Active on port 8080. Version: {VERSION}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()