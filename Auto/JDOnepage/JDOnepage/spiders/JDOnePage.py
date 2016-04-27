# - * - coding: utf-8 - * -


from scrapy.spiders import CrawlSpider
from JDOnepage.items import JdOnepageItem
from scrapy.selector import Selector
from scrapy.http import Request
import requests
import linecache
import re, json
#global price
#price = 0
global URL
URL = 0
global product_id
product_id = 1905319
global TMS
TMS =0
global product
product =0
f = open('JDOnepageDoc.csv','w')
f.truncate()

class JdOnepage(CrawlSpider):
    name = "JDOnepage"    
    start_urls = ['http://item.jd.com/1905319.html']
     
    def parse(self, response): 
        item = JdOnepageItem()
        selector = Selector(response)
        #product_id = selector.xpath('//*[@id="parameter2"]/li[2]/text()').extract()
        name = selector.xpath('//*[@id="parameter2"]/li[1]/@title').extract()
        #price = selector.xpath('//*[@id="jd-price"]/text()').extract()
        saler = selector.xpath('//*[@id="extInfo"]/div[2]/em/text()').extract()
        type1 = selector.xpath('//*[@id="root-nav"]/div/div/strong/a/text()').extract()
        #type21 = selector.xpath('//*[@id="root-nav"]/div/div/span[1]/a[1]/text()').extract()
        type22 = selector.xpath('//*[@id="root-nav"]/div/div/span[1]/a[2]/text()').extract()
        #type23 = selector.xpath('//*[@id="root-nav"]/div/div/span[2]/a[1]/text()').extract()
        #type24 = selector.xpath('//*[@id="root-nav"]/div/div/span[2]/a[2]/text()').extract()
        #global price
        global TMS
        global URL
        global product_id
        global product
        print product_id
        json_url = 'http://p.3.cn/prices/mgets?skuIds=J_' + str(product_id)
        r = requests.get(json_url).text
        data = json.loads(r)[0]
        price = data['m']
        item['num_id'] = TMS
        item['name'] = name
        item['price'] = price
        item['product_id'] = product_id
        item['saler'] = saler
        item['URL'] = URL
        item['Type1'] = type1
        item['Type2'] = type22
        if(TMS>0):
            yield item
        TMS+=1
        
        f = open("JDSpiderDoc.csv", "r")
        if(TMS<len(f.readlines())):
            line = linecache.getline("JDSpiderDoc.csv",TMS+1)
            price = 0
            product_id=0
            URL=0 
            product = line.split(',')
            if product[-1].strip()=='':
                TMS+=1
                line = linecache.getline("JDSpiderDoc.csv",TMS+1)
                product = line.split(',')
            nextLink = "http://item.jd.com/"+product[-1].strip()+".html"
            #price = product[0]
            URL = nextLink
            product_id = product[-1].strip()
            yield Request(nextLink,self.parse)
            f.close()
        else:
            exit()