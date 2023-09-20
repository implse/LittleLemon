from django.db import models

# Booking
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.name

# Menu
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=10)

    def __str__(self):
        return self.title
