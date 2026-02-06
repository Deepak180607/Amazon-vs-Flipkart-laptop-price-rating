from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
def Scrape_data():
    path = r"D:\VSCode\edgedriver_win64\msedgedriver.exe"
    services = Service(executable_path=path)
    driver = webdriver.Edge(service=services)
    url = "https://www.amazon.in/ref=nav_logo"
    driver.get(url)
    search = driver.find_element(By.NAME, "field-keywords")
    search.send_keys("Gaming Laptops")
    search.send_keys(Keys.RETURN)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
            
        products = driver.find_elements(By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
        title_lst = []
        pri = []
        ratings = []
        for product in products:
            try:
                title = product.find_element(By.TAG_NAME, 'h2').text
                price = product.find_element(By.CLASS_NAME, 'a-price-whole').text
                rating = product.find_element(By.CLASS_NAME, 'a-row.a-size-small').text
                title_lst.append(title)
                pri.append(price)
                ratings.append(rating)
            except:
                continue
    finally:
        sleep(1)
        driver.quit()
        

    driver.quit()
    clean_names = []
    clean_prices = []
    clean_ratings = []

    for t, p, r in zip(title_lst, pri, ratings):
        if "|" in t:
            continue

        # name
        clean_names.append(t.split(',')[0].strip())

        # price
        clean_prices.append(int(p.replace(",", "")))
        
        clean_ratings.append(float(r.split("\n")[0]))
    dict = {"Name":clean_names, "Prices":clean_prices, "Ratings":clean_ratings}
    df = pd.DataFrame(dict)
    df.to_csv("data/amazon.csv", index=False)

    return df