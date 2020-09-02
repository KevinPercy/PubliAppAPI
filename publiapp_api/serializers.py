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


class ArticuloSerializer(serializers.ModelSerializer):
    """Serializer para Articulos"""
    class Meta:
        model = models.Articulo
        fields = ("id", "nombre_articulo", "descripcion_articulo",
                  "precio", "precio_promo", "id_categoria", "id_resenia")


class NegocioSerializer(serializers.ModelSerializer):
    """Serializer para negocios"""
    class Meta:
        model = models.Negocio
        fields = ("id", "nombre_negocio", "descripcion_negocio",
                  "precio", "precio_promo", "id_categoria", "id_resenia")


class ServicioSerializer(serializers.ModelSerializer):
    """Serializer para servicios"""
    class Meta:
        model = models.Servicio
        fields = ("id", "nombre_servicio", "descripcion_servicio",
                  "precio", "precio_promo", "id_categoria", "id_resenia")


class ImagenSerializer(serializers.ModelSerializer):
    """Serializer para las imagenes"""
    # imagen = serializers.ImageField(max_length=None, use_url=True)
    # es_principal = serializers.BooleanField(default=False)

    class Meta:
        model = models.Imagen
        fields = ('imagen', 'es_principal', 'id_anuncio')


class AnuncioSerializer(serializers.ModelSerializer):
    """Serializer para anuncios"""

    imagenes = ImagenSerializer(many=True)

    class Meta:
        model = models.Anuncio
        fields = ("id", "titulo_anuncio", "fecha_anuncio", "fecha_fin", "direccion", "telefono1", "telefono2",
                  "estado", "nivel_anuncio", "id_anunciante", "id_articulo", "id_negocio", "id_servicio", "imagenes")

    def create(self, validated_data):
        anuncio = models.Anuncio(titulo_anuncio=validated_data.get("titulo_anuncio"),
                                 fecha_anuncio=validated_data.get(
                                     "fecha_anuncio"),
                                 fecha_fin=validated_data.get("fecha_fin"),
                                 direccion=validated_data.get("direccion"),
                                 telefono1=validated_data.get("telefono1"),
                                 telefono2=validated_data.get("telefono2"),
                                 estado=validated_data.get("estado"),
                                 nivel_anuncio=validated_data.get(
                                     "nivel_anuncio"),
                                 id_anunciante=validated_data.get(
                                     "id_anunciante"),
                                 id_articulo=validated_data.get("id_articulo"),
                                 id_servicio=validated_data.get("id_servicio")
                                 )
        anuncio.save()
        imagenes = validated_data.get('imagenes')
        for imagen in imagenes:
            models.Imagen.objects.create(id_anuncio=anuncio, **imagen)
        return validated_data
