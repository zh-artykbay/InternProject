from app.models import SulpakWatch, SulpakWatchHistory
from app.ScraperForSulpak import scrape

urls = [
    'https://www.sulpak.kz/f/smart_chasiy',
    'https://www.sulpak.kz/f/smart_chasiy?page=2',
    'https://www.sulpak.kz/f/smart_chasiy?page=3',
    'https://www.sulpak.kz/f/smart_chasiy?page=4',
]

scrape(urls, SulpakWatch, SulpakWatchHistory)