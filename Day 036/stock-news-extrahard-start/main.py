import requests
from secret import ALPHAVANTAGE_API_KEY, NEWS_API_KEY, my_email, password
import datetime as dt
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

today=dt.datetime.now().today()
last_month = today.replace(month=today.month - 1).date()

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY,
}

def significant_change_in_price(price_list):
    difference = abs(price_list[0] - price_list[1])
    print(difference)
    change_percentage = round(difference / price_list[1] * 100, ndigits=4)
    return change_percentage


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get("https://www.alphavantage.co/query", params=alpha_parameters)
response.raise_for_status()

stock_data = response.json()['Time Series (Daily)']
price_list = [float(stock_data[key]['4. close']) for (index, key) in enumerate(stock_data, start=0) if index < 2]


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
change_margin = significant_change_in_price(price_list)
if change_margin >= 5:
    news_parameters = {
        "q": COMPANY_NAME.split(" ")[0].lower(),
        "from": last_month,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    response.raise_for_status()

    news_data = response.json()["articles"][0:3]
    top_articles = [{"title": news['title'], "description": news["description"]} for news in news_data]
    article_content = ""
    for article in top_articles:
        article_content += f"Headline: {article['title']}\n"
        article_content += f"Brief: {article['description']}\n\n"
    print(article_content)



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    if price_list[0] > price_list[1]:
        symbol = "🔺"
    else:
        symbol = "🔻"
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Stock Alert\n\n{COMPANY_NAME}: {symbol} {round(change_margin)}%{article_content.encode('utf-8')}")



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

