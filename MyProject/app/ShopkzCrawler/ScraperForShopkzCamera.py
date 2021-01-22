from app.ShopkzCrawler.ScraperForShopkz import scrape_Shopkz
from app.models import ShopKzCamera, ShopKzCameraHistory


urls = [
    'https://shop.kz/fotoapparaty/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
]

scrape_Shopkz(urls, ShopKzCamera, ShopKzCameraHistory)
