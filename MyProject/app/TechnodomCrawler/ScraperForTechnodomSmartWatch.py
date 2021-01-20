from app.TechnodomCrawler.ScraperForTechnodom import scrape_technodom
from app.models import TechnodomWatch, TechnodomWatchHistory

urls = [
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=2',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=3',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=4',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=5',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=6',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=7',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=8',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=9',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=10',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=11',
]

scrape_technodom(urls, TechnodomWatch, TechnodomWatchHistory)