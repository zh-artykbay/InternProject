from app.SulpakCrawler.ScraperForSulpak import scrape
from app.models import SulpakPowerbank, SulpakPowerbankHistory


urls = [
    'https://www.sulpak.kz/f/akkumulyatoriy_k_telefonam',
    'https://www.sulpak.kz/f/akkumulyatoriy_k_telefonam?page=2',
]

scrape(urls, SulpakPowerbank, SulpakPowerbankHistory)
