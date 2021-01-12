import scrapy


class SmartphonesSpider(scrapy.Spider):
    name = "smartphone2"

    start_urls = [
        'https://www.mechta.kz/sec tion/smartfony/',
    ]

    def parse(self, response):
        for smartphone in response.css('div.bs3'):
            yield {
                'name': smartphone.css('div.q-pt-xs q-px-sm text-ts2 text-color2 ellipsis-2-lines::text').get().strip(),
                'price': smartphone.css('div.q-px-sm div.text-ts3 text-bold text-color2::text').get().strip(),
            }
