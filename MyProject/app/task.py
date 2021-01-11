from app.scraperforsulpak import scrape
from MyProject.MyProject.celery import app


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


@app.task
def scrape_One():
    scrape(urls)
    return

