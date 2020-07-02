import random
import requests

from rest_framework import generics
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from .documents import ProverbDocument
from .serializers import SearchDocumentSerializer

from django.shortcuts import render
from .models import Proverb
from .serializers import ProverbsSerializer


class ListProverbsView(generics.ListAPIView):
    queryset = Proverb.objects.all()
    serializer_class = ProverbsSerializer


class RandomProverbView(generics.ListAPIView):
    serializer_class = ProverbsSerializer

    def get_queryset(self):
        return Proverb.objects.all().filter(
            id=random.randrange(1, Proverb.objects.all().count() + 1)
        )


class SearchProverbsView(BaseDocumentViewSet):
    document = ProverbDocument
    serializer_class = SearchDocumentSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        SearchFilterBackend
    ]

    search_fields = (
        'welsh',
        'english',
    )

    filter_fields = {

    }

    ordering_fields = {

    }

    ordering = ('id')


def test_view(request):
    r = requests.get('http://localhost:8000/random?type=json')
    print(r.text)
    return render(request, 'proverbs/test.html')
