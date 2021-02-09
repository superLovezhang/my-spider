import scrapy, time
from scrapy.http import HtmlResponse


class Test1Spider(scrapy.Spider):
    name = 'test1'
    index = 0
    allowed_domains = ['http://exercise.kingname.info/exercise_middleware_ua']
    start_urls = ['http://exercise.kingname.info/exercise_middleware_ua']

    def parse(self, response: HtmlResponse):
        print(response.text, "==========================================")
        # ++self.index
        # if (self.index >= 10):
        #     return
        return response.follow('https://book.douban.com/tag/编程?start=%d&type=T'%20, self.parse)
