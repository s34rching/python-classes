from twilio.rest import Client
from datetime import datetime, timedelta
import os
import requests

ALPHA_ADVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
CATERPILLAR = "Caterpillar Inc"
CATERPILLAR_INC_SYMBOL = "CAT"

ALPHA_ADVANTAGE_KEY = os.environ.get("ALPHA_ADVANTAGE_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
PERSONAL_NUMBER = os.environ.get("PERSONAL_NUMBER")


def compose_message(price_change: float, recent_article) -> str:
    if price_change > 0:
        headline = f"{CATERPILLAR_INC_SYMBOL} ▲ {round(price_change, 3)}"
    else:
        headline = f"{CATERPILLAR_INC_SYMBOL} 🔻 {round(price_change, 3)}"

    return f"{headline}\n\n{recent_article["title"]}\n\n{recent_article["description"]}\n\n{recent_article["url"]}"


def get_date_days_ago(days_ago: int) -> str:
    previous_date = datetime.now() - timedelta(days=days_ago)
    return previous_date.strftime('%Y-%m-%d')


def get_stock_closing_price_days_ago(stock_data, date: str) -> float:
    price_str = stock_data["Time Series (Daily)"][date]["4. close"]

    return float(price_str)


yesterday = get_date_days_ago(1)
day_before_yesterday = get_date_days_ago(2)

stock_req_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": CATERPILLAR_INC_SYMBOL,
    "apikey": ALPHA_ADVANTAGE_KEY
}

stocks_response = requests.get(ALPHA_ADVANTAGE_ENDPOINT, stock_req_params)
stocks_data = stocks_response.json()

yesterday_price = get_stock_closing_price_days_ago(stocks_data, yesterday)
day_before_yesterday_price = get_stock_closing_price_days_ago(stocks_data, day_before_yesterday)

percents_change = (yesterday_price - day_before_yesterday_price) / day_before_yesterday_price * 100

if percents_change > 5 or percents_change < -2:
    news_req_params = {
        "q": CATERPILLAR,
        "qInTitle": CATERPILLAR,
        "from": day_before_yesterday,
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT, news_req_params)
    news_data = news_response.json()
    first_article = news_data["articles"][0]

    client = Client(TWILIO_SID, TWILIO_TOKEN)
    message = client.messages.create(
        body=compose_message(percents_change, first_article),
        from_=TWILIO_NUMBER,
        to=PERSONAL_NUMBER
    )
