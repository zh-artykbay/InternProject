from app.TechnodomCrawler.ScraperForTechnodom import scrape_technodom
from app.models import TechnodomSmartphones, TechnodomSmartphonesHistory


urls = [
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=2',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=3',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=4',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=5',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=6',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=7',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=8',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=9',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=10',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=12',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=12',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=13',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=14',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=15',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=16',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=17',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=18',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=19',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=20',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=21',
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=22',

]


scrape_technodom(urls, TechnodomSmartphones, TechnodomSmartphonesHistory)

#'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=23',