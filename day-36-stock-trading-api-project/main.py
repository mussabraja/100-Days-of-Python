import requests
import os
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_keyy = os.environ.get("stock_api_key")
news_api_keyy = os.environ.get("news_api_key")
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": stock_api_keyy
}

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=stock_api_keyy'

r = requests.get(STOCK_ENDPOINT, params=parameters)
data = r.json()
us_dict = data['Time Series (Daily)']
values_list = list(us_dict.values())
yesterdays_closing = values_list[0]['4. close']
two_das_ago_closing = values_list[1]['4. close']
difference = (abs(float(two_das_ago_closing)-float(yesterdays_closing)))
diff_percent = (float(difference) / float(two_das_ago_closing)) * 100

news_parameters = {
    "q": "tesla",
    "apiKey": news_api_keyy,
    "sortBy": "publishedAt",
}

if diff_percent > 5:
    r2 = requests.get(NEWS_ENDPOINT, params=news_parameters)
    data_2 = r2.json()
    articles_p = data_2['articles']
    y = articles_p[:3]
    print("Get News")
    for n in y:
        desc = n["description"]
        print(desc)
        print(n["title"])
