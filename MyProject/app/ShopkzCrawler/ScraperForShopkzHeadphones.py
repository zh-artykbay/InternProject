from app.ShopkzCrawler.ScraperForShopkz import scrape_Shopkz
from app.models import ShopKzHeadphone, ShopKzHeadphoneHistory


urls = [
    'https://shop.kz/naushniki-i-garnitury/naushniki-dlya-telefonov/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/naushniki-i-garnitury/naushniki-dlya-telefonov/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
    'https://shop.kz/naushniki-i-garnitury/naushniki-dlya-telefonov/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=3',
    'https://shop.kz/naushniki-i-garnitury/naushniki-dlya-telefonov/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=4',
    'https://shop.kz/naushniki-i-garnitury/naushniki-dlya-telefonov/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=5',
    'https://shop.kz/naushniki-i-garnitury/naushniki-dlya-telefonov/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=6',
    'https://shop.kz/naushniki-i-garnitury/naushniki-dlya-telefonov/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=7',
    'https://shop.kz/naushniki-i-garnitury/naushniki-dlya-telefonov/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=8',
    'https://shop.kz/naushniki-i-garnitury/naushniki-dlya-telefonov/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=9',
]

scrape_Shopkz(urls, ShopKzHeadphone, ShopKzHeadphoneHistory)
