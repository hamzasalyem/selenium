from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Hamza Saleem\chromedriver.exe")
driver.get("http://www.python.org")

print(driver.title)
assert "Python" in driver.title
print(driver.title)

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("py")
elem.send_keys(Keys.RETURN)

element = driver.find_element(By.XPATH, "//input[@id-search-field']")

element = driver.find_element(By.ID, "passwd-id")
element = driver.find_element(By.NAME, "passwd")

element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")

assert "No results found." not in driver.page_source
driver.close()