import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import base64
import cv2
import simplejson
import numpy as np
from CircleDetection import CircleDetect

class WebSocketServer(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        base64img = message
        img = data_uri_to_cv2_img(base64img)
        circles = CircleDetect(img)
        print circles
        print simplejson.dumps(circles)
        self.write_message(simplejson.dumps(circles))

    def on_close(self):
        print("WebSocket closed")


def serve_forever():
    global server
    application = tornado.web.Application(
        [
            (r'/', WebSocketServer),
        ]
    )
    application.listen(8000)
    server = tornado.ioloop.IOLoop.instance()
    server.start()


def data_uri_to_cv2_img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, 1)
    return img

if __name__ == '__main__':
    serve_forever()
