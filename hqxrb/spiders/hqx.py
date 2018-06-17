# -*- coding: utf-8 -*-
import json
import time
import scrapy
from hqxrb.items import HqxrbItem

class HqxSpider(scrapy.Spider):
    name = 'hqx'
    allowed_domains = ['app3.qdaily.com']
    type_dict={
    "16":"Top15","17":"设计","1":"长文章","19":"时尚","22":"10个图","3":"娱乐","63":"大公司头条","5":"城市","18":"商业","54":"游戏","4":"智能"
    }
    start_urls = ['http://app3.qdaily.com/app3/categories/index/1/0.json',
                  'http://app3.qdaily.com/app3/categories/index/16/0.json',
                  'http://app3.qdaily.com/app3/categories/index/17/0.json',
                  'http://app3.qdaily.com/app3/categories/index/18/0.json',
                  'http://app3.qdaily.com/app3/categories/index/19/0.json',
                  'http://app3.qdaily.com/app3/categories/index/3/0.json',
                  'http://app3.qdaily.com/app3/categories/index/4/0.json',
                  'http://app3.qdaily.com/app3/categories/index/5/0.json',
                  'http://app3.qdaily.com/app3/categories/index/22/0.json',
                  'http://app3.qdaily.com/app3/categories/index/63/0.json',
                  'http://app3.qdaily.com/app3/categories/index/54/0.json',
                  ]

    def parse(self, response):
        base_next_url = 'http://app3.qdaily.com/app3/categories/index/{}/{}.json'
        type_num=response.url.split("/")[-2]
        dict_rsp = json.loads(response.body.decode())
        next_page = dict_rsp["response"]["last_key"]
        next_url = base_next_url.format(type_num,next_page)
        base_url = 'http://app3.qdaily.com/app3/articles/detail/{}.json'
        # 下一页
        yield scrapy.Request(next_url, callback=self.parse)

        news_list = dict_rsp["response"]["feeds"]
        if news_list:
            for new in news_list:
                content = new["post"]
                item = HqxrbItem()
                item["type"] = self.type_dict[type_num]
                item["id"] = content["id"]
                item["title"] = content["title"]
                item["image"] = content["image"]
                item["publish_time"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(content["publish_time"]))
                item["praise_count"] = content["praise_count"]
                item["comment_count"] = content["comment_count"]
                item["url"] = base_url.format(content["id"])
                yield item
