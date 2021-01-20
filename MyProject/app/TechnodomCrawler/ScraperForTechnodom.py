from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.db_functions import check_item_is_exist, update_item_price, insert_item_to_table


def scrape_technodom(urls, Table_name, History_table_name):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\Program Files (x86)/chromedriver')

    for url in urls:
        driver.get(url)

        try:

            count_items = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_xpath("//li[@class='ProductCard']"))

        except TimeoutError:
            print("Timeout Error")
            driver.quit()

        try:
            for item in count_items:
                name = item.find_element_by_css_selector('a.ProductCard-Content h4')
                price = item.find_element_by_css_selector(
                    'a.ProductCard-Content div.ProductCard-PriceAndCredit p.ProductPrice data')
                if name.text.strip():
                    name = name.text.strip()
                    price = int(price.text[:-2].replace(" ", ""))

                    if check_item_is_exist(name, Table_name):
                        update_item_price(name, price, Table_name, History_table_name)
                    else:
                        insert_item_to_table(name, price, Table_name, History_table_name)

        except Exception as e:
            raise e
            driver.quit()
