#! /usr/bin/env python
#coding=utf-8
"""
起多个进程执行本模块
"""
from scrapy.spider import Spider
from scrapy.selector import Selector
#from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.http import Request
import time
from crawl.items import CrawlItem
from redis import Redis
from scrapy_redis.spiders import RedisSpider


class HouseInfo(RedisSpider):
    name = "info"
    redis_key = "spider:item"
    allowed_domains = ["bj.58.com"]
    
    def parse(self,response):
        print 'spider 2:',response.url
        sel = Selector(response)
        item = CrawlItem()
        item["total"] = sel.xpath('//p[@class="house-basic-item1"]/span[1]/text()').extract()[0]
        item["price"] = sel.xpath('//p[@class="house-basic-item1"]/span[2]/text()').extract()[0]
        item["area"] = sel.xpath('//p[@class="area"]/span[@class="main"]/text()').extract()[0]
        item["name"] = sel.xpath('//ul[@class="house-basic-item3"]/li/span[2]/a[1]/text()').extract()[1]
        try:
            item["distance"] = sel.xpath('//span[@class="f12 c_999 mr_10"]/text()').extract()[0]
        except:
            item["distance"] = 'aaaaaa50afdfasaa0'
        yield item
        
