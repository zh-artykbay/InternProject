from app.ShopkzCrawler.ScraperForShopkz import scrape_Shopkz
from app.models import ShopKzTV, ShopKzTVHistory

urls = [
    'https://shop.kz/televizory/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/televizory/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
]

scrape_Shopkz(urls, ShopKzTV, ShopKzTVHistory)