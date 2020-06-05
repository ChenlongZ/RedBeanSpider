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

    def start_requests(self):
        urls = HOME_URL
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # TODO: 1. get cookies and redirection URL; 2 use cookies and issue request to redirection URL
    def parse(self, response):
        cookie = response.headers.getlist('Set-Cookie')
        cookie1 = response.headers.getlist('set-cookie')
        self.log(cookie)
        self.log(cookie1)
        # FormRequest.from_reponse(
        #     response,
        #     formdata=
        # )
