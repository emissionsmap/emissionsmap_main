from django.urls import path
from api.api import ElectricidadProdFuenteApiladaApiView
from api.api import Energiaco2ApiView
from api.api import GasesApiView
from api.api import HistoricEmissionsApiView
from api.api import HuellaBiocapacidadApiView
from api.api import HuellaSosteniblePorPaisApiView
from api.api import SubEnergiaFosilRenovablesNuclearApiView
from api.api import TemperaturaAnomaliaApiView

urlpatterns = [
    path('electricidad_por_fuente/', ElectricidadProdFuenteApiladaApiView.as_view(), name='electricidad_por_fuente_api'),
    path('energia_co2/', Energiaco2ApiView.as_view(), name='energia_co2_api'),
    path('gases/', GasesApiView.as_view(), name='gases_api'),
    path('historico_emisiones/', HistoricEmissionsApiView.as_view(), name='historico_emisiones_api'),
    path('historico_huella_mundial/', HuellaBiocapacidadApiView.as_view(), name='biocapacidad_api'),
    path('huella_actual_por_pais/', HuellaSosteniblePorPaisApiView.as_view(), name='huella_api'),
    path('fosil_renovable_nuclear/', SubEnergiaFosilRenovablesNuclearApiView.as_view(), name='fosil_renovable_nuclear_api'),
    path('temperatura/', TemperaturaAnomaliaApiView.as_view(), name='temperatura_api'),
]