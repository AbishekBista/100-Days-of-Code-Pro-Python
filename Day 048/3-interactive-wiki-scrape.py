from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "c:/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(options=options, service=service)

driver.get("https://en.m.wikipedia.org/wiki/Main_Page")

article_tag = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_tag.text)

driver.quit()
