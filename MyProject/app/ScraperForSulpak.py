from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.models import SulpakSmartphones, SulpakSmartphonesHistory


def scrape(urls):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\Program Files (x86)/chromedriver')

    for url in urls:
        driver.get(url)

        try:

            count_items = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_css_selector('div.goods-tiles div.product-container-right-side'))

            #count_items = driver.find_elements_by_css_selector('div.goods-tiles div.product-container-right-side')
        except TimeoutError:
            print("Timeout Error")
            driver.quit()

        try:
            for item in count_items:
                name = item.find_element_by_css_selector('h3.title')

                if item.find_element_by_css_selector('div.price-block div.price span'):
                    price = item.find_element_by_css_selector('div.price-block div.price span')

                    print(name.text)
                    print(price.text)

                    try:
                        smartphone = SulpakSmartphones.objects.get(name=name.text)
                    except:
                        smartphone = False

                    if smartphone:
                        if price.text != smartphone.current_price:
                            smartphone.current_price = price.text
                            smartphone.save()
                            new_item_history = SulpakSmartphonesHistory(phone_id=smartphone, price=price.text)
                            new_item_history.save()
                    else:
                        new_item = SulpakSmartphones(name=name.text, current_price=price.text)
                        new_item.save()

                        new_item_history = SulpakSmartphonesHistory(phone_id=new_item, price=price.text)
                        new_item_history.save()
                else:
                    break

        except Exception as e:
            raise e
            driver.quit()
