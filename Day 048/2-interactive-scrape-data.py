from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path="c:/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service)

driver.get("https://www.python.org")

conference_group = driver.find_elements(By.CSS_SELECTOR, ".event-widget > .shrubbery > .menu > li")

event_dict = {}
for index, event in enumerate(conference_group):
    text = event.text
    event_data = text.split("\n")
    time = event_data[0]
    event_name = event_data[1]
    event_dict[index] = {
        'time': time,
        'name': event_name
    }

print(event_dict)



driver.quit()