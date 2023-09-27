from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

# Home
class Index(TemplateView):
    template_name = 'index.html'

# API: Menu
class MenuItemView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

# API: Single Menu
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

# API: Booking
class BookingViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()






