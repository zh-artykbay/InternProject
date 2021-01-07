import scrapy


class SmartphonesSpider4(scrapy.Spider):
    name = "smartphone4"

    start_urls = [
        'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
        'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
        'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=3',
        'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=4',
        'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=5',
        'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=6',
        'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=7',
        'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=8',
        'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=9',


    ]

    def parse(self, response):
        for smartphone in response.css('div.bx_catalog_item_container'):
            yield {
                'name': smartphone.css('div.bx-catalog-middle-part div.bx_catalog_item_title a::text').get().strip(),
                'price': smartphone.css('div.bx-catalog-right-part div.bx_catalog_item_price div.bx_price div.bx-more-prices span.bx-more-price-text::text').get().strip(),
            }