from secret import ZILLOW_SITE, GOOGLE_FORM_SITE
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
import requests
import time

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ne;q=0.6,fr;q=0.5"
}

response = requests.get(ZILLOW_SITE, headers=header)
response.raise_for_status()

content = response.content

soup = BeautifulSoup(content, 'html.parser')

prices = soup.select(selector='span[data-test]')
addresses = soup.select(selector='address[data-test]')
links = soup.select(selector="a[data-test]")

prices = [price.text[0:6] for price in prices]
addresses = [address.text for address in addresses]
links = [f'{ZILLOW_BASE_URL}{link.get("href")}' if link.get("href").startswith("/") else link.get("href") for link in links]


service = Service("c:/chromedriver.exe")
options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service)

for i in range(len(prices)):
    driver.get(GOOGLE_FORM_SITE)

    input_elements = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")

    for index, element in enumerate(input_elements):
        if index == 0:
            element.send_keys(addresses[i])
        elif index == 1:
            element.send_keys(prices[i])
        elif index == 2:
            element.send_keys(links[i])

    submit_element = driver.find_element(By.CSS_SELECTOR, "div[role='button']")
    submit_element.click()

    time.sleep(2)








