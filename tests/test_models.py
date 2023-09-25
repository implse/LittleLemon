from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_menu(self):
        item = Menu.objects.create(title="Salade caesar", price=12)
        self.assertEqual(item.__str__(), "Salade caesar : 12")