from bs4 import BeautifulSoup
import requests
# import lxml

# with open(file="website.html", mode="r", encoding='utf-8') as file:
#     content = file.read()
   

# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)

#### GET ALL ######

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
     # print(tag.getText())
#     print(tag.get("href"))

# GET TAGS BY ATTRIBUTE NAME

# heading = soup.find(name="h1", id="name")
# print(heading)

# section = soup.find(name="h3", class_="heading")
# print(section.get("class"))

# first_anchor = soup.select_one(selector="p a")
# print(first_anchor)

# heading = soup.select(selector=".heading")
# print(heading)

response = requests.get("https://news.ycombinator.com/show")

yc_content = response.text

soup = BeautifulSoup(yc_content, "html.parser")

article_text = []
article_link = []

all_titles = soup.select(selector=".titleline > a")



for titles in all_titles:
    text = titles.string
    article_text.append(text)
    
    link = titles.get("href")
    article_link.append(link)

article_points = [int(score.string.split(" ")[0]) for score in soup.select(selector=".subline > .score")]


max_point = max(article_points)

max_index = article_points.index(max_point)

print(f'Most popular article: {article_text[max_index]} -> {article_link[max_index]}')


