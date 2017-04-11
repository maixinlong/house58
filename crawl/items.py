# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlItem(scrapy.Item):
    distance = scrapy.Field() #离地铁距离
    price = scrapy.Field()   #单价
    total = scrapy.Field() #总价
    area = scrapy.Field()  #面积大小
    name = scrapy.Field()  #区名称
    line = scrapy.Field() #地铁线
    
    