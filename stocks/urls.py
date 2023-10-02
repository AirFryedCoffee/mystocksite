from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("prices/", views.get_price, name="get_price"),
    path("home/", views.home, name="home"),
]

