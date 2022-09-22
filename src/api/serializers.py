from rest_framework import serializers
from api.models import PaisMaestro
from api.models import InformacionPais
from api.models import ConsumoPais
from api.models import ProduccionPais
from api.models import HuellaPais
from api.models import EmisionesPais
from api.models import MundialMaestro
from api.models import HuellaMundial
from api.models import GasesMundial
from api.models import TemperaturaMundial
from api.models import PrediccionMundial


class InformacionPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacionPais
        fields = '__all__'


class ConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumoPais
        exclude = ('informacion',)

class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduccionPais
        exclude = ('informacion',)

class ConsumoPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumoPais
        exclude = ('id','anio','codigo','informacion')

class ProduccionPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduccionPais
        exclude = ('id','anio','codigo','informacion')

class ConsumoProduccionInformacionSerializer(serializers.ModelSerializer):
    consumo = ConsumoPaisSerializer(many=True, source='informacion_consumo')
    produccion = ProduccionPaisSerializer(many=True, source='informacion_produccion')
    
    class Meta:
        model = InformacionPais
        fields = ['anio','poblacion','pbi','gen_elect','dem_elect','consumo','produccion']

class PaisConInformacionSerializer(serializers.ModelSerializer):
    informacion = ConsumoProduccionInformacionSerializer(many=True, source='pais_informacion')
    
    class Meta:
        model = PaisMaestro
        fields = ['id','pais','informacion']

class HuellaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuellaPais
        exclude = ('idpais','idcontinente')

class EmisionesPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmisionesPais
        fields = '__all__'

class HuellaMundialSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuellaMundial
        fields = '__all__'

class GasesMundialSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasesMundial
        fields = '__all__'

class TemperaturaMundialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperaturaMundial
        fields = '__all__'

class HuellaGasesTemperaturaMundialSerializer(serializers.ModelSerializer):
    huella = HuellaMundialSerializer(many=True, source='mundial_huella')
    gases = GasesMundialSerializer(many=True, source='mundial_gases')
    temperatura = TemperaturaMundialSerializer(many=True, source='mundial_temperatura')
    
    class Meta:
        model = MundialMaestro
        fields = ['anio','poblacion','huella','gases','temperatura']


class PrediccionMundialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrediccionMundial
        fields = '__all__'