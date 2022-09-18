from django.urls import path, re_path
from api.api import DatosExtrasEnergiaPaisApiView
from api.api import GasesApiView
from api.api import HistoricoGhgApiView
from api.api import HuellaMundialApiView
from api.api import HuellaPaisApiView
from api.api import ProduccionEnergiaPaisApiView
from api.api import TemperaturaMundialApiView
from api.api import PrediccionesApiView
from api.views import inicio ,apiGeoJson

from api.api import ConsumoEnergiaPaisApiView
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Api Documentación',
        default_version='v1.0',
        description = "Documentación pública de la api de mapa de emisiones",

    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)


urlpatterns = [
    path('consumo/', ConsumoEnergiaPaisApiView.as_view(), name='consumo_api'),
    path('extras/', DatosExtrasEnergiaPaisApiView.as_view(), name='extras_api'),
    path('gases/', GasesApiView.as_view(), name='gases_api'),
    path('historico_emisiones/', HistoricoGhgApiView.as_view(), name='historico_emisiones_api'),
    path('huella_mundial/', HuellaMundialApiView.as_view(), name='huellamundial_api'),
    path('huella__pais/', HuellaPaisApiView.as_view(), name='huellapais_api'),
    path('produccion_por_fuente/', ProduccionEnergiaPaisApiView.as_view(), name='produccion_por_fuente_api'),
    path('temperatura/', TemperaturaMundialApiView.as_view(), name='temperatura_api'),
    path('geojson/', apiGeoJson, name='geojson'),
    path('predicciones/', PrediccionesApiView.as_view(), name='predicciones'),
    path('', schema_view.with_ui('redoc',cache_timeout=0), name='doc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]