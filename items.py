import scrapy
from scrapy.loader.processors import TakeFirst


class LeroyItem(scrapy.Item):
    _id = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    file_name = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field()
    params1 = scrapy.Field()
    params2 = scrapy.Field()
    params = scrapy.Field()
    price = scrapy.Field()
