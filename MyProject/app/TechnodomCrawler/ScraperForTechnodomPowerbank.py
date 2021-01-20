from app.TechnodomCrawler.ScraperForTechnodom import scrape_technodom
from app.models import TechnodomPowerbank, TechnodomPowerbankHistory

urls = [
    'https://www.technodom.kz/smartfony-i-gadzhety/aksessuary-dlja-telefonov/vneshnie-akkumuljatory',
    'https://www.technodom.kz/smartfony-i-gadzhety/aksessuary-dlja-telefonov/vneshnie-akkumuljatory?page=2',
    'https://www.technodom.kz/smartfony-i-gadzhety/aksessuary-dlja-telefonov/vneshnie-akkumuljatory?page=3',
    'https://www.technodom.kz/smartfony-i-gadzhety/aksessuary-dlja-telefonov/vneshnie-akkumuljatory?page=4',
    'https://www.technodom.kz/smartfony-i-gadzhety/aksessuary-dlja-telefonov/vneshnie-akkumuljatory?page=5',
    'https://www.technodom.kz/smartfony-i-gadzhety/aksessuary-dlja-telefonov/vneshnie-akkumuljatory?page=6',
]

scrape_technodom(urls, TechnodomPowerbank, TechnodomPowerbankHistory)
