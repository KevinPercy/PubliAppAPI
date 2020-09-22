from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.parsers import FileUploadParser

from publiapp_api import serializers
from publiapp_api import models
from publiapp_api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

    @action(
        methods=["put"],
        detail=True,
        serializer_class=serializers.PasswordSerializer,
        permission_classes=[permissions.IsSuperuserOrIsSelf],
        url_path="change-password",
        url_name="change_password",
    )
    def set_password(self, request, pk=None):
        serializer = serializers.PasswordSerializer(data=request.data)
        user = self.get_object()
        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"status": "password set"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        response = super(UserLoginApiView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({"token": token.key, "id": token.user_id})


class AnunciosViewSet(viewsets.ModelViewSet):
    """Administra la creacion y modificacion de anuncios"""
    search_fields = ['titulo_anuncio']
    filter_backends = (filters.SearchFilter,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.AnunciosSerializer
    queryset = models.Anuncio.objects.all()
    permission_classes = (permissions.IsSafeMethod,)


class DetalleAnuncioViewSet(viewsets.ModelViewSet):
    """Administra la creaction y modificacion de detallesAnuncios"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.DetalleAnuncioSerializer
    queryset = models.DetalleAnuncio.objects.all()
    permission_classes = (permissions.IsSafeMethod,)


class PrecioViewSet(viewsets.ModelViewSet):
    """Administra la creaction y modificacion de Precios"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.PrecioSerializer
    queryset = models.Precio.objects.all()
    permission_classes = (permissions.IsSafeMethod,)


class CategoriaViewSet(viewsets.ModelViewSet):
    """Administra la creaction y modificacion de categorias"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CategoriaSerializer
    queryset = models.Categoria.objects.all()
    permission_classes = (permissions.IsSafeMethod,)


class ReseniaViewSet(viewsets.ModelViewSet):
    """Administra la creaction y modificacion de categorias"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ReseniaSerializer
    queryset = models.Resenia.objects.all()
    permission_classes = (permissions.IsSafeMethod,)


class RolViewSet(viewsets.ModelViewSet):
    """Administra la creacion y modificacion de foles"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.RolSerializer
    queryset = models.Rol.objects.all()
    permission_classes = (permissions.IsSafeMethod,)


class AnuncianteViewSet(viewsets.ModelViewSet):
    """Administra la creacion y modificacion de Anunciantes"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.AnuncianteSerializer
    queryset = models.Anunciante.objects.all()
    permissions_classes = (permissions.IsSafeMethod,)


class ImagenUploadView(viewsets.ModelViewSet):
    """Administra la carga de imagenes """
    queryset = models.Imagen.objects.all()
    serializer_class = serializers.ImagenSerializer
