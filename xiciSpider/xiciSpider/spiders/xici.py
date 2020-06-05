# -*- coding: utf-8 -*-
import scrapy
# todo 1) saving is adding it to the bottom 2) no Chinese

# create class, and herits from scrapy.Spider class (the most basic class, other classes also herit from this class)
# how many classes in scrapy:

# error while run scrapy crawl xici. Go to setting, DEFAULT_REQUEST_HEADERS
# DEBUG: Retrying <GET https://www.xicidaili.com/nn/> (failed 1 times): 503 Service Unavailable

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    # multi-page method 1
    # page_total = response.xpath('//*[@id="body"]/div[3]/a[10]')
    # start_urls = [f'https://www.xicidaili.com/nn/{page}' for page in range(1, page_total)]
    start_urls = ['https://www.xicidaili.com/nn/']

    custom_settings = None

    # analyse; get the data/website; response is from downloader
    def parse(self, response):
        selectors = response.xpath("//tr")
        for selector in selectors:
            ip = selector.xpath("./td[2]/text()").get()
            port = selector.xpath("./td[3]/text()").get()
            address = selector.xpath("./td[4]/text()").get()
            anonymity = selector.xpath("./td[5]/text()").get()
            http_type = selector.xpath("./td[6]/text()").get()
            surviving_time = selector.xpath("./td[9]/text()").get()
            verifying_time = selector.xpath("./td[10]/text()").get()
            # another method
            # ip = selector.xpath("./td[2]/text()").extract_first()
            items = {
                'ip': ip,
                'port': port,
                'address': address,
                'anonymity': anonymity,
                'https_http': http_type,
                'surviving_time': surviving_time,
                'verifying_time': verifying_time,
            }
            yield items
        # next page method 2
        next_page = response.xpath("//a[@class='next_page']/@href").get()  # '/nn/2'
        if next_page.strip('/')[3] < 50:  # 'if next_page:' added, bc none for the last page
            # combine in to full url
            # next_url = 'https://www.xicidaili.com' + next_page
            next_url = response.urljoin(next_page)
            # send out Request; callback*回调函数(不写'()'): give the Response back to self to parse; yield 生成器
            yield scrapy.Request(next_url, callback=self.parse())

