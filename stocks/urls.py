from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("prices/", views.get_price, name="get_price"),
    path("home/", views.trending_tickers_view, name="trending_tickers"),
    path("", views.new_user_stock, name="new_stock"),
] 
