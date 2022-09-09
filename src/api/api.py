from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ElectricidadProdFuenteApiladaSerializer
from api.serializers import Energiaco2Serializer
from api.serializers import GasesSerializer
from api.serializers import HistoricEmissionsSerializer
from api.serializers import HuellaBiocapacidadSerializer
from api.serializers import HuellaSosteniblePorPaisSerializer
from api.serializers import SubEnergiaFosilRenovablesNuclearSerializer
from api.serializers import TemperaturaAnomaliaSerializer
from api.models import ElectricidadProdFuenteApilada
from api.models import Energiaco2
from api.models import Gases
from api.models import HistoricEmissions
from api.models import HuellaBiocapacidad
from api.models import HuellaSosteniblePorPais
from api.models import SubEnergiaFosilRenovablesNuclear
from api.models import TemperaturaAnomalia

class ElectricidadProdFuenteApiladaApiView(APIView):
    def get(self,request):
        obj = ElectricidadProdFuenteApilada.objects.all()
        ser = ElectricidadProdFuenteApiladaSerializer(obj, many=True)
        return Response(ser.data)

class Energiaco2ApiView(APIView):
    def get(self,request):
        obj = Energiaco2.objects.all()
        ser = Energiaco2Serializer(obj, many=True)
        return Response(ser.data)
   
class GasesApiView(APIView):
    def get(self,request):
        obj = Gases.objects.all()
        ser = GasesSerializer(obj, many=True)
        return Response(ser.data)

class HistoricEmissionsApiView(APIView):
    def get(self,request):
        obj = HistoricEmissions.objects.all()
        ser = HistoricEmissionsSerializer(obj, many=True)
        return Response(ser.data)

class HuellaBiocapacidadApiView(APIView):
    def get(self,request):
        obj = HuellaBiocapacidad.objects.all()
        ser = HuellaBiocapacidadSerializer(obj, many=True)

        return Response(ser.data)
class HuellaSosteniblePorPaisApiView(APIView):
    def get(self,request):
        obj = HuellaSosteniblePorPais.objects.all()
        ser = HuellaSosteniblePorPaisSerializer(obj, many=True)
        return Response(ser.data)

class SubEnergiaFosilRenovablesNuclearApiView(APIView):
    def get(self,request):
        obj = SubEnergiaFosilRenovablesNuclear.objects.all()
        ser = SubEnergiaFosilRenovablesNuclearSerializer(obj, many=True)
        return Response(ser.data)

class TemperaturaAnomaliaApiView(APIView):
    def get(self,request):
        obj = TemperaturaAnomalia.objects.all()
        ser = TemperaturaAnomaliaSerializer(obj, many=True)
        return Response(ser.data)