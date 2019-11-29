import scrapy
from ..items import PicDownload


class AvstarImageSpider(scrapy.Spider):
    name = 'pic'

    '''
    @property
    def start_urls(self):
        return ['https://www.seedmm.work/actresses/{}'.format(i) for i in range(1, 3)]
    '''
    start_urls = ['https://www.seedmm.work/actresses/{}'.format(i) for i in range(1, 3)]

    def parse(self, response):
        item = PicDownload()
        item['image_urls'] = response.css('a.avatar-box div.photo-frame img::attr(src)').extract()
        yield item
