# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    birthday = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
    height = scrapy.Field()
    cup = scrapy.Field()
    bust = scrapy.Field()
    waist = scrapy.Field()
    hips = scrapy.Field()


class PicDownload(scrapy.Item):
    images = scrapy.Field()
    image_urls = scrapy.Field()
