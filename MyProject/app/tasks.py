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


from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def scrape_Technodom():
    return scrape_technodom()

@shared_task(bind=True)
def scrape_Sulpak():
    #logger.info(self.request.id)
    return scrape()

