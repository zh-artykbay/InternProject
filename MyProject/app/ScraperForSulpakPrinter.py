from app.ScraperForSulpak import scrape
from app.models import SulpakPrinter, SulpakPrinterHistory


urls = [
    'https://www.sulpak.kz/f/printeriy',
]

scrape(urls, SulpakPrinter, SulpakPrinterHistory)
