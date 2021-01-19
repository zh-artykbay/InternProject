from app.ScraperForSulpak import scrape
from app.models import SulpakTV, SulpakTVHistory


urls = [
    'https://www.sulpak.kz/f/led_oled_televizoriy',
    'https://www.sulpak.kz/f/led_oled_televizoriy?page=2',
    'https://www.sulpak.kz/f/led_oled_televizoriy?page=3',
    'https://www.sulpak.kz/f/led_oled_televizoriy?page=4',
    'https://www.sulpak.kz/f/led_oled_televizoriy?page=5',
    'https://www.sulpak.kz/f/led_oled_televizoriy?page=6',
    'https://www.sulpak.kz/f/led_oled_televizoriy?page=7',

]

scrape(urls, SulpakTV, SulpakTVHistory)