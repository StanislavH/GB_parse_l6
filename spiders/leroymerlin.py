import scrapy
from scrapy.http import HtmlResponse
from leroymerlinparser.items import leroymerlinparserItem
from scrapy.loader import ItemLoader
import time


class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self):
        self.start_urls = [f'https://leroymerlin.ru/catalogue/elektrotovary/']

    def parse(self, response: HtmlResponse):
        ads_links = response.xpath(
            '//a[@class="bex6mjh_plp b1f5t594_plp p5y548z_plp pblwt5z_plp nf842wf_plp"]/@href').extract()
        for link in ads_links:
            time.sleep(3)
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=leroymerlinparserItem(), response=response)
        loader.add_css('namee', 'h1.header-2::text')
        loader.add_xpath('photos', '//*/picture[@slot="pictures"]/source[1]/@srcset')
        loader.add_xpath('params1', '//*/uc-pdp-section-vlimited/dl/div[@class="def-list__group"]/dt/text()')
        loader.add_xpath('params2', '//*/uc-pdp-section-vlimited/dl/div[@class="def-list__group"]/dd/text()')
        params = []
        params1 = loader.get_collected_values("params1")
        params2 = loader.get_collected_values("params2")
        for i in range(len(params1)):
            params.append([params1[i], params2[i]])
        #loader.add_value('params', loader.get_collected_values('params1'), loader.get_collected_values('params2'))
        loader.add_value('params', params)
        loader.add_xpath('price', '//span[@slot="price"][1]/text()')
        print(loader.get_collected_values('namee'), loader.get_collected_values('params'),
              loader.get_collected_values('photos'), loader.get_collected_values('price'))
        yield loader.load_item()
