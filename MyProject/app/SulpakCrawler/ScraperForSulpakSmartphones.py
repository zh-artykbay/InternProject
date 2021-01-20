from app.SulpakCrawler.ScraperForSulpak import scrape
from app.models import SulpakSmartphones, SulpakSmartphonesHistory


urls = [
    'https://www.sulpak.kz/f/smartfoniy',
    'https://www.sulpak.kz/f/smartfoniy?page=2',
    'https://www.sulpak.kz/f/smartfoniy?page=3',
    'https://www.sulpak.kz/f/smartfoniy?page=4',
    'https://www.sulpak.kz/f/smartfoniy?page=5',
    'https://www.sulpak.kz/f/smartfoniy?page=6',
    'https://www.sulpak.kz/f/smartfoniy?page=7',
    'https://www.sulpak.kz/f/smartfoniy?page=8',
    'https://www.sulpak.kz/f/smartfoniy?page=9',
    'https://www.sulpak.kz/f/smartfoniy?page=10',
]

scrape(urls, SulpakSmartphones, SulpakSmartphonesHistory)
