import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_duckduckgo_search():
    driver = webdriver.Chrome()
    driver.get("https://duckduckgo.com/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.title_contains("Selenium"))

    assert "Selenium" in driver.title
    driver.quit()

def test_duckduckgo_title():
    driver = webdriver.Chrome()
    driver.get("https://duckduckgo.com/")
    assert "DuckDuckGo" in driver.title
    driver.quit()
