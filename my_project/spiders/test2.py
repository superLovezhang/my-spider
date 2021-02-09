import scrapy

class test2(scrapy.Spider):
    name = 'ipspider'
    index = 3
    start_urls = ['http://exercise.kingname.info/exercise_middleware_ip/1']

    def parse(self, response, **kwargs):
        self.index += 1
        index = self.index
        print(response.text, index)
        yield response.follow('http://exercise.kingname.info/exercise_middleware_ip/%d'%index, self.parse)