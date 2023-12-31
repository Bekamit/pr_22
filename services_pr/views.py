from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from .serializers import ServicesReadSerializer, \
    SelectWriteSerializer, \
    UnderSerializer, SelectReadSerializer, ServicesWriteSerializer, BookingSericesReadSerializer, BookingSerivcesWriteSerializer

from .models import Services, SelectCategory, UnderService, Booking_s
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.order_by('pk')
    serializer_class = ServicesReadSerializer
    permission_classes = [IsAuthenticated]

    # parser_classes = (MultiPartParser,)

    def get_serializer_class(self):
        if self.action == 'create':
            return ServicesWriteSerializer
        return super().get_serializer_class()




class SelectViewSet(viewsets.ModelViewSet):
    queryset = SelectCategory.objects.order_by('pk')
    serializer_class = SelectReadSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return SelectWriteSerializer
        return super().get_serializer_class()




class UnderViewSet(viewsets.ModelViewSet):
    queryset = UnderService.objects.order_by('pk')
    serializer_class = UnderSerializer
    permission_classes = [IsAuthenticated]

    # parser_classes = (MultiPartParser,)

class BookingUnderServicesViewSet(viewsets.ModelViewSet):
    queryset = Booking_s.objects.order_by('pk')
    serializer_class = BookingSericesReadSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return BookingSerivcesWriteSerializer
        return super().get_serializer_class()