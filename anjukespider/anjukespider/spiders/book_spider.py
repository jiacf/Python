import scrapy
from anjukespider.items import AnjukespiderItem
class BookSpider(scrapy.Spider):
    name = 'book_spider'
    start_urls = 'http://books.toscrape.com/'
    def start_requests(self):
        yield scrapy.Request(self.start_urls,callback=self.parse)
    def parse(self, response):
        item = AnjukespiderItem()
        html = response.css('.col-md-9 ol.row li')
        for i in html:
            item['img_url'] = response.urljoin(i.css('.image_container a img::attr("src")').extract_first())
            item['name'] = i.css('.product_pod h3 a::text').extract_first()
            item['money'] = i.css('.product_pod .product_price p.price_color::text').re_first('\d*\.\d*')
            yield item
        next_url = response.urljoin(response.css('.next >a::attr("href")').extract_first())
        # print(next_url)
        # if next_url:
        #     yield scrapy.Request(next_url,callback=self.parse)

