from django.shortcuts import render
from django.http import HttpResponse
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# API: Menu
class MenuItemView(ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

# API: Single Menu
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

# API: Booking
class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


