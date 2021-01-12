from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.models import ShopKzSmartphones, ShopKzSmartphonesHistory

urls = [
    'https://shop.kz/smartfony/smartfony-xiaomi/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/smartfony/smartfony-xiaomi/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
    'https://shop.kz/smartfony/smartfony-xiaomi/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=3',
    'https://shop.kz/smartfony/smartfony-samsung/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/smartfony/smartfony-samsung/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
    'https://shop.kz/smartfony/smartfony-realme/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/smartfony/smartfony-poco/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/smartfony/smartfony-apple-iphone/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'https://shop.kz/smartfony/smartfony-apple-iphone/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=2',
    'https://shop.kz/smartfony/smartfony-meizu/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
]

def scrape(urls):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\Program Files (x86)/chromedriver')

    for url in urls:
        driver.get(url)

        try:
            count_items = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_css_selector('div.bx_catalog_item'))
            #print(len(count_items))
            #count_items = driver.find_elements_by_css_selector('div.goods-tiles div.product-container-right-side')
        except TimeoutError:
            print("Timeout Error")
            driver.quit()

        try:
            for item in count_items:
                #username = item.find_element_by_xpath("//div[@class='bx_catalog_item_container gtm-impression-product']")
                #username.get_attribute("data-product")
                name = item.find_element_by_css_selector('div.bx_catalog_item_container div.bx-catalog-middle-part div.bx_catalog_item_title a')
                price = item.find_element_by_css_selector('div.bx-catalog-right-part div.bx_catalog_item_price div.bx_price')

                print(name.get_attribute("title").strip())
                print(price.text.strip())
                name = name.get_attribute("title").strip()
                price = price.text.strip()

                try:
                    smartphone = ShopKzSmartphones.objects.get(name=name)
                except:
                    smartphone = False

                if smartphone:
                    if price != smartphone.current_price:
                        smartphone.current_price = price
                        smartphone.save()
                        new_item_history = ShopKzSmartphonesHistory(phone_id=smartphone, price=price)
                        new_item_history.save()
                else:
                    new_item = ShopKzSmartphones(name=name, current_price=price)
                    new_item.save()

                    new_item_history = ShopKzSmartphonesHistory(phone_id=new_item, price=price)
                    new_item_history.save()

        except Exception as e:
            raise e
            driver.quit()

scrape(urls)