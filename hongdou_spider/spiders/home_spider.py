import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import FormRequest

HOME_URL = [
    'https://www.2redbeans.com/zh-CN/app/login',
]


class RbSpider(CrawlSpider):
    name = "rb"

    http_user = 'z.f.antory@tom.com'
    http_pass = 'n0t3st'

    handle_httpstatus_list = [301, 302]

    def start_requests(self):
        urls = HOME_URL
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # TODO: 1. get cookies and redirection URL; 2 use cookies and issue request to redirection URL
    def parse(self, response):
        cookie = response.headers.getlist('Set-Cookie')
        self.log(cookie)
