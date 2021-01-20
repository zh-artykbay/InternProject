from app.TechnodomCrawler.ScraperForTechnodom import scrape_technodom
from app.models import TechnodomHeadphone, TechnodomHeadphoneHistory

urls = [
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=2',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=3',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=4',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=5',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=6',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=7',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=8',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=9',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=10',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=11',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=12',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=13',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=14',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=15',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=16',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=17',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=18',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=19',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=20',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=21',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=22',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=23',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=24',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=25',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=26',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=27',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=28',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=29',
    'https://www.technodom.kz/smartfony-i-gadzhety/naushniki?page=30',

]

scrape_technodom(urls, TechnodomHeadphone, TechnodomHeadphoneHistory)
