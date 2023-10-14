from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Stonk
from django.http import JsonResponse
from datetime import datetime

# Alpha Vantage API 
vantage_api_key = 'IU3KH32W5EJQE5PQ'

def get_trending_tickers():
    trending_tickers_url = f'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={vantage_api_key}'
    s = requests.get(trending_tickers_url)
    trending_ticker_data = s.json()
    filtered_tickers = [stock['ticker'] for stock in trending_ticker_data['most_actively_traded'] if int(stock['volume']) > 1000000]
    filtered_tickers.insert(0, "Trending Stocks:")
    return filtered_tickers

def trending_tickers_view(reqeust):
    trending_tickers = get_trending_tickers()
    return render(reqeust, 'stocks/home.html', {'trending_tickers': trending_tickers})



def home(reqeust):
    return render(reqeust, 'stocks/home.html')


def index(request):
    return HttpResponse("Blank")


def get_price(request):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=IU3KH32W5EJQE5PQ'
    r = requests.get(url)
    data = r.json()

    closing_prices = []

    for date, values in data['Time Series (Daily)'].items():

        closing_price = float(values['4. close'])
        closing_prices.append({"Date": date, "Closing Price":closing_price})

    #print(closing_prices)

    new_closing_prices = json.dumps(closing_prices).replace("'", "\"")
    print(new_closing_prices)

    return render(request, 'stocks/closing_prices.html', {"closing_prices": new_closing_prices})


 