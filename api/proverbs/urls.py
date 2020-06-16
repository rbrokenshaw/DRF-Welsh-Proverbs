from django.contrib import admin
from django.urls import path, include
from .views import ListProverbsView

urlpatterns = [
    path('', ListProverbsView.as_view(), name="proverbs-all")
]
