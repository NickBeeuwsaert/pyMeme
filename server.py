#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import argparse
from meme import *
import json

class MemeGenerator(tornado.web.RequestHandler):
    def prepare(self):
        self.options = {"meme":"forever-alone","top":"", "bottom":""}
        
    def generate(self):
        
        self.add_header("Content-Type", "image/png");
        surface = create_meme(self.options["meme"], self.options["top"], self.options["bottom"]);
        surface.write_to_png(self);
        surface.finish();
class MainHandler(MemeGenerator):
    def get(self):
        meme = self.get_argument("meme", "forever-alone")
        top = self.get_argument("top","")[:256]; # cut it off at 256 characters long...
        bottom= self.get_argument("bottom", "")[:256];
        self.options = {"meme": meme, "top": top, "bottom": bottom}
        self.generate();

class JSONHandler(MemeGenerator):
    def get(self, jsonOptions):
        try:
            self.options.update(json.loads(jsonOptions))
        except:
            pass
        self.generate()
application = tornado.web.Application([
    (r"/api/", MainHandler),
    (r"/api/json/(.*)", JSONHandler),
])

if __name__ == "__main__":
    parser = argparse.ArgumentParser();
    parser.add_argument("--address","-a", type=str, help="The address to listen on, defaults to 127.0.0.1", default="127.0.0.1");
    parser.add_argument("--port","-p", type=int, help="The port to listen on, defaults to 8888", default=8888);
    args = parser.parse_args()
    application.listen(args.port, args.address)
    tornado.ioloop.IOLoop.instance().start()
