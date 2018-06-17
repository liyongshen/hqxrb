# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HqxrbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    id = scrapy.Field()
    image = scrapy.Field()
    title = scrapy.Field()
    comment_count = scrapy.Field()
    praise_count = scrapy.Field()
    url = scrapy.Field()
    publish_time = scrapy.Field()
