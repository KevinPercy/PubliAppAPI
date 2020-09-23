from rest_framework import serializers
from publiapp_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password"
                }
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"]
        )

        return user


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class RolSerializer(serializers.ModelSerializer):
    """Serializer para Roles"""

    class Meta:
        model = models.Rol
        fields = "__all__"


class ConstanstesSerializer(serializers.ModelSerializer):
    """Serializer para Constantes"""
    class Meta:
        model = models.Constantes
        fields = "__all__"


class AnuncianteSerializer(serializers.ModelSerializer):
    """Serializer para anunciantes"""

    class Meta:
        model = models.Anunciante
        fields = ("id", "nombre", "apellidos", "dni",
                  "email", "fecha_registro", "id_rol")
        # extra_kwargs = {
        #     'id_rol': {
        #         'read_only': True
        #     }
        # }


class CategoriaSerializer(serializers.ModelSerializer):
    """Serializer para categorias"""
    class Meta:
        model = models.Categoria
        fields = ("id", "nombre_categoria", "tipo_categoria")


class ReseniaSerializer(serializers.ModelSerializer):
    """Serializer para resenia"""
    class Meta:
        model = models.Resenia
        fields = ("id", "comentario", "puntuacion", "equipo")


class DetalleAnuncioSerializer(serializers.ModelSerializer):
    """Serializer para  detalles de anuncios"""
    class Meta:
        model = models.DetalleAnuncio
        fields = "__all__"


class PrecioSerializer(serializers.ModelSerializer):
    """Serializer de precios"""
    class Meta:
        model = models.Precio
        fields = "__all__"


class ImagenSerializer(serializers.ModelSerializer):
    """Serializer para las imagenes"""
    # imagen = serializers.ImageField(max_length=None, use_url=True)
    # es_principal = serializers.BooleanField(default=False)

    class Meta:
        model = models.Imagen
        fields = ('imagen', 'es_principal', 'id_anuncio')


class AnunciosSerializer(serializers.ModelSerializer):
    """Serializer para anuncios"""

    imagenes = ImagenSerializer(many=True, read_only=True)
    detalleAnuncio = DetalleAnuncioSerializer(many=True, read_only=True)
    precios = PrecioSerializer(many=True, read_only=True)

    class Meta:
        model = models.Anuncio
        fields = ("id", "titulo_anuncio", "fecha_anuncio", "fecha_fin", "direccion", "telefono1", "telefono2",
                  "estado", "nivel_anuncio", "anunciante", "detalleAnuncio", "precios", "imagenes"
                  )
