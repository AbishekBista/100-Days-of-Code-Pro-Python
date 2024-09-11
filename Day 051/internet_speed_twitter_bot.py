from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from secret import TWITTER_USER, TWITTER_EMAIL, TWITTER_PASSWORD

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_driver_path = "c:/chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_button.click()
        time.sleep(40)
        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(5)
        email_field = self.driver.find_element(By.TAG_NAME, "input")
        email_field.send_keys(TWITTER_EMAIL)
        email_field.send_keys(Keys.ENTER)
        time.sleep(1)

        name_field = self.driver.find_element(By.NAME, "text")
        name_field.send_keys(TWITTER_USER)
        name_field.send_keys(Keys.ENTER)

        time.sleep(1)

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)

        time.sleep(5)
        text_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        text_field.click()
        text_field.send_keys(f"Hello Internet Provider, my download speed was supposed to be 250 Mbps/10 Mbps, however, I'm getting {self.down} Mbps/{self.up} Mbps, please fix the issue.")

        time.sleep(5)
        post_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']")
        post_button.click()


    