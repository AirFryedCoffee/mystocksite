from .views import get_trending_tickers
from .views import trending_tickers_view
import requests
import json
from django.shortcuts import render

def trending_tickers(request):
    trending_tickers_data = get_trending_tickers()
    return {'trending_tickers': trending_tickers_data}

