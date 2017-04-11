# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from db.mgdb import get_db

class CrawlPipeline(object):
    def __init__(self):
        self.db = get_db()
    
    def process_item(self, item, spider):
        """
        spider.name
        """
        line,distance = self.__redistance(item['distance'])
        item['distance'] = distance
        item['line'] = line
        item['price'] = self.__reprice(item['price'])
        item['total'] = float(item['total'])
        item['area'] = self.__area(item['area'])
        self.db.insert(dict(item))
        return item

    def __redistance(self,str):
        line = 0
        distance = 0
        p = re.compile(r'\d+')
        if u'亦庄线' in str:
            line = 20
            distance = p.findall(str)[0]
        elif u'昌平线' in str:
            line = 21
            distance = p.findall(str)[0]
        elif u'八通线' in str:
            line = 22
            distance = p.findall(str)[0]
        elif u'大兴线' in str:
            line = 23
            distance = p.findall(str)[0]
        elif u'房山线' in str:
            line = 24
            distance = p.findall(str)[0]
        else:
            try:
                line,distance = p.findall(str)
            except Exception,e:
                print 'distance err:',e,str
        return int(line),int(distance)
    
    def __reprice(self,str):
        price = 0
        p = re.compile(r'\d+')
        try:
            price = int(p.findall(str)[0])
        except Exception,e:
            print 'price err:',e,str
        return price
    
    def __area(self,str):
        p = re.compile(r'\d+')
        try:
            str = float(p.findall(str)[0])
        except Exception,e:
            print 'area err',e
        return str