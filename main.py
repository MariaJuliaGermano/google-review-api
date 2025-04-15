from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

def open_google_maps(location):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://www.google.com/maps")
        sleep(13)

        search_box = driver.find_element(By.ID, "searchboxinput")
        search_box.send_keys(location)
        search_box.send_keys(Keys.RETURN)
        sleep(15)

        return driver
    except Exception as e:
        print(f"Erro ao abrir o Google Maps: {e}")
        driver.quit()
        return None

def click_reviews(driver):
    try:
        reviews_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Reviews for Eiffel Tower')]")
        reviews_button.click()
        sleep(15)
    except Exception as e:
        print(f"Erro ao acessar as avaliações: {e}")
        driver.quit()

def scroll_reviews(driver, scrolls=5):
    try:
        reviews_container = driver.find_element(By.CLASS_NAME, "m6QErb.DxyBCb.kA9KIf.dS8AEf")
        for _ in range(scrolls):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", reviews_container)
            sleep(12)
    except Exception as e:
        print(f"Erro ao rolar as avaliações: {e}")
        driver.quit()

def extract_reviews(driver):
    try:
        reviews = []

        authors = driver.find_elements(By.CLASS_NAME, "d4r55")
        ratings = driver.find_elements(By.CLASS_NAME, "kvMYJc")
        texts = driver.find_elements(By.CLASS_NAME, "wiI7pd")

        for i in range(len(authors)):
            review = {
                "author": authors[i].text if i < len(authors) else "N/A",
                "rating": ratings[i].get_attribute("aria-label") if i < len(ratings) else "N/A",
                "text": texts[i].text if i < len(texts) else "N/A"
            }
            reviews.append(review)

        return reviews
    except Exception as e:
        print(f"Erro ao extrair avaliações: {e}")
        driver.quit()
        return []

if __name__ == "__main__":
    location = "Eiffel Tower"
    driver = open_google_maps(location)

    if driver:
        click_reviews(driver)
        scroll_reviews(driver, scrolls=5)
        reviews = extract_reviews(driver)
        print(reviews)
        driver.quit()

        driver.quit(print, scroll_reviews)  