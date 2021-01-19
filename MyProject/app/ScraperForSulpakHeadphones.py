from app.ScraperForSulpak import scrape
from app.models import SulpakHeadphone, SulpakHeadphoneHistory


urls = [
    'https://www.sulpak.kz/f/naushniki',
    'https://www.sulpak.kz/f/naushniki?page=2',
    'https://www.sulpak.kz/f/naushniki?page=3',
    'https://www.sulpak.kz/f/naushniki?page=4',
    'https://www.sulpak.kz/f/naushniki?page=5',
    'https://www.sulpak.kz/f/naushniki?page=6',
    'https://www.sulpak.kz/f/naushniki?page=7',
    'https://www.sulpak.kz/f/naushniki?page=8',
    'https://www.sulpak.kz/f/naushniki?page=9',
    'https://www.sulpak.kz/f/naushniki?page=10',
]

scrape(urls, SulpakHeadphone, SulpakHeadphoneHistory)
