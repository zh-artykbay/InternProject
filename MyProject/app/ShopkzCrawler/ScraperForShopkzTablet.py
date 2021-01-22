from app.ShopkzCrawler.ScraperForShopkz import scrape_Shopkz
from app.models import ShopKzTablet, ShopKzTabletHistory


urls = [
    'https://shop.kz/planshety/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/planshety/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
]

scrape_Shopkz(urls, ShopKzTablet, ShopKzTabletHistory)
