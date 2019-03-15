import scrapy

class HttpSpider(scrapy.Spider):
    name = 'html'
    start_urls = 'http://httpbin.org/get'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    def start_requests(self):
        yield scrapy.Request(self.start_urls,callback=self.parse,headers=self.headers)
    def parse(self, response):
        print(response.text)