from django.contrib import admin
from django.urls import path, include
from .views import ListProverbsView, RandomProverbView, test_view

urlpatterns = [
    path('all/', ListProverbsView.as_view(), name="proverbs-all"),
    path('random/', RandomProverbView.as_view(), name="random-proverb"),
    path('test/', test_view, name='test-view')
]
