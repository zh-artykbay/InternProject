from app.TechnodomCrawler.ScraperForTechnodom import scrape_technodom
from app.models import TechnodomCamera, TechnodomCameraHistory


urls = [
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=12',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=2',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=3',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=4',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=5',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=6',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=7',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=8',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=9',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=10',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=11',
    'https://www.technodom.kz/fototehnika-i-kvadrokoptery/fotoapparaty?page=13',
]

scrape_technodom(urls, TechnodomCamera, TechnodomCameraHistory)
