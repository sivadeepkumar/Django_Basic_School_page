from django.urls import path

from finance.views import *


urlpatterns = [
    path('fin-finanace/',finanace),
    path('stafffinanace/',stafffinanace),
]