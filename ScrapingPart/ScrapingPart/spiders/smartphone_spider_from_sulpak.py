import scrapy


class SmartphonesSpider(scrapy.Spider):
    name = "smartphone"

    def start_requests(self):
        urls = [
            'https://www.sulpak.kz/f/smartfoniy',
            'https://www.sulpak.kz/f/smartfoniy?page=2',
        ]
        #for url in urls:
         #   yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for smartphone in response.css('div.goods-tiles'):
            yield {
                'name': smartphone.css('div.product-container-right-side h3.title::text').get(),
                'price': smartphone.css('div.product-container-right-side div.price-block div.price span::text').get(),
            }