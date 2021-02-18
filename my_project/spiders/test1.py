import time

import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://exercise.kingname.info/exercise_middleware_ua']

    def parse(self, response):
        print(response.text)
        # yield response.follow('http://exercise.kingname.info/exercise_middleware_ua?time=%s'%time.time(), self.parse)