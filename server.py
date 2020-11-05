# -*- coding: utf-8 -*-
import tornado.web
import tornado.httpserver
from tornado.options import define, options
from twisted.internet import reactor
from handler import CrawlerHandler
import sys
from importlib import reload

reload(sys)

define("port", 8080, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/crawl", CrawlerHandler)
        ]

        settings = dict(
            debug=True,
            xsrf_cookies=False,
        )

        tornado.web.Application.__init__(self, handlers, **settings)

        self.information()

    def information(self):
        info_list = ["> Tornado Server %s" % tornado.version,
                     "> Port : %s" % options.port,
                     "> Debug Mode : %s" % self.settings.get('debug'),
                     "Listening now.."]

        for info in info_list:
            print(info)

        return


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), no_keep_alive=True)

    http_server.listen(options.port)

    # multi core
    # http_server.bind(options.port)
    # http_server.start(0)

    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
