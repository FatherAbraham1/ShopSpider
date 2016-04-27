# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdOnepageItem(scrapy.Item):
    # define the fields for your item here like:

    #行号id
    num_id = scrapy.Field()
    #商品id
    product_id = scrapy.Field()
    #商品名字
    name = scrapy.Field()
    #正价
    price = scrapy.Field()    
    #销售类型
    saler = scrapy.Field()
    #来源URL
    URL = scrapy.Field()
    #商品大类
    Type1 = scrapy.Field()
    #商品小类
    Type2 = scrapy.Field()




