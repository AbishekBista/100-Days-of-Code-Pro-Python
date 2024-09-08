from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path="c:/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service)

driver.get("https://en.wikipedia.org/wiki/Human")
search_bar = driver.find_element(By.NAME, "search")
print(search_bar.get_attribute("placeholder"))

driver.quit()
