from django.urls import path
from .views import HomePageView, AboutPageView
urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
]  # http://127.0.0.1:8000/about
