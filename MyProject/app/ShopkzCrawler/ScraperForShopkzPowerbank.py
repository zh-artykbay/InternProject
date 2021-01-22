from app.ShopkzCrawler.ScraperForShopkz import scrape_Shopkz
from app.models import ShopKzPowerbank, ShopKzPowerbankHistory


urls = [
    'https://shop.kz/power-bank-mobilnye-akkumulyatory/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/power-bank-mobilnye-akkumulyatory/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
]

scrape_Shopkz(urls, ShopKzPowerbank, ShopKzPowerbankHistory)
