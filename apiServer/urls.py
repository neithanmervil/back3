from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, NivelViewSet, PuntajeViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'niveles', NivelViewSet)
router.register(r'puntajes', PuntajeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
