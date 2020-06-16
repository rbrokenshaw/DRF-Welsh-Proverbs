from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Proverb
from .serializers import ProverbsSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_proverb(welsh="", english=""):
        if welsh != "" and english != "":
            Proverb.objects.create(welsh=welsh, english=english)


    def setUp(self):
        self.create_proverb("Co' ni off!", "Off we go!")
        self.create_proverb("Well Duw Duw!", "Well well!")


class GetAllProverbsTest(BaseViewTest):

    def test_get_all_proverbs(self):
        response = self.client.get(
            reverse("proverbs-all", kwargs={"version": "v1"})
        )
        expected = Proverb.objects.all()
        serialized = ProverbsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)