# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GrouponItem(scrapy.Item):
    # define the fields for your item here like:
    promotion_title = scrapy.Field()
    merchant = scrapy.Field()
    rel_location = scrapy.Field()
    total_ratings = scrapy.Field()
    deal_features = scrapy.Field()
    state = scrapy.Field()
    mini_info = scrapy.Field()
    categories = scrapy.Field()
    url = scrapy.Field()