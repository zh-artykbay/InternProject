from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\Program Files (x86)/chromedriver')
urls = [
    'https://www.sulpak.kz/f/smartfoniy',
    'https://www.sulpak.kz/f/smartfoniy?page=2',
    'https://www.sulpak.kz/f/smartfoniy?page=3',
    'https://www.sulpak.kz/f/smartfoniy?page=4',
    'https://www.sulpak.kz/f/smartfoniy?page=5',
    'https://www.sulpak.kz/f/smartfoniy?page=6',
    'https://www.sulpak.kz/f/smartfoniy?page=7',
    'https://www.sulpak.kz/f/smartfoniy?page=8',
    'https://www.sulpak.kz/f/smartfoniy?page=9',
    'https://www.sulpak.kz/f/smartfoniy?page=10',
]
for url in urls:
    driver.get(url)

    count_items = driver.find_elements_by_css_selector('div.goods-tiles div.product-container-right-side')
    for item in count_items:
        name = item.find_element_by_css_selector('h3.title')
        price = item.find_element_by_css_selector('div.price-block div.price span')

        print(name.text)
        print(price.text)
