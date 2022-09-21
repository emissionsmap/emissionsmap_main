from api.serializers import PaisConInformacionSerializer
from api.serializers import HuellaPaisSerializer , GasesMundialSerializer
from api.serializers import EmisionesPaisSerializer, TemperaturaMundialSerializer
from api.serializers import HuellaGasesTemperaturaMundialSerializer
from api.serializers import PrediccionMundialSerializer, HuellaMundialSerializer
from api.serializers import ConsumoSerializer, ProduccionSerializer
from api.models import PaisMaestro, ConsumoPais, ProduccionPais
from api.models import HuellaPais
from api.models import EmisionesPais , TemperaturaMundial
from api.models import MundialMaestro ,GasesMundial
from api.models import PrediccionMundial ,HuellaMundial

from rest_framework import generics, filters
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


class PaisConInformacionApiView(generics.ListAPIView):
    serializer_class = PaisConInformacionSerializer

    def get_queryset(self):
        queryset = PaisMaestro.objects.all()[:3]
        return queryset


class HuellaPaisApiView(generics.ListAPIView):
    serializer_class = HuellaPaisSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = {
    #     'iso_code' : ['contains'],
    #     'year': ['contains']
    # }

    # search_fields = ['country']

    def get_queryset(self):
        queryset = HuellaPais.objects.all()
        return queryset

class HuellaMundialApiView(generics.ListAPIView):
    serializer_class = HuellaMundialSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = {
    #     'iso_code' : ['contains'],
    #     'year': ['contains']
    # }

    # search_fields = ['country']

    def get_queryset(self):
        queryset = HuellaMundial.objects.all()
        return queryset


class GasesMundialApiView(generics.ListAPIView):
    serializer_class = GasesMundialSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = {
    #     'iso_code' : ['contains'],
    #     'year': ['contains']
    # }

    # search_fields = ['country']

    def get_queryset(self):
        queryset = GasesMundial.objects.all()
        return queryset


class TemperaturaMundialApiView(generics.ListAPIView):
    serializer_class = TemperaturaMundialSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = {
    #     'iso_code' : ['contains'],
    #     'year': ['contains']
    # }

    # search_fields = ['country']

    def get_queryset(self):
        queryset = TemperaturaMundial.objects.all()
        return queryset

class EmisionesPaisApiView(generics.ListAPIView):
    serializer_class = EmisionesPaisSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = {
    #     'anio': ['contains']
    # }

    def get_queryset(self):
        queryset = EmisionesPais.objects.all()
        return queryset



class HuellaGasesTemperaturaMundialApiView(generics.ListAPIView):
    serializer_class = HuellaGasesTemperaturaMundialSerializer

    def get_queryset(self):
        queryset = MundialMaestro.objects.all()[:3]
        return queryset

class PrediccionMundialApiView(generics.ListAPIView):
    serializer_class = PrediccionMundialSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = {
    #     'anio': ['contains'],
    # }

    def get_queryset(self):
        queryset = PrediccionMundial.objects.all()
        return queryset


class ConsumoApiView(generics.ListAPIView):
    serializer_class = ConsumoSerializer

    def get_queryset(self):
        queryset = ConsumoPais.objects.all()
        return queryset

class ProduccionApiView(generics.ListAPIView):
    serializer_class = ProduccionSerializer

    def get_queryset(self):
        queryset = ProduccionPais.objects.all()
        return queryset