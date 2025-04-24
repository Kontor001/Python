import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "UFGC99WVCIJGMSOU"
NEWS_API_KEY = "0faa120db99740f283640e5545afdab2"
auth_token="0d498a85630a3f1d4c1f28fb54322f62"
account_sid="ACa4c05b9a4e2372c3a433b475f449ce78"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

#If TODO4 percentage is greater than 5 then print("Get News").
# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diff_percent > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    # Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = articles[:3]
    print(three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.
    #Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_articles = [f"headline: {article ['title']}. \nBrief:{article ['description']}" for article in three_articles]


    client = Client(account_sid, auth_token)
    #Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_="+14155238886",
            to="+2349060515456"
        )