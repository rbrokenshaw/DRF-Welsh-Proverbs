from django.contrib import admin
from django.urls import path, include
from .views import ListProverbsView, RandomProverbView, SearchProverbsView, test_view

urlpatterns = [
    path('all/', ListProverbsView.as_view(), name="proverbs-all"),
    path('random/', RandomProverbView.as_view(), name="random-proverb"),
    path('search/', SearchProverbsView.as_view({'get': 'list'}), name="search-proverb"),
    path('test/', test_view, name='test-view')
]
