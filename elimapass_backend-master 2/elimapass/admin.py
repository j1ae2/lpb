from django.contrib import admin

from elimapass.models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tarjeta)
admin.site.register(Paradero)
admin.site.register(Recarga)
admin.site.register(Ruta)
admin.site.register(ParaderoRuta)
admin.site.register(Bus)
admin.site.register(Viaje)
admin.site.register(Tarifa)