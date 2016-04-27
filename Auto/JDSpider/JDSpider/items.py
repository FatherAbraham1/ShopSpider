# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:

    #产品id
    product_id = scrapy.Field()
    #正价
    price = scrapy.Field()
    #名称
    name = scrapy.Field()



