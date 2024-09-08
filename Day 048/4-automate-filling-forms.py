from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "c:/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(options=options, service=service)

driver.get("https://secure-retreat-92358.herokuapp.com")

# CLICKING ON LINK TAGS

# article_tag = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

# wiktionary = driver.find_element(By.LINK_TEXT, "Wiktionary")
# wiktionary.click()

# FILLING INPUTS
fname = driver.find_element(By.NAME, "fName")

fname.send_keys("Mario")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Luigi")

email = driver.find_element(By.NAME, "email")
email.send_keys("mario@luigi.com")

sign_up = driver.find_element(By.TAG_NAME, "button")
sign_up.click()




