from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.utils import timezone
from django.db.models import Lookup


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, last_name, dni, id_rol, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)  # takes care of the second half
        user = self.model(email=email,
                          name=name,
                          last_name=last_name,
                          dni=dni,
                          id_rol=id_rol)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, password)

        user.is_superuser = True  # automatically created in the PermissionsMixin
        user.is_staff = True

        user.save(using=self._db)

        return user


class Rol(models.Model):
    """Datos de Rol"""
    rol = models.CharField(max_length=2)

    def __str__(self):
        """retornar el valor de rol """
        return self.rol


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    dni = models.CharField(max_length=8)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    id_rol = models.ForeignKey(
        Rol,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    objects = UserProfileManager()

    USERNAME_FIELD = "email"

    #REQUIRED_FIELDS = ['email']

    def __str__(self):
        """Return the string representation of our user"""
        return self.email


class Ubigeo(models.Model):
    """Datos de Rol"""
    codigo_ubigeo = models.CharField(max_length=6)
    departamento = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    distrito = models.CharField(max_length=50)
    latitud = models.CharField(max_length=15)
    longitud = models.CharField(max_length=15)

    def __str__(self):
        """retornar el valor de rol """
        return self.codigo_ubigeo


class LogBusqueda(models.Model):
    """Datos de Rol"""
    palabra = models.CharField(max_length=30)
    dispositivo = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """retornar el valor de rol """
        return self.palabra + self.fecha.strftime("%Y%m%d%H%M%S")


class LogDetalleAnuncio(models.Model):
    """Datos de Rol"""
    id_anuncio = models.CharField(max_length=40)
    dispositivo = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """retornar el valor de rol """
        return self.fecha.strftime("%Y%m%d%H%M%S") + self.id_anuncio


class LogContacto(models.Model):
    """Datos de Rol"""
    id_anuncio = models.CharField(max_length=40)
    dispositivo = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=timezone.now)
    nro_telefono = models.CharField(max_length=15)

    def __str__(self):
        """retornar el valor de rol """
        return self.fecha.strftime("%Y%m%d%H%M%S") + self.nro_telefono


class Constantes(models.Model):
    """System constants"""
    description = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    value = models.CharField(max_length=10)

    def __str__(self):
        """return system code"""
        return self.description


class Anunciante(models.Model):
    """Datos del Anunciante"""
    nombre = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    dni = models.CharField(max_length=8)
    email = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(default=timezone.now)
    id_rol = models.ForeignKey(
        Rol,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        """return Anunciante"""
        return self.nombre


class Categoria(models.Model):
    """Datos de las Categorias"""
    nombre_categoria = models.CharField(max_length=40)
    tipo_categoria = models.CharField(max_length=10)

    def __str__(self):
        """retorna el nombre de la categoría"""
        return self.nombre_categoria


class Anuncio(models.Model):
    """Datos de anuncio"""
    titulo_anuncio = models.CharField(max_length=100)
    fecha_anuncio = models.DateTimeField(default=timezone.now)
    fecha_fin = models.DateTimeField(default=timezone.now)
    direccion = models.CharField(max_length=150)
    telefono1 = models.CharField(max_length=15)
    telefono2 = models.CharField(max_length=15)
    estado = models.PositiveIntegerField(default=0)  # positive integer
    nivel_anuncio = models.CharField(max_length=1)
    anunciante = models.ForeignKey(
        Anunciante,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    ubigeo = models.ForeignKey(Ubigeo,
                               related_name='ubigeo',
                               on_delete=models.CASCADE)

    def __str__(self):
        """Retornar el titulo del anuncio como string"""
        return self.titulo_anuncio


class DetalleAnuncio(models.Model):
    """Datos de los anuncios(Articulo, Negocio, Servicio)"""
    anuncio = models.ForeignKey(Anuncio,
                                related_name='detalleAnuncio',
                                on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=800)
    tipoAnuncio = models.ForeignKey(
        Constantes,
        on_delete=models.CASCADE,
    )
    categoria = models.ForeignKey(Categoria,
                                  related_name='categoria',
                                  on_delete=models.CASCADE)

    def __str__(self):
        """retorna el nombre del articulo"""
        return self.nombre


class ArticuloOcacional(models.Model):
    """Datos de los anuncios ocacionales (Articulo, Negocio, Servicio)"""
    anuncio = models.ForeignKey(Anuncio,
                                related_name='articuloOcacional',
                                on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=800)
    id_categoria = models.ForeignKey(
        Categoria,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        """retorna el nombre del articulo"""
        return self.nombre


class Resenia(models.Model):
    """Datos de las Resenias"""
    anuncio = models.ForeignKey(Anuncio,
                                related_name='resenia',
                                on_delete=models.CASCADE)
    comentario = models.CharField(max_length=40)
    puntuacion = models.IntegerField(default=0)
    equipo = models.CharField(max_length=100, default='ND')  # No Definido
    usuario = models.CharField(max_length=100)

    def __str__(self):
        """retorna el nombre de la resenia"""
        return self.equipo


class Precio(models.Model):
    """Datos de los precios por anuncio"""
    anuncio = models.ForeignKey(Anuncio,
                                related_name='precios',
                                on_delete=models.CASCADE)
    concepto = models.CharField(max_length=100)
    monto = models.FloatField(default=0.0)
    monto_promo = models.FloatField(default=0.0)
    moneda = models.IntegerField(default=0)

    def __str__(self):
        """Retorna concepto Precio"""
        return self.concepto


class Imagen(models.Model):
    """Datos de la imagen"""
    imagen = models.FileField(blank=False, null=False)
    es_principal = models.BooleanField(default=False)
    id_anuncio = models.ForeignKey(Anuncio,
                                   on_delete=models.CASCADE,
                                   related_name='imagenes')

    def __str__(self):
        return self.imagen.name


class NotEqual(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' % (lhs, rhs), params
