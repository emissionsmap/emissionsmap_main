from django.urls import path, re_path
from api.api import PaisConInformacionApiView
from api.api import HuellaPaisApiView
from api.api import EmisionesPaisApiView
from api.api import HuellaGasesTemperaturaMundialApiView
from api.api import PrediccionMundialApiView
from api.api import HuellaMundialApiView
from api.api import GasesMundialApiView
from api.api import TemperaturaMundialApiView
from api.views import apiGeoJson, topContinentes
from api.api import ConsumoApiView, ProduccionApiView
from api.api import EmisionesContinenteApiView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Api Documentación Emissions Maps',
        default_version='v1.0',
        contact=openapi.Contact(email="arodriguezv@uni.pe"),
        description = """
        !Gracias por interesarte en usar nuestra API!

        Encontraras diferentes puntos de entrada que puedes consumirlas
        de manera pública.Puede utilizar nuestra API para obtener acceso a información sobre:

        * Que fuentes de energía consumen los países en el mundo
        * Que fuentes de energía producen los países en el mundo
        * Comportamiento de la temperatura y los principales gases del efecto invernadero a través del tiempo

        Además, puede usar esta API para obtener la principales métricas mediambientales que se usan para medir
        el desarrollo sostenible de un país.

        Listo para comenzar?
        
        Adelante!
        """,

    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)


urlpatterns = [
    # path('emisiones_continente', EmisionesContinenteApiView().as_view(), name='emisiones_continente'),
    path('consumo', ConsumoApiView.as_view(), name='consumo'),
    path('produccion', ProduccionApiView.as_view(), name='produccion'),
    path('pais_general', PaisConInformacionApiView.as_view(), name='pais_general'),#x
    path('huella_pais', HuellaPaisApiView.as_view(), name='huella_pais'), #x
    path('huella_mundial', HuellaMundialApiView.as_view(), name='huella_mundial'), ########
    path('gases_mundial', GasesMundialApiView.as_view(), name='gases_mundial'), ########
    # path('temperatura_mundial', TemperaturaMundialApiView.as_view(), name='temperatura_mundial'), ########
    # path('emisiones_pais', EmisionesPaisApiView.as_view(), name='emisiones_pais'),########
    path('mundial_general', HuellaGasesTemperaturaMundialApiView.as_view(), name='mundial_general'),#x
    # path('prediccion_mundial', PrediccionMundialApiView.as_view(), name='prediccion_mundial'), ########
    path('geojson', apiGeoJson, name='geojson'),########
    path('top10', topContinentes, name='top10'),
    path('', schema_view.with_ui('redoc',cache_timeout=0), name='doc'),########
]