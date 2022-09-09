from rest_framework import serializers
from api.models import ElectricidadProdFuenteApilada
from api.models import Energiaco2
from api.models import Gases
from api.models import HistoricEmissions
from api.models import HuellaBiocapacidad
from api.models import HuellaSosteniblePorPais
from api.models import SubEnergiaFosilRenovablesNuclear
from api.models import TemperaturaAnomalia


class ElectricidadProdFuenteApiladaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricidadProdFuenteApilada
        fields = ('codigo','pais','continente','anio','petroleo','carbon','gas','hidro',
                    'solar','viento','nuclear','otras_renovables')

class Energiaco2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Energiaco2
        fields = ('codigo','pais','continente','anio','combustible',
                    'pib','intensidad_energetica_percap','emision_co2',
                    'consumo_energia_twh','produccion_energia_twh','intensidad_energetica_percap_twh')

class GasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gases
        fields  = ('anio','oxido_nitroso','hexafloruro_azufre','dioxido_carbono','metano')

class HistoricEmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricEmissions
        fields = '__all__'

class HuellaBiocapacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuellaBiocapacidad
        fields = ('anio','poblacion','biocapacidad_percap','huella_ecologica_percap','tierra')

class HuellaSosteniblePorPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuellaSosteniblePorPais
        fields = ('codigo','pais','continente','desarrollo_sostenible','expectativa_vida',
                'indice_desarrollo_humano','pib_percap','grupo_ingresos','poblacion','huella_carbono',
                'huella_ecologica','biocapacidad','tierra')

class SubEnergiaFosilRenovablesNuclearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubEnergiaFosilRenovablesNuclear
        fields = ('codigo','pais','continente','anio','combustibles_fosiles','renovables','nuclear')

class TemperaturaAnomaliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperaturaAnomalia
        fields = ('anio','temperatura_media','limite_inferior','limite_superior')