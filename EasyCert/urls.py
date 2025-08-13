from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ContratoViewSet, ArchivoUsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'contratos', ContratoViewSet)
router.register(r'archivos', ArchivoUsuarioViewSet)

urlpatterns = router.urls
