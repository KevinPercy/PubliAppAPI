from django.contrib import admin

from publiapp_api import models
from django.db.models import Field

admin.site.register(models.UserProfile)
admin.site.register(models.Constantes)
admin.site.register(models.Anuncio)
admin.site.register(models.DetalleAnuncio)
admin.site.register(models.Precio)
admin.site.register(models.Categoria)
admin.site.register(models.Resenia)
admin.site.register(models.Rol)
admin.site.register(models.Ubigeo)
admin.site.register(models.Anunciante)
admin.site.register(models.Imagen)
admin.site.register(models.LogBusqueda)
admin.site.register(models.LogDetalleAnuncio)
admin.site.register(models.LogContacto)
admin.site.register(models.ArticuloOcacional)

Field.register_lookup(models.NotEqual)
