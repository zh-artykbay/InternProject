from app.TechnodomCrawler.ScraperForTechnodom import scrape_technodom
from app.models import TechnodomMonitor, TechnodomMonitorHistory

urls = [
    'https://www.technodom.kz/noutbuki-i-komp-jutery/komp-jutery-i-monitory/monitory',
    'https://www.technodom.kz/noutbuki-i-komp-jutery/komp-jutery-i-monitory/monitory?page=2',
    'https://www.technodom.kz/noutbuki-i-komp-jutery/komp-jutery-i-monitory/monitory?page=3',
    'https://www.technodom.kz/noutbuki-i-komp-jutery/komp-jutery-i-monitory/monitory?page=4',
    'https://www.technodom.kz/noutbuki-i-komp-jutery/komp-jutery-i-monitory/monitory?page=5',
    'https://www.technodom.kz/noutbuki-i-komp-jutery/komp-jutery-i-monitory/monitory?page=6',
    'https://www.technodom.kz/noutbuki-i-komp-jutery/komp-jutery-i-monitory/monitory?page=6',
    'https://www.technodom.kz/noutbuki-i-komp-jutery/komp-jutery-i-monitory/monitory?page=7',
]

scrape_technodom(urls, TechnodomMonitor, TechnodomMonitorHistory)
