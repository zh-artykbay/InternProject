from app.ShopkzCrawler.ScraperForShopkz import scrape_Shopkz
from app.models import ShopKzPrinter, ShopKzPrinterHistory


urls = [
    'https://shop.kz/printery-lazernye/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/printery-struynye/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/printery-matrichnye/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
]

scrape_Shopkz(urls, ShopKzPrinter, ShopKzPrinterHistory)
