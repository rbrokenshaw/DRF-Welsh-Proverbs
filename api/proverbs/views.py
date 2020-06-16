from rest_framework import generics
from .models import Proverb
from .serializers import ProverbsSerializer


class ListProverbsView(generics.ListAPIView):
    queryset = Proverb.objects.all()
    serializer_class = ProverbsSerializer