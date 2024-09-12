from secret import CHROME_DRIVER_PATH, INSTAGRAM_USER, INSTAGRAM_PASSWORD, SIMILAR_ACCOUNT
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions, Chrome
import time


class InstaFollower:

    def __init__(self):
        service = Service(executable_path=CHROME_DRIVER_PATH)
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = Chrome(options=options, service=service)
        self.follow_buttons = None

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login")
        time.sleep(3)

        name_field = self.driver.find_element(By.NAME, "username")
        name_field.send_keys(INSTAGRAM_USER)

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(INSTAGRAM_PASSWORD)

        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        time.sleep(3)

        not_now = self.driver.find_element(By.CSS_SELECTOR, "div[role='button']")
        not_now.click()

        time.sleep(2)

        notification = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        notification.click()


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(2)

        follower_button = self.driver.find_element(By.CSS_SELECTOR, f"a[href='/{SIMILAR_ACCOUNT}/followers/']")
        follower_button.click()
        time.sleep(3)

        for i in range(8): # follow max 160 people ( 8 x 20 = 160), Instagram has a limit of 150 new follow requests per day
            print(i)
            self.follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "div[role='dialog'] button[type='button'] div[style='height: 100%;']")
            print(f'Follower button found: {len(self.follow_buttons)}')
            self.follow()
            self.follow_buttons[-1].location_once_scrolled_into_view

    def follow(self):
        for button in self.follow_buttons:
           if button.text != "Follow":
               pass
           else:
               button.click()
               time.sleep(1)
           