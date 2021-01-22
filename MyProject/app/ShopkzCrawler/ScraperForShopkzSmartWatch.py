from app.ShopkzCrawler.ScraperForShopkz import scrape_Shopkz
from app.models import ShopKzWatch, ShopKzWatchHistory


urls = [
    'https://shop.kz/smart-chasy/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/smart-chasy/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
    'https://shop.kz/smart-chasy/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=3',
    'https://shop.kz/smart-chasy/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=4',

]

scrape_Shopkz(urls, ShopKzWatch, ShopKzWatchHistory)