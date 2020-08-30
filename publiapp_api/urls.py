from django.urls import path, include
from rest_framework.routers import DefaultRouter

from publiapp_api import views

router = DefaultRouter()
router.register('profiles', views.UserProfileViewSet)
router.register('anuncios', views.AnuncioViewSet)
router.register('articulos', views.ArticuloViewSet)
router.register('negocios', views.NegocioViewSet)
router.register('servicios', views.ServicioViewSet)
router.register('categoria', views.CategoriaViewSet)
router.register('resenia', views.ReseniaViewSet)
router.register('rol', views.RolViewSet)
router.register('anunciante', views.AnuncianteViewSet)
router.register('imagen', views.ImagenUploadView)

urlpatterns = [
    # path('imagen/', views.ImagenUploadView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
