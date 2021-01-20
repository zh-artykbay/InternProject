from app.SulpakCrawler.ScraperForSulpak import scrape
from app.models import SulpakVRglass, SulpakVRglassHistory


urls = [
    'https://www.sulpak.kz/f/zd_ochki',
]

scrape(urls, SulpakVRglass, SulpakVRglassHistory)
