# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaijiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class AuthItem(scrapy.Item):
    authName = scrapy.Field()
    classification = scrapy.Field()


class ArticleItem(scrapy.Item):
    article_title = scrapy.Field()
    article_abstract = scrapy.Field()
    article_href = scrapy.Field()
    pic_href = scrapy.Field()
    auth_name = scrapy.Field()

