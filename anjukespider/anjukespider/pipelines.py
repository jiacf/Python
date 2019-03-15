# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AnjukespiderPipeline(object):
    exchange_rate = 8.8893
    def process_item(self, item, spider):
        item['money'] = 'Y%0.2f'%(float(item['money']) * self.exchange_rate)
        return item

class bookspiderPipline():
    def open_spider(self,spider):
        self.file = open('book_info.txt','w')
    def process_item(self,item,spider):
        self.file.write(str(item))
    def close_spider(self,spifrt):
        self.file.close()