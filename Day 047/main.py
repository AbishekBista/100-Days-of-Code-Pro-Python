import requests
from bs4 import BeautifulSoup
import smtplib
from secret import my_email, password

# Get the current price of the product
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ne;q=0.6,fr;q=0.5",
}

link = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(link, headers=headers)
response.raise_for_status()

content = response.text

with open('received.html', 'r', encoding='utf-8') as file:
    file = file.read()

soup = BeautifulSoup(file, "lxml")

price_string = soup.select_one(selector=".a-price>span:nth-of-type(2)").string
price = float(price_string.split("$")[1])

product_name_tag = soup.select_one(selector="span#productTitle")
product_name = product_name_tag.string.strip()

# Send email
if price < 100:
    with smtplib.SMTP(host='smtp.gmail.com') as connection:
        connection.starttls()
        
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:AmazonPriceAlert!\n\n{product_name} is now ${price}\n{link}".encode('utf-8'))