from app.TechnodomCrawler.ScraperForTechnodom import scrape_technodom
from app.models import TechnodomVRglass, TechnodomVRglassHistory


urls = [
    'https://www.technodom.kz/noutbuki-i-komp-jutery/virtual-naja-real-nost/ochki-virtual-noj-real-nosti/f/cl-virtual-reality-osnovnyye-792/dlja-pk',
]

scrape_technodom(urls, TechnodomVRglass, TechnodomVRglassHistory)
