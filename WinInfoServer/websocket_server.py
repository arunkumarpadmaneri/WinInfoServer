import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import json
from printer_control import get_sys_info
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection')
        self.write_message("Connection Opened")
      
    def on_message(self, message):
        print ('message received:',type(message))
        msg = json.loads(message)
        print("msg",msg)
        response = get_sys_info(msg['win32classname'],msg['props'])
        response_dict = json.dumps(response)
        # self.set_default_printer(message)
        # Reverse Message and send it back
        print ('sending back message',response_dict)
        self.write_message(response_dict)
 
    def on_close(self):
        print ('connection closed')
      
    def check_origin(self, origin):
        return True
 
 

if __name__ == "__main__":
# def main():
    application = tornado.web.Application([
        (r'/ws', WSHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()