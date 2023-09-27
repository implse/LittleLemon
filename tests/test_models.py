from django.test import TestCase
from restaurant.models import Menu

# Model Menu Tests
class MenuTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="Salade caesar", price=12)
        Menu.objects.create(title="Millefeuille végé", price=10)
        Menu.objects.create(title="Suprême de volaille", price=14)
        Menu.objects.create(title="Macoha burger", price=17)

    def test_get_menu(self):
        menu1 = Menu.objects.get(title="Salade caesar")
        menu2 = Menu.objects.get(title="Millefeuille végé")
        menu3 = Menu.objects.get(title="Suprême de volaille")
        menu4 = Menu.objects.get(title="Macoha burger")
        self.assertEqual(f'{menu1.title} : {menu1.price}', "Salade caesar : 12.00")
        self.assertEqual(f'{menu2.title} : {menu2.price}', "Millefeuille végé : 10.00")
        self.assertEqual(f'{menu3.title} : {menu3.price}', "Suprême de volaille : 14.00")
        self.assertEqual(f'{menu4.title} : {menu4.price}', "Macoha burger : 17.00")

    def test_update_menu(self):
        menu_burger = Menu.objects.get(title="Macoha burger")
        menu_burger.price = 15
        menu_burger.save()
        update_menu = Menu.objects.get(title="Macoha burger")
        self.assertEqual(f'{update_menu.title} : {update_menu.price}', "Macoha burger : 15.00")
