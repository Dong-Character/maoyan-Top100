# -*- coding: utf-8 -*-
import scrapy

from Maoyan.items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['manyan.com']
    # start_urls = ['http://www.manyan.com/']
    def start_requests(self):
        for i in range(5):
            url = 'https://maoyan.com/board/4?offset={}'.format((i-1)*10)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    def parse(self, response):
        # 基准解析
        dd_list = response.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
        # print(dd_list)
        for dd in dd_list:
            item = MaoyanItem()
            item['name'] = dd.xpath('./a/@title').get()
            item['star'] = dd.xpath('./div/div/div[1]/p[2]/text()').get().strip()
            item['time'] = dd.xpath('./div/div/div[1]/p[3]/text()').get().strip()[6:15]
            yield item