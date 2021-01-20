from app.TechnodomCrawler.ScraperForTechnodom import scrape_technodom
from app.models import TechnodomPrinter, TechnodomPrinterHistory

urls = [
    'https://www.technodom.kz/noutbuki-i-komp-jutery/periferijnye-ustrojstva/printery',
    'https://www.technodom.kz/noutbuki-i-komp-jutery/periferijnye-ustrojstva/printery?page=2',
    'https://www.technodom.kz/noutbuki-i-komp-jutery/periferijnye-ustrojstva/printery?page=3',
]

scrape_technodom(urls, TechnodomPrinter, TechnodomPrinterHistory)
