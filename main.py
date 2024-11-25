from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
 
def open_google_maps(location):
    driver = webdriver.Chrome()

    try:
        driver.get("https:/www.google.com/maps")
        sleep(3)

        search_box = driver.find_element(By.ID, "searchboxinput")
        search_box.send_keys(location)
        search_box.send_keys(Keys.RETURN)
        sleep(5)

        return driver
    except Exception as e:
        print(f"Erro ao abrir o Google Maps: {e}")
        driver.quit()

def click_reviews(driver):
    try:
        reviews_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'reviews')]")
        reviews_button.click()
        sleep(5)
    except Exception as e:
        print(f"Erro ao acessar as avaliações: {e}")
        driver.quit()

def scroll_reviews(driver, scrolls=5):
    try:
        reviews_container = driver.find_element(By.CLASS_NAME, "m6QErb.DxyBCb.kA9KIf.dS8AEf")
        for _ in range(scrolls):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", reviews_container)
            sleep(2)
    except Exception as e:
        print(f"Erro ao colar as avaliações: {e}")
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
                "rating": ratings[i].get_atribute("arial-label") if i < len(ratings) else "N/A",
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