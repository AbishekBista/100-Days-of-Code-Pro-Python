from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from secret import MY_EMAIL, PASSWORD
import time

chrome_driver_path = "c:/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service)
url="https://www.linkedin.com/jobs/view/4017079241/?alternateChannel=search&refId=d0JUSknkEsPC6fSw6QnuKA%3D%3D&trackingId=jkRA%2FPd96Kc%2B2U9jaObbUg%3D%3D"
driver.get(url)

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

email_field = driver.find_element(By.NAME, "session_key")
email_field.send_keys(MY_EMAIL)

password_field = driver.find_element(By.NAME, "session_password")
password_field.send_keys(PASSWORD)

sign_in_button = driver.find_element(By.CLASS_NAME, 'btn__primary--large')
sign_in_button.click()

time.sleep(5)

easy_apply_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[1]/div/div[1]/div/div/div/div[6]/div/div/div/button")
easy_apply_button.click()

next_button = driver.find_element(By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
next_button.click()

time.sleep(2)
review_button = driver.find_element(By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
review_button.click()

time.sleep(2)
submit_button = driver.find_element(By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
submit_button.click()