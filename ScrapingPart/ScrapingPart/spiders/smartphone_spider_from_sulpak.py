import scrapy


class SmartphonesSpider(scrapy.Spider):

    name = "smartphone"

    start_urls = [
        'https://www.sulpak.kz/f/smartfoniy',
        'https://www.sulpak.kz/f/smartfoniy?page=2',
        'https://www.sulpak.kz/f/smartfoniy?page=3',
        'https://www.sulpak.kz/f/smartfoniy?page=4',
        'https://www.sulpak.kz/f/smartfoniy?page=5',
        'https://www.sulpak.kz/f/smartfoniy?page=6',
        'https://www.sulpak.kz/f/smartfoniy?page=7',
        'https://www.sulpak.kz/f/smartfoniy?page=8',
        'https://www.sulpak.kz/f/smartfoniy?page=9',
        'https://www.sulpak.kz/f/smartfoniy?page=10',
        'https://www.sulpak.kz/f/smartfoniy?page=11',
        'https://www.sulpak.kz/f/smartfoniy?page=12',
        'https://www.sulpak.kz/f/smartfoniy?page=13',
        'https://www.sulpak.kz/f/smartfoniy?page=14',
    ]
    #@celery_app.task(bind=True, default_retry_delay=60 * 60)
    def parse(self, response):
        for smartphone in response.css('div.goods-tiles'):
            yield {
                'name': smartphone.css('div.product-container-right-side h3.title::text').get().strip(),
                'price': smartphone.css('div.product-container-right-side div.price-block div.price span::text').get().strip(),
            }

