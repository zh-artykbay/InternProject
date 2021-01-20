from app.SulpakCrawler.ScraperForSulpak import scrape
from app.models import SulpakCamera, SulpakCameraHistory


urls = [
    'https://www.sulpak.kz/f/zerkalniye_fotoapparatiy',
    'https://www.sulpak.kz/f/fotoapparatiy',
]

scrape(urls, SulpakCamera, SulpakCameraHistory)
