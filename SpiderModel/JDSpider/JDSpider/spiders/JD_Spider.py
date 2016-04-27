# - * - coding: utf-8 - * -
from scrapy.spiders import CrawlSpider
from JDSpider.items import JdspiderItem
from scrapy.selector import Selector
from scrapy.http import Request
import requests
import re, json
global count
count=0
global tot_item
tot_item=0
global trg_item
trg_item=0

f = open('F:\\Program_Stores\\Python\\2016-04-26\\Auto\\DataWare\\JDTotal\\$$query$$.csv','w')
f.truncate()
class JdSpider(CrawlSpider):
    name = "JDSpider"
    start_urls = ["http://search.jd.com/s_new.php?keyword=$$query$$&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=3&page=1&s=26&scrolling=y&pos=30"]

    def parse(self, response):
        global count
        global tot_item
        global trg_item
        tot_item=0
        trg_item=0
        
        item = JdspiderItem()
        selector = Selector(response)
        Pages = selector.xpath('/html/body/li')
        for each in Pages:						
            product_id = each.xpath('@data-sku').extract()
            name = each.xpath('div/div[3]/a/em/text()').extract()
            price = each.xpath('div/div[2]/strong/i/text()').extract()
            item['name'] = name
            item['product_id'] = product_id
            item['price'] = price
            
            tot_item+=1
            if '$$query$$' in name:
            	  trg_item+=1
            yield item
        count+=1   
        print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' 
        print count 
        print 'http://search.jd.com/s_new.php?keyword=$$query$$&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=3&page='+str(count)+'&s=26&scrolling=y&pos=30' 
        print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' 
        if (tot_item*0.5>trg_item) and (count<=10):
        		yield Request('http://search.jd.com/s_new.php?keyword=$$query$$&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=3&page='+str(count)+'&s=26&scrolling=y&pos=30',callback=self.parse)
