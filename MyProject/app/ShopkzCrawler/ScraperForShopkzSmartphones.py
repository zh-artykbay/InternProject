from app.ShopkzCrawler.ScraperForShopkz import scrape_Shopkz
from app.models import ShopKzSmartphones, ShopKzSmartphonesHistory


urls = [
    'https://shop.kz/smartfony/smartfony-xiaomi/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/smartfony/smartfony-xiaomi/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
    'https://shop.kz/smartfony/smartfony-xiaomi/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=3',
    'https://shop.kz/smartfony/smartfony-samsung/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/smartfony/smartfony-samsung/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
    'https://shop.kz/smartfony/smartfony-realme/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/smartfony/smartfony-poco/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/smartfony/smartfony-apple-iphone/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/smartfony/smartfony-apple-iphone/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
    'https://shop.kz/smartfony/smartfony-meizu/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
]

scrape_Shopkz(urls, ShopKzSmartphones, ShopKzSmartphonesHistory)
