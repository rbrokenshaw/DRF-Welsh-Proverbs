from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .models import Proverb
from .documents import ProverbDocument


class ProverbsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proverb
        fields = ("welsh", "english")


class SearchDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ProverbDocument
        fields = (
            'welsh',
            'english',
        )
