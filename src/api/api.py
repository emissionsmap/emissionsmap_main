from api.serializers import PaisConInformacionSerializer
from api.serializers import HuellaPaisSerializer , GasesMundialSerializer
from api.serializers import EmisionesPaisSerializer, TemperaturaMundialSerializer
from api.serializers import HuellaGasesTemperaturaMundialSerializer
from api.serializers import PrediccionMundialSerializer, HuellaMundialSerializer
from api.serializers import ConsumoSerializer, ProduccionSerializer
from api.serializers import EmisionesContinenteSerializer
from api.models import PaisMaestro, ConsumoPais, ProduccionPais
from api.models import HuellaPais, EmisionesContinente
from api.models import EmisionesPais , TemperaturaMundial
from api.models import MundialMaestro ,GasesMundial
from api.models import PrediccionMundial ,HuellaMundial

from rest_framework import generics, filters
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


class PaisConInformacionApiView(generics.ListAPIView):
    """
    Información General por país

    En estructura anidada 
    """
    serializer_class = PaisConInformacionSerializer

    def get_queryset(self):
        queryset = PaisMaestro.objects.all()[:3]
        return queryset


class HuellaPaisApiView(generics.ListAPIView):
    """
    KPI's histórico por país

    Principales métricas para cada pais según la ISO 3166
    """
    serializer_class = HuellaPaisSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('codigo','continente')

    search_fields = ['pais']

    def get_queryset(self):
        queryset = HuellaPais.objects.all()
        return queryset

class HuellaMundialApiView(generics.ListAPIView):
    """
    Histórico mundial de KPI's medioambientales

    biocapacidad -> Representa la disponibilidad de superficie biológicamente productiva por habitante. Unidad: gha/persona (1 gha es la capacidad productiva de 1 ha de tierra de producción media mundial)

    huella_ecológica -> Total de superficie ecológicamente productiva para producir los recursos consumidos por un habitante y los residuos que genera.  Unidad hgpc (hectárea global per Cópita: la capacidad productiva de 1 ha de tierra de producción media mundial)

    tierra -> Cociente  entre (huella ecologica/biocapacidad) define la cantidad de  planetas Tierra que se necesita para sustentar a la población.
    """
    serializer_class = HuellaMundialSerializer

    def get_queryset(self):
        queryset = HuellaMundial.objects.all()
        return queryset


class GasesMundialApiView(generics.ListAPIView):
    """
    Histórico mundial de gases del efecto invernadero

    Con unidades en MtCO₂e, N2O (Óxido Nitroso), SF6 (Hexafloruro de Azufre),
    CO2 (Dióxido de Carbono), CH4 (Metano), anio (año)
    """
    serializer_class = GasesMundialSerializer

    def get_queryset(self):
        queryset = GasesMundial.objects.all()
        return queryset


class TemperaturaMundialApiView(generics.ListAPIView):
    """
    Comportamiento histórico de la temperatura

    Medición global 
    """
    serializer_class = TemperaturaMundialSerializer

    def get_queryset(self):
        queryset = TemperaturaMundial.objects.all()
        return queryset

class EmisionesPaisApiView(generics.ListAPIView):
    serializer_class = EmisionesPaisSerializer

    def get_queryset(self):
        queryset = EmisionesPais.objects.all()
        return queryset



class HuellaGasesTemperaturaMundialApiView(generics.ListAPIView):
    """
    Información Mundial General

    Información general,en estructura anidada 
    """
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
    """
    Consumo de energía eléctrica por país

    El consumo está distribuido por tipos de fuentes de energía, código de país según ISO 3166 alfa-3, 
    otras energías renovables engloba a todas las energías renovables no mencionadas en la estructura JSON.
    """
    serializer_class = ConsumoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('codigo', )

    def get_queryset(self):
        queryset = ConsumoPais.objects.all()
        return queryset

class ProduccionApiView(generics.ListAPIView):
    """
    Producción de energía eléctrica por país

    La producción está distribuido por tipos de fuentes de energía, código de país según ISO 3166 alfa-3, 
    otras energías renovables engloba a todas las energías renovables no mencionadas en la estructura JSON.
    """
    serializer_class = ProduccionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('codigo',)

    def get_queryset(self):
        queryset = ProduccionPais.objects.all()
        return queryset

class EmisionesContinenteApiView(generics.ListAPIView):
    serializer_class = EmisionesContinenteSerializer

    def get_queryset(self):
        queryset = EmisionesContinente.objects.all()
        return queryset