from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from Leroy.items import LeroyItem
from urllib.parse import urljoin
from scrapy.loader.processors import MapCompose, Compose, Join


class LeroySpider(CrawlSpider):
    name = 'leroymerlin'
    start_urls = [f'https://leroymerlin.ru/catalogue/elektrotovary/']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths='//a[@class="bex6mjh_plp s15wh9uj_plp l7pdtbg_plp r1yi03lb_plp sj1tk7s_plp"]')),
        Rule(
            LinkExtractor(restrict_xpaths='//a[@class="bex6mjh_plp b1f5t594_plp p5y548z_plp pblwt5z_plp nf842wf_plp"]'),
            callback='parse_item')
    )

    def parse_item(self, response):
        item_loaded = ItemLoader(item=LeroyItem(), response=response)
        item_loaded.add_xpath('file_name', '//h1/text()', MapCompose(lambda i: i.replace(':', '')))
        item_loaded.add_xpath('file_urls', '//*/picture[@slot="pictures"]/source[1]/@srcset',
                              MapCompose(lambda i: urljoin(response.url, i)))

        item_loaded.add_value('file_name', '1.jpg')
        item_loaded.add_xpath('params1', '//*/uc-pdp-section-vlimited/dl/div[@class="def-list__group"]/dt/text()')
        item_loaded.add_xpath('params2', '//*/uc-pdp-section-vlimited/dl/div[@class="def-list__group"]/dd/text()',
                              MapCompose(lambda i: i.replace('\n', ''), lambda i: i.replace('  ', '')))
        item_loaded.add_value('params', [
            [item_loaded.get_collected_values("params1")[i], item_loaded.get_collected_values("params2")[i]]
            for i in range(len(item_loaded.get_collected_values("params1")))
        ])
        item_loaded.add_value('url', response.url)
        item_loaded.add_xpath('price', '//span[@slot="price"][1]/text()', MapCompose(Join(), lambda i: i.replace(' ', ''), lambda i: float(i)))

        return item_loaded.load_item()
