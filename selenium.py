
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

pesquisa = driver.find_element(By.NAME, "q")

pesquisa.send_keys("Python Selenium")

pesquisa.send_keys(Keys.RETURN)

time.sleep(5)

titulos = driver.find_elements(By.TAG_NAME, "h3")

for titulo in titulos[:5]:
    print(titulo.text)

driver.quit()
