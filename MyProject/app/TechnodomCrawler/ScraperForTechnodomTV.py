from app.TechnodomCrawler.ScraperForTechnodom import scrape_technodom
from app.models import TechnodomTV, TechnodomTVHistory


urls = [
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=2',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=3',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=4',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=5',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=6',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=7',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=8',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=9',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=10',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=11',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=12',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=13',
    'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=14',


]

scrape_technodom(urls, TechnodomTV, TechnodomTVHistory)

#'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=15',
#'https://www.technodom.kz/tv-audio-foto-video/televizory/led-televizory?page=16',