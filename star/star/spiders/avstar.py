# -*- coding: utf-8 -*-
import scrapy
from ..items import StarItem
import re

class AvstarSpider(scrapy.Spider):
    name = 'avstar'
    #allowed_domains = ['https://www.seedmm.work']

    @property
    def start_urls(self):
        return ['https://www.seedmm.work/actresses/{}'.format(i) for i in range(1, 200)]

    def parse(self, response):

        for avstar in response.css('a.avatar-box'):
            item = StarItem(
#                name = avstar.css('div.photo-info span::text').extract_first().strip(),

#                image_urls = avstar.css('div.photo-frame img::attr(src)').extract_first()
            )
            url = response.css('a.avatar-box::attr(href)').extract_first()
            request = scrapy.Request(url, self.parse_star)
            request.meta['item'] = item
            yield request

            for url in response.css('a.avatar-box::attr(href)').extract():
                request = scrapy.Request(url, self.parse_star)
                request.meta['item'] = item
                yield request


    def parse_star(self, response):
        item = response.meta['item']
        item['image_urls'] = response.css('div.photo-frame img::attr(src)').extract_first()
        item['name'] = response.css('div.avatar-box div.photo-info span::text'
                ).extract_first().strip()
#        item['birthday'] = response.css('div.avatar-box div.photo-info p::text'
#                ).re_first('生日: (.+)')

        d = {}
        for i in response.css('div.avatar-box div.photo-info p::text').extract():
            k, v = i.split(': ')
            d[k] = v
        item['birthday'] = d.get('生日', None)
        item['cup'] = d.get('罩杯', None)

        height = d.get('身高', None)
        if not height:
            item['height'] = 0
        else:
            item['height'] = re.findall('(\d*)cm', height)[0]

        bust = d.get('胸圍', None)
        if not bust:
            item['bust'] = 0
        else:
            item['bust'] = re.findall('(\d*)cm',d.get('胸圍', None))[0]

        waist = d.get('腰圍', None)
        if not waist:
            item['waist'] = 0
        else:
            item['waist'] = re.findall('(\d*)cm',d.get('腰圍', None))[0]

        hips = d.get('臀圍', None)
        if not hips:
            item['hips'] = 0
        else:
            item['hips'] = re.findall('(\d*)cm',d.get('臀圍', None))[0]

        yield item
