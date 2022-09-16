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
from api.models import ConsumoEnergiaPais
from api.models import DatosExtrasEnergiaPais
from api.models import Gases
from api.models import HistoricoGhg
from api.models import HuellaMundial
from api.models import HuellaPais
from api.models import ProduccionEnergiaPais
from api.models import TemperaturaMundial


class ConsumoEnergiaPaisApiView(APIView):
    def get(self,request):
        obj = ConsumoEnergiaPais.objects.all()
        ser = ConsumoEnergiaPaisSerializer(obj, many=True)
        return Response(ser.data)

class DatosExtrasEnergiaPaisApiView(APIView):
    def get(self,request):
        obj = DatosExtrasEnergiaPais.objects.all()
        ser = DatosExtrasEnergiaPaisSerializer(obj, many=True)
        return Response(ser.data)
   
class GasesApiView(APIView):
    def get(self,request):
        obj = Gases.objects.all()
        ser = GasesSerializer(obj, many=True)
        return Response(ser.data)

class HistoricoGhgApiView(APIView):
    def get(self,request):
        obj = HistoricoGhg.objects.all()
        ser = HistoricoGhgSerializer(obj, many=True)
        return Response(ser.data)

class HuellaMundialApiView(APIView):
    def get(self,request):
        obj = HuellaMundial.objects.all()
        ser = HuellaMundialSerializer(obj, many=True)

        return Response(ser.data)
class HuellaPaisApiView(APIView):
    def get(self,request):
        obj = HuellaPais.objects.all()
        ser = HuellaPaisSerializer(obj, many=True)
        return Response(ser.data)

class ProduccionEnergiaPaisApiView(APIView):
    def get(self,request):
        obj = ProduccionEnergiaPais.objects.all()
        ser = ProduccionEnergiaPaisSerializer(obj, many=True)
        return Response(ser.data)

class TemperaturaMundialApiView(APIView):
    def get(self,request):
        obj = TemperaturaMundial.objects.all()
        ser = TemperaturaMundialSerializer(obj, many=True)
        return Response(ser.data)