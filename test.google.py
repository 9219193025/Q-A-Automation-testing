from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

# Find the search input box
search_box = driver.find_element(By.NAME, "search")

# Type "Python programming" and press Enter
search_box.send_keys("Python programming")
search_box.send_keys(Keys.RETURN)

time.sleep(2)

# Click on the first link (Python programming language page)
first_link = driver.find_element(By.XPATH, "//a[@href='/wiki/Python_(programming_language)']")
first_link.click()

time.sleep(3)
driver.quit()
