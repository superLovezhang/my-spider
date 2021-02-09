import scrapy

class cookieSpider(scrapy.Spider):
    name = "cookiespider"
    start_urls = ['http://exercise.kingname.info/exercise_login_success']

    def parse(self, response, **kwargs):
        print(response.text)