from django.urls import path
from api.api import ConsumoEnergiaPaisApiView
from api.api import DatosExtrasEnergiaPaisApiView
from api.api import GasesApiView
from api.api import HistoricoGhgApiView
from api.api import HuellaMundialApiView
from api.api import HuellaPaisApiView
from api.api import ProduccionEnergiaPaisApiView
from api.api import TemperaturaMundialApiView
from api.views import inicio ,apiGeoJson


urlpatterns = [
    path('consumo_por_fuente/', ConsumoEnergiaPaisApiView.as_view(), name='consumo_por_fuente_api'),
    path('extras/', DatosExtrasEnergiaPaisApiView.as_view(), name='extras_api'),
    path('gases/', GasesApiView.as_view(), name='gases_api'),
    path('historico_emisiones/', HistoricoGhgApiView.as_view(), name='historico_emisiones_api'),
    path('huella_mundial/', HuellaMundialApiView.as_view(), name='huellamundial_api'),
    path('huella__pais/', HuellaPaisApiView.as_view(), name='huellapais_api'),
    path('produccion_por_fuente/', ProduccionEnergiaPaisApiView.as_view(), name='produccion_por_fuente_api'),
    path('temperatura/', TemperaturaMundialApiView.as_view(), name='temperatura_api'),
    path('geojson/', apiGeoJson, name='geojson'),
    path('', inicio, name='GasesDetail'),
]