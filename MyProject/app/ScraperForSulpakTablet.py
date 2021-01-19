from app.ScraperForSulpak import scrape
from app.models import SulpakTablet, SulpakTabletHistory


urls = [
    'https://www.sulpak.kz/f/planshetiy',
    'https://www.sulpak.kz/f/planshetiy?page=2',
    'https://www.sulpak.kz/f/planshetiy?page=3',
]

scrape(urls, SulpakTablet, SulpakTabletHistory)
