from scrapy import signals
from scrapy.utils.project import get_project_settings
from scrapy.http import Request
import random, logging, time
from .src.cookieUtils import CookieUtils

settings = get_project_settings()

class MyProjectSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MyProjectDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


"""
处理请求IP的下载中间件
"""
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(settings['PROXIES'])
        request.meta['proxy'] = proxy


"""
处理User-Agent的下载中间件
"""
class DoubanDownloaderMiddleware(object):
    def process_request(self, request, spider):
        time.sleep(5)
        request.headers['User-Agent'] = random.choice(settings['USER_AGENT_LIST'])
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        return request


"""
处理cookie的下载中间件
"""
class CookieMiddleware:
    def process_request(self, request: Request, spider):
        if (spider.name == 'cookiespider'):
            cookies = CookieUtils.getCookies()
            logging.info("===================================被cookie中间件处理, cookie是%s"%cookies)
            request.cookies = cookies
        return None