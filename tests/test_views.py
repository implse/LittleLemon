from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

# API Menu Tests
class MenuViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='citron', password='lemon@123!')
        self.token = Token.objects.create(user=self.user)
        Menu.objects.create(title="Salade caesar", price=12)
        Menu.objects.create(title="Millefeuille végé", price=10)
        Menu.objects.create(title="Suprême de volaille", price=14)
        Menu.objects.create(title="Macoha burger", price=17)

    def test_get_all(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = client.get(f'/restaurant/menu/', format='json')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        menu = Menu.objects.get(title="Salade caesar")
        response = client.get(f'/restaurant/menu/{menu.id}', format='json')
        serializer = MenuSerializer(menu)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

# API Booking Tests
class BookingViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='citron', password='lemon@123!')
        self.token = Token.objects.create(user=self.user)
        Booking.objects.create(name="charly", no_of_guests=2, booking_date="2023-10-01")
        Booking.objects.create(name="bloom", no_of_guests=3, booking_date="2023-10-07")
        Booking.objects.create(name="leonie", no_of_guests=2, booking_date="2023-10-12")
        Booking.objects.create(name="jean", no_of_guests=2, booking_date="2023-10-19")

    def test_get_all_booking(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = client.get(f'/restaurant/booking/tables/', format='json')
        tables = Booking.objects.all()
        serializer = BookingSerializer(tables, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_booking(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        table = Booking.objects.get(name="charly")
        response = client.get(f'/restaurant/booking/tables/{table.id}', format='json', follow=True)
        serializer = BookingSerializer(table)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)







