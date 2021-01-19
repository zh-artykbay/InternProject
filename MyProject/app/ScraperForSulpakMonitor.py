from app.ScraperForSulpak import scrape
from app.models import SulpakMonitor, SulpakMonitorHistory


urls = [
    'https://www.sulpak.kz/f/monitoriy',
]

scrape(urls, SulpakMonitor, SulpakMonitorHistory)
