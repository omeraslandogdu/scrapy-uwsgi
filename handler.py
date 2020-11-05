import json
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
import tornado.web, tornado.httpserver
from scrapyscript import Job,Processor
from scrapy import cmdline
from crawler.spiders.crawler import CrawlerSpider
from twisted.internet import defer, reactor
import sys
from importlib import reload
reload(sys)


def set_default_headers(request):
    request.set_header("Access-Control-Allow-Origin", "*")
    request.set_header("Access-Control-Allow-Credentials", "true")
    request.set_header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    request.set_header("Access-Control-Allow-Headers", "Content-Type, Depth, User-Agent, X-File-Size, X-Requested-With, X-Requested-By, If-Modified-Since, X-File-Name, Cache-Control")
    request.set_header('Content-Type', 'application/json')


def create_response(status, message, *args, **kwargs):
    response = dict()
    response['status'] = status
    response['message'] = message
    if kwargs:
        response.update(kwargs)
    return response


class CrawlerHandler(tornado.web.RequestHandler):
    def post(self):
        set_default_headers(self)
        result = dict()
        try:
            body = eval(self.request.body)
        except Exception as e:
            print("Error", str(e))
            body = None

        items = {}

        @defer.inlineCallbacks
        def crawl():
            yield runner.crawl(CrawlerSpider, urls=body['urls'], items=items)
            reactor.crash()

        configure_logging()
        config = get_project_settings()
        config.update({
        'REDIRECT_ENABLED': bool(body['redirect_enabled'])
        })
        runner = CrawlerRunner(settings=config)
        crawl()
        reactor.run()

        try:
            result['status'] = "success"
            result['message'] = "Crawl Ok!"
            result['items'] = json.loads(json.dumps(items))
            self.write(create_response(status='success', message=result))
        except Exception as e:
            result['status'] = "error"
            result['message'] = str(e)
            self.write(create_response(status='error', message=result))
