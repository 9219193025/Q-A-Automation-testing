from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def google_search(query):
    with webdriver.Chrome() as driver:
        driver.get("https://www.bing.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.submit()

        results = WebDriverWait(driver, 30).until(
            
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3"))
        )
        return results
results = google_search("Selenium Python")
print(f"Found {len(results)} results!")
