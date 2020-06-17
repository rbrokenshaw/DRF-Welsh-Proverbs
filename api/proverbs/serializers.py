from rest_framework import serializers
from .models import Proverb


class ProverbsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proverb
        fields = ("welsh", "english")