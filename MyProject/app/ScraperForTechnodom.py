from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
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
    'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony?page=23',
]

def scrape(urls):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\Program Files (x86)/chromedriver')

    for url in urls:
        driver.get(url)

        try:
            count_items = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_xpath("//li[@class='ProductCard']"))
            print(count_items)
        except TimeoutError:
            print("Timeout Error")
            driver.quit()

        try:
            for item in count_items:
                name = item.find_element_by_css_selector('a.ProductCard-Content h4')
                price = item.find_element_by_css_selector('a.ProductCard-Content div.ProductCard-PriceAndCredit p.ProductPrice data')
                name = name.text.strip()
                price = price.text.strip()

                try:
                    smartphone = TechnodomSmartphones.objects.get(name=name)
                except:
                    smartphone = False

                if smartphone:
                    if price != smartphone.current_price:
                        smartphone.current_price = price
                        smartphone.save()
                        new_item_history = TechnodomSmartphonesHistory(phone_id=smartphone, price=price)
                        new_item_history.save()
                else:
                    new_item = TechnodomSmartphones(name=name, current_price=price)
                    new_item.save()

                    new_item_history = TechnodomSmartphonesHistory(phone_id=new_item, price=price)
                    new_item_history.save()
        except Exception as e:
            raise e
            driver.quit()


scrape(urls)
