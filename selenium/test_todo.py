from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:5000")
assert "TODO" in driver.title
print("Test Passed: Title contains 'TODO'")
driver.quit()
