from app.ShopkzCrawler.ScraperForShopkz import scrape_Shopkz
from app.models import ShopKzVRglass, ShopKzVRglassHistory


urls = [
    'https://shop.kz/search/?category=233&q=VR&s=',
]

scrape_Shopkz(urls, ShopKzVRglass, ShopKzVRglassHistory)
