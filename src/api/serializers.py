from rest_framework import serializers
from api.models import ConsumoEnergiaPais
from api.models import DatosExtrasEnergiaPais
from api.models import Gases
from api.models import HistoricoGhg
from api.models import HuellaMundial
from api.models import HuellaPais
from api.models import ProduccionEnergiaPais
from api.models import TemperaturaMundial

class ConsumoEnergiaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumoEnergiaPais
        fields = '__all__'

class DatosExtrasEnergiaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosExtrasEnergiaPais
        fields = '__all__'

class GasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gases
        fields = '__all__'

class HistoricoGhgSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoGhg
        fields = '__all__'

class HuellaMundialSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuellaMundial
        fields = '__all__'

class HuellaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuellaPais
        fields = '__all__'

class ProduccionEnergiaPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduccionEnergiaPais
        fields = '__all__'

class TemperaturaMundialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperaturaMundial
        fields = '__all__'