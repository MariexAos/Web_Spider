# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
       # print('结果返回')
        print(response)
        print(type(response))
      #  print('结果结束')
        html = str(response.body,encoding="utf8")
        with open("baidu.html","w",encoding="utf8")as f:
            f.write(html)
