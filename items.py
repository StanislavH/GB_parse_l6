import scrapy
from scrapy.loader.processors import TakeFirst, Join, MapCompose


class leroymerlinparserItem(scrapy.Item):
    def filter_price(value):
        value = ''.join(value).replace(" ", '')
        return float(value)

    def del_whitespace(value):
        for i in range(len(value)):
            value[i] = str(value[i]).replace('  ', '').replace("\n", '')
        return value

    def sum_params(val1, val2):
        for i in range(len(val1)):
            val1[i] = ([val1[i], val2[i]])
        return val1

    # define the fields for your item here like:
    _id = scrapy.Field()
    namee = scrapy.Field()
    photos = scrapy.Field()
    params1 = scrapy.Field(input_processor=del_whitespace,
                           output_processor=TakeFirst(), )
    params2 = scrapy.Field(input_processor=del_whitespace,
                           output_processor=TakeFirst(), )
    params = scrapy.Field(#input_processor=sum_params,
                          #output_processor=TakeFirst(),
                          )
    price = scrapy.Field(
        input_processor=filter_price,
        output_processor=TakeFirst(),
    )
    print(namee, photos, params, price)
    pass
