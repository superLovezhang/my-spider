import scrapy
from scrapy.http.response.html import HtmlResponse
from ..items import MyProjectItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/编程?start=0&type=T']
    start_index = 0

    def parse(self, response: HtmlResponse):
        self.start_index += 20
        index = self.start_index
        for box in response.xpath('//div[@class="info"]'):
            item = MyProjectItem()
            item['title'] = box.xpath('./h2/a|span/text()').get()
            item['rate'] = box.xpath('./div[@class="star clearfix"]/span[2]/text()').get()
            item['description'] = box.xpath("./p/text()").get()
            infos = box.xpath('./div[1]/text()').get().split('/')
            item['price'] = infos[len(infos) - 1]
            yield item
        # return response.follow('https://book.douban.com/tag/编程?start=%d&type=T'%index, self.parse)