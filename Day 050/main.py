from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas

chrome_driver_path = "c:/chromedriver.exe"

service = Service(executable_path=chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

checkpoint_reached = False

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://fitgirl-repacks.site")

game_data_list = []

page_numbers = int(driver.find_element(By.CSS_SELECTOR, ".pagination.loop-pagination a:nth-last-child(2)").text)

for i in range(1, 449):
    driver.get(f"https://fitgirl-repacks.site/page/{i}/")
    print(f"Current page: {i}")
    article_post = driver.find_elements(By.CLASS_NAME, 'category-lossless-repack')
    for index, article in enumerate(article_post):
    
        # find title, date, comments, genre, companies, language, original size, repack size, description
        title = article.find_element(By.CSS_SELECTOR, ".entry-header h1 > a").text
        print(title)
        if title == 'XBLAZE LOST: MEMORIES':
            checkpoint_reached = True
            break
        date = article.find_element(By.CSS_SELECTOR, ".entry-header .entry-meta .entry-date a").text
        comments = article.find_element(By.CSS_SELECTOR, ".entry-header .entry-meta .comments-link a").text
        languages = article.find_element(By.CSS_SELECTOR, ".entry-content p strong:nth-of-type(1)").text
        companies = article.find_element(By.CSS_SELECTOR, ".entry-content p strong:nth-of-type(2)").text
        original_size = article.find_element(By.CSS_SELECTOR, ".entry-content p strong:nth-last-of-type(2)").text
        repack_size = article.find_element(By.CSS_SELECTOR, ".entry-content p strong:nth-last-of-type(1)").text

    
        game_data_list.append({
            'title': title,
            'date': date,
            'comments': int(comments.split(" ")[0]),
            "companies": companies,
            "languages": languages,
            "original_size": original_size,
            "repack_size": repack_size,
        })
    if checkpoint_reached:
        break

df = pandas.DataFrame(game_data_list)
df.to_csv('game_data.csv')


   

driver.quit()

