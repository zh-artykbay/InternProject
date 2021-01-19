from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
#from app.models import TechnodomSmartphones, TechnodomSmartphonesHistory

urls = [
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=2',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=3',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=4',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=5',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=6',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=7',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=8',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=9',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=10',
    'https://www.technodom.kz/smartfony-i-gadzhety/gadzhety/smart-chasy?page=11',
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
            #print(count_items)
        except TimeoutError:
            print("Timeout Error")
            driver.quit()

        try:
            for item in count_items:
                name = item.find_element_by_css_selector('a.ProductCard-Content h4')
                price = item.find_element_by_css_selector('a.ProductCard-Content div.ProductCard-PriceAndCredit p.ProductPrice data')

               """ if name.text.strip():
                    print(name.text.strip())
                    print(int(price.text[:-2].replace(" ", "")))"""
                #name = name.text.strip()
                #price = price.text.strip()

                """try:
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
                    new_item_history.save()"""
        except Exception as e:
            raise e
            driver.quit()


scrape(urls)
