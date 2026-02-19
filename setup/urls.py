from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_telemetria.api import viewsets  

router = routers.DefaultRouter()

router.register(r'marcas', viewsets.MarcaViewSet)
router.register(r'modelos', viewsets.ModeloViewSet)
router.register(r'veiculos', viewsets.VeiculoViewSet)
router.register(r'unidades-medida', viewsets.UnidadeMedidaViewSet)
router.register(r'medidas', viewsets.MedidaViewSet)
router.register(r'medicoes-veiculo', viewsets.MedicaoVeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
