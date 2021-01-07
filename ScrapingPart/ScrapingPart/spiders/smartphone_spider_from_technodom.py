import scrapy


class SmartphonesSpiderTechnodom(scrapy.Spider):
    name = "smartphone1"

    start_urls = [
        'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony',
    ]

    def parse(self, response):
        for smartphone in response.css('a.ProductCard-Content'):
            yield {
                'name': smartphone.css('h4.title::text').get().strip(),
                'price': smartphone.css('div.ProductCard-PriceAndCredit p.ProductPrice  span data::text').get().strip(),
            }

#