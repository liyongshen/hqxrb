# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from hashlib import sha1

class HqxrbPipeline(object):
    def open_spider(self,spider):
        self.f = open("hqx.json","w")
        self.f.write("[")
        self.set=set()

    def process_item(self, item, spider):
        code = self.filter(item)
        if code in self.set:
            return
        else:
            item = json.dumps(dict(item),ensure_ascii=False)
            self.f.write(item+",\n")
            self.set.add(code)
            # print(code)
            return item

    def close_spider(self,spider):
        self.f.write("]")
        self.f.close()

    def filter(self,item):
        item_dict = dict(item)
        sha = sha1()
        # 有些新闻属于多种分类
        # sha.update(item_dict["type"].encode('utf-8'))
        sha.update(str(item_dict["id"]).encode('utf-8'))
        sha.update(item_dict["image"].encode('utf-8'))
        sha.update(item_dict["title"].encode('utf-8'))
        sha.update(str(item_dict["comment_count"]).encode('utf-8'))
        sha.update(str(item_dict["praise_count"]).encode('utf-8'))
        sha.update(item_dict["url"].encode('utf-8'))
        sha.update(item_dict["publish_time"].encode('utf-8'))
        return sha.hexdigest()