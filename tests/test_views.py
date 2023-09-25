from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Salade caesar", price=12)
        Menu.objects.create(title="Millefeuille végé", price=10)
        Menu.objects.create(title="MSuprême de volaille", price=14)
        Menu.objects.create(title="Macoha Burger", price=17)

    def test_get_all(self):
        client = APIClient()
        response = client.get('/restaurant/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

