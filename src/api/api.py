from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ConsumoEnergiaPaisSerializer
from api.serializers import DatosExtrasEnergiaPaisSerializer
from api.serializers import GasesSerializer
from api.serializers import HistoricoGhgSerializer
from api.serializers import HuellaMundialSerializer
from api.serializers import HuellaPaisSerializer
from api.serializers import ProduccionEnergiaPaisSerializer
from api.serializers import TemperaturaMundialSerializer
from api.serializers import PrediccionesSerializer
from api.models import ConsumoEnergiaPais
from api.models import DatosExtrasEnergiaPais
from api.models import Gases
from api.models import HistoricoGhg
from api.models import HuellaMundial
from api.models import HuellaPais
from api.models import ProduccionEnergiaPais
from api.models import TemperaturaMundial
from api.models import Predicciones

from rest_framework import viewsets, generics, filters
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


class ConsumoEnergiaPaisApiView(generics.ListAPIView):
    serializer_class = ConsumoEnergiaPaisSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'iso_code' : ['contains'],
        'year': ['contains']
    }

    def get_queryset(self):
        queryset = ConsumoEnergiaPais.objects.all()
        return queryset


class DatosExtrasEnergiaPaisApiView(generics.ListAPIView):
    serializer_class = DatosExtrasEnergiaPaisSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'iso_code' : ['contains'],
        'year': ['contains']
    }

    search_fields = ['country']

    def get_queryset(self):
        queryset = DatosExtrasEnergiaPais.objects.all()
        return queryset

class GasesApiView(generics.ListAPIView):
    serializer_class = GasesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'year': ['contains']
    }

    def get_queryset(self):
        queryset = Gases.objects.all()
        return queryset


class HistoricoGhgApiView(generics.ListAPIView):
    serializer_class = HistoricoGhgSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'country': ['contains'],
        'code': ['contains'],
        'continente': ['contains']
    }

    def get_queryset(self):
        queryset = HistoricoGhg.objects.all()
        return queryset

class HuellaMundialApiView(generics.ListAPIView):
    serializer_class = HuellaMundialSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'year': ['contains'],
    }

    def get_queryset(self):
        queryset = HuellaMundial.objects.all()
        return queryset

class HuellaPaisApiView(generics.ListAPIView):
    serializer_class = HuellaPaisSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'country': ['contains'],
        'code': ['contains'],
        'continente': ['contains']
    }

    def get_queryset(self):
        queryset = HuellaPais.objects.all()
        return queryset

class ProduccionEnergiaPaisApiView(generics.ListAPIView):
    serializer_class = ProduccionEnergiaPaisSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'year': ['contains'],
        'iso_code': ['contains']
    }

    def get_queryset(self):
        queryset = ProduccionEnergiaPais.objects.all()
        return queryset

class TemperaturaMundialApiView(APIView):
    serializer_class = TemperaturaMundialSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'year': ['contains'],
        'iso_code': ['contains']
    }

    def get_queryset(self):
        queryset = TemperaturaMundial.objects.all()
        return queryset
    
class PrediccionesApiView(APIView):
    serializer_class = PrediccionesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'year': ['contains'],
    }

    def get_queryset(self):
        queryset = Predicciones.objects.all()
        return queryset