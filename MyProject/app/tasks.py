from celery import shared_task
from app.ScraperForSulpakCamera import scrape
from app.ScraperForSulpakHeadphones import scrape
from app.ScraperForSulpakPrinter import scrape
from app.ScraperForSulpakPowerbank import scrape
from app.ScraperForSulpakMonitor import scrape
from app.ScraperForSulpakSmartphones import scrape
from app.ScraperForSulpakSmartWatch import scrape
from app.ScraperForSulpakTablet import scrape
from app.ScraperForSulpakTV import scrape
from app.ScraperForSulpakVRglass import scrape
#import app.ScraperForSulpakSmartphones.scrape
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task(bind=True)
def scrape_One():
    #logger.info(self.request.id)
    return scrape()

