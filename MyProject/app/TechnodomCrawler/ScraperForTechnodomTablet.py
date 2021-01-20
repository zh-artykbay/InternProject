from app.TechnodomCrawler.ScraperForTechnodom import scrape_technodom
from app.models import TechnodomTablet, TechnodomTabletHistory

urls = [
    'https://www.technodom.kz/smartfony-i-gadzhety/planshety-i-jelektronnye-knigi/planshety',
    'https://www.technodom.kz/smartfony-i-gadzhety/planshety-i-jelektronnye-knigi/planshety?page=2',
    'https://www.technodom.kz/smartfony-i-gadzhety/planshety-i-jelektronnye-knigi/planshety?page=3',
    'https://www.technodom.kz/smartfony-i-gadzhety/planshety-i-jelektronnye-knigi/planshety?page=4',
    'https://www.technodom.kz/smartfony-i-gadzhety/planshety-i-jelektronnye-knigi/planshety?page=5',
    'https://www.technodom.kz/smartfony-i-gadzhety/planshety-i-jelektronnye-knigi/planshety?page=6',
    'https://www.technodom.kz/smartfony-i-gadzhety/planshety-i-jelektronnye-knigi/planshety?page=7',
]

scrape_technodom(urls, TechnodomTablet, TechnodomTabletHistory)
