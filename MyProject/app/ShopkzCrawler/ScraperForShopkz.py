from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.db_functions import check_item_is_exist, update_item_price, insert_item_to_table


def scrape_Shopkz(urls, Table_name, History_table_name):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\Program Files (x86)/chromedriver')

    for url in urls:
        driver.get(url)

        try:
            count_items = WebDriverWait(driver, 10).until(
                lambda driver: driver.find_elements_by_css_selector('div.bx_catalog_item'))

        except TimeoutError:
            print("Timeout Error")
            driver.quit()

        try:
            for item in count_items:

                name = item.find_element_by_css_selector(
                    'div.bx_catalog_item_container div.bx-catalog-middle-part div.bx_catalog_item_title a')
                name = name.get_attribute("title").strip()

                price = item.find_element_by_css_selector(
                    'div.bx-catalog-right-part div.bx_catalog_item_price div.bx_price')
                price = price.text.strip().split('₸')

                if price[1]:
                    price = int(price[1].strip().replace(" ", ""))
                else:
                    price = int(price[0].strip().replace(" ", ""))

                if check_item_is_exist(name, Table_name):
                    update_item_price(name, price, Table_name, History_table_name)
                else:
                    insert_item_to_table(name, price, Table_name, History_table_name)

        except Exception as e:
            raise e
            driver.quit()