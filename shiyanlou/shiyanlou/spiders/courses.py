# -*- coding: utf-8 -*-
import scrapy

from shiyanlou.items import CourseItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['shiyanlou.com']

    @property
    def start_urls(self):
        url_list = ['https://www.shiyanlou.com/courses/',
                    'https://www.shiyanlou.com/courses/?page_size=20&cursor=bz0yMA%3D%3D',
                    'https://www.shiyanlou.com/courses/?page_size=20&cursor=bz00MA%3D%3D']
        return url_list

    def parse(self, response):
        for course in response.css('div.col-md-3'):
            item = CourseItem({
                'name': course.css('h6::text').extract_first().strip(),
                'description': course.css('div.course-description::text').extract_first().strip(),
                'type': course.css('span.course-type::text').extract_first(default='free').strip(),
                'students': course.css('span.students-count span::text').extract_first()
            })
            yield item
