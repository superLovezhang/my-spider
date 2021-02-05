import scrapy


class MyProjectItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    rate = scrapy.Field()
