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
from redis import Redis
from scrapy_redis.spiders import RedisSpider


class Boss(RedisSpider):
    name = "58"
    redis_key = "spider:start_urls"
    allowed_domains = ["bj.58.com"]
    
    def parse(self,response):
        r = Redis()
        sel = Selector(response)
        sites = sel.xpath('//p[@class="bthead"]')
        for site in sites:
            info_url = site.xpath('a[@class="t"]/@href').extract()[0]
            r.lpush('spider:item',info_url)
        next_url = sel.xpath('//a[@class="next"]/@href').extract()[0]
        time.sleep(4)
        r.lpush('spider:start_urls',next_url)
        #yield Request(next_url,callback=self.parse)
