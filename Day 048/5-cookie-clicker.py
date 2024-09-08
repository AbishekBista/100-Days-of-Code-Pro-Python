from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path="c:/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(2)

language_button = driver.find_element(By.ID, "langSelect-EN")
language_button.click()

time.sleep(2)

big_cookie = driver.find_element(By.ID, "bigCookie")

game_timeout = time.time() + 60 * 1

while True:
    if time.time() > game_timeout:
        cookies_per_second = driver.find_element(By.ID, "cookiesPerSecond")
        print(cookies_per_second.text.split(" ")[2])
        break
    upgrade_timeout = time.time() + 5
    while True:
        if time.time() > upgrade_timeout:
            try:
                highest_upgrade = driver.find_elements(By.XPATH, "//div[@class='product unlocked enabled']")[-1]
            except:
                print("Highest upgrade disabled")
            else:
                highest_upgrade.click()
            break
        big_cookie.click()




        
    


