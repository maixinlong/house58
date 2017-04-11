#! /usr/bin/env python
#coding=utf-8
from scrapy.spider import Spider
from scrapy.selector import Selector
#from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.http import Request
import time
from crawl.items import CrawlItem


class Boss(BaseSpider):
    name = "58"
    allowed_domains = ["bj.58.com"]
    start_urls = [
        #"http://bj.58.com/chaoyang/ershoufang/?PGTID=0d30000c-0000-1957-7571-5a30f1f9daf0&ClickID=3",
        "http://bj.58.com/ershoufang/?PGTID=0d100000-0000-1df4-97d7-ca2d4c91a772&ClickID=1",
        "http://bj.58.com/ershoufang/pn2/?PGTID=0d30000c-0000-1846-8574-01abd0ae881d&ClickID=2",
        #'http://www.baidu.com',
    ]
    
    def parse(self,response):
        sel = Selector(response)
        sites = sel.xpath('//p[@class="bthead"]')
        for site in sites:
            info_url = site.xpath('a[@class="t"]/@href').extract()[0]
            yield Request(info_url,callback=self.pparse_info)
        next_url = sel.xpath('//a[@class="next"]/@href').extract()[0]
        print 'next_url:',next_url
        yield Request(next_url,callback=self.parse)
            
    def pparse_info(self,response):
        sel = Selector(response)
        item = CrawlItem()
        item["total"] = sel.xpath('//p[@class="house-basic-item1"]/span[1]/text()').extract()[0]
        item["price"] = sel.xpath('//p[@class="house-basic-item1"]/span[2]/text()').extract()[0]
        item["area"] = sel.xpath('//p[@class="area"]/span[@class="main"]/text()').extract()[0]
        item["name"] = sel.xpath('//ul[@class="house-basic-item3"]/li/span[2]/a[1]/text()').extract()[1]
        item["distance"] = sel.xpath('//span[@class="f12 c_999 mr_10"]/text()').extract()[0]
        yield item
        
