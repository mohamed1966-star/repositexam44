from datetime import datetime
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from Model import Model
from Field import *
from Database import Database

Model.db = Database('database.sqlite')
Model.connection = Model.db.connect()

PORT = 8000


class Post(Model):
    title = CharField()
    body = TextField()
    created_at = DateTimeField()
    published = BooleanField()


class User(Model):
    first_name = CharField()
    last_name = CharField(max_length=255)
    age = IntegerField()


if __name__ == '__main__':

    class MyHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/posts':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(Post.all()).encode('utf-8'))


    with HTTPServer(('',PORT), MyHandler) as httpd:
        print('Serving at port', PORT)
        httpd.serve_forever()

