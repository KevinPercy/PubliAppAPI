from rest_framework import serializers
from publiapp_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ("id", "name", "last_name", "dni", "id_rol", "email",
                  "password")
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
            last_name=validated_data["last_name"],
            dni=validated_data["dni"],
            id_rol=validated_data["id_rol"],
            password=validated_data["password"])

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


class UbigeoSerializer(serializers.ModelSerializer):
    """Serializer para Ubigeo"""
    class Meta:
        model = models.Ubigeo
        fields = "__all__"


class AnuncianteSerializer(serializers.ModelSerializer):
    """Serializer para anunciantes"""
    class Meta:
        model = models.Anunciante
        fields = ("id", "nombre", "apellidos", "dni", "email",
                  "fecha_registro", "id_rol")
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
        fields = "__all__"


class FilteredDetalleSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        qry_categoria = self.context['request'].GET.get('id_categoria')
        data = data.filter(id_categoria=qry_categoria)
        return super(FilteredDetalleSerializer, self).to_representation(data)


class DetalleAnuncioSerializer(serializers.ModelSerializer):
    """Serializer para  detalles de anuncios"""
    class Meta:
        model = models.DetalleAnuncio
        fields = "__all__"


class ArticuloOcacionalSerializer(serializers.ModelSerializer):
    """Serializer para  articulos ocacionales"""
    class Meta:
        model = models.ArticuloOcacional
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
    articuloOcacional = ArticuloOcacionalSerializer(many=True, read_only=True)
    precios = PrecioSerializer(many=True, read_only=True)
    resenia = ReseniaSerializer(many=True, read_only=True)
    ubigeo = UbigeoSerializer(read_only=True)
    # id_categoria = serializers.SerializerMethodField('get_categoriaID')
    ubigeo_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Ubigeo.objects.all(),
        source='ubigeo',
        write_only=True,
        allow_null=False)

    # def get_categoriaID(self, obj):
    #     categoria_id = models.DetalleAnuncio.objects.filter(id_categoria=obj)
    #     serializer = DetalleAnuncioSerializer(
    #         categoria_id)
    #     return serializer.data

    class Meta:
        model = models.Anuncio
        fields = (
            "id",
            "titulo_anuncio",
            "fecha_anuncio",
            "fecha_fin",
            "direccion",
            "telefono1",
            "telefono2",
            "estado",
            "nivel_anuncio",
            "anunciante",
            "detalleAnuncio",
            "articuloOcacional",
            "precios",
            "imagenes",
            "ubigeo",
            "ubigeo_id",
            "resenia",
        )
