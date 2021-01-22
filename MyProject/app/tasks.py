from celery import shared_task
from app.SulpakCrawler.ScraperForSulpakCamera import scrape
from app.SulpakCrawler.ScraperForSulpakHeadphones import scrape
from app.SulpakCrawler.ScraperForSulpakPrinter import scrape
from app.SulpakCrawler.ScraperForSulpakPowerbank import scrape
from app.SulpakCrawler.ScraperForSulpakMonitor import scrape
from app.SulpakCrawler.ScraperForSulpakSmartphones import scrape

from app.SulpakCrawler.ScraperForSulpakSmartWatch import scrape
from app.SulpakCrawler.ScraperForSulpakTablet import scrape
from app.SulpakCrawler.ScraperForSulpakTV import scrape
from app.SulpakCrawler.ScraperForSulpakVRglass import scrape

from app.TechnodomCrawler.ScraperForTechnodomCamera import scrape_technodom
from app.TechnodomCrawler.ScraperForTechnodomHeadphones import scrape_technodom
from app.TechnodomCrawler.ScraperForTechnodomMonitor import scrape_technodom
from app.TechnodomCrawler.ScraperForTechnodomPowerbank import scrape_technodom
from app.TechnodomCrawler.ScraperForTechnodomPrinter import scrape_technodom
from app.TechnodomCrawler.ScraperForTechnodomSmartphones import scrape_technodom
from app.TechnodomCrawler.ScraperForTechnodomSmartWatch import scrape_technodom
from app.TechnodomCrawler.ScraperForTechnodomTablet import scrape_technodom
from app.TechnodomCrawler.ScraperForTechnodomTV import scrape_technodom
from app.TechnodomCrawler.ScraperForTechnodomVRglass import scrape_technodom

from app.ShopkzCrawler.ScraperForShopkzCamera import scrape_Shopkz
from app.ShopkzCrawler.ScraperForShopkzPrinter import scrape_Shopkz
from app.ShopkzCrawler.ScraperForShopkzSmartphones import scrape_Shopkz
from app.ShopkzCrawler.ScraperForShopkzMonitor import scrape_Shopkz
from app.ShopkzCrawler.ScraperForShopkzTV import scrape_Shopkz
from app.ShopkzCrawler.ScraperForShopkzHeadphones import scrape_Shopkz
from app.ShopkzCrawler.ScraperForShopkzPowerbank import scrape_Shopkz
from app.ShopkzCrawler.ScraperForShopkzSmartWatch import scrape_Shopkz
from app.ShopkzCrawler.ScraperForShopkzTablet import scrape_Shopkz

from app.MatchingItems import match_items

from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

@shared_task
def scrape_Technodom():
    return scrape_technodom()


@shared_task
def scrape_Shopkz():
    return scrape_Shopkz()


@shared_task(bind=True)
def scrape_Sulpak():
    return scrape()


@shared_task(bind=True)
def Matching_items():
    return match_items()
