from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Stonk
from django.http import JsonResponse

# Alpha Vantage API 
API_KEY = 'IU3KH32W5EJQE5PQ'

def home(reqeust):
    return HttpResponse("This is the home page")


def index(request):
    return HttpResponse("Blank")


def get_price(request):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=IU3KH32W5EJQE5PQ'
    r = requests.get(url)
    data = r.json()

    return JsonResponse(data)
