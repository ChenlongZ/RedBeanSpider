import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import FormRequest
from scrapy.http import Request

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
        print(response.body)
        # self.log(response.body)

        # send request
        request_with_cookies = Request(callback=self.parse, url="https://www.2redbeans.com/zh-CN/app/search", cookies={'_dating_session':'a3pVZ1R5MjBrUnlHVXRsSjAzdFh1ZkdYN0lscVNTaUdNMFc0N1pZWldOMys5NGRTd2NtV0hYYWtkTmJvZmJsSG9UbjVzK0VhSnJrV0xoQ0JLWlRlZnJQWmxIdUZrVzBMN1dJUytZcTRzTHFHNnB0Z093SWJiZ2hLdVhEUE85TnhsQ1lJb1ZoR05sWmtQeW5YTERxcDBmTExjeEpJWGtQQ0lhSVowSXRaOTZvL1FkaUUxWkhzNmRlS1NSWWNuY25XUGpsT092RzF6OW1HMUdCRFFKRmJTMksrVTVLK1plMVY3Y0FVYS8xRVQyWFBDK01XR3BLdUNEM1YzVnhVUHBVTnVJV1JVVFNqdzUwRDlENmNFa0c1Wk9hTk1YTjVPZjlxQVJEdGpVaXJxbEpmb2NoWjdQTDlRY0U3SmFFSytVZHFsSiszK1ZUWTFlWlJibFZOQ1FRQXV2UVYwTG8xRlErWTZ2aDJ2MDJlbkI0PS0tdVdLR1AzS3ZDZVVCdnoxTzEveEhZdz09--4c0d9e36f567f6d2f4248e6ee60ea44bfebff134; path=/; HttpOnly'})
        yield request_with_cookies

    def parse_1(self, response):
        self.log(response.body)