from django.contrib import admin

from .models import *

admin.site.register(Farmer)
admin.site.register(Farmerlogin)

admin.site.register(Weather_Station)
admin.site.register(Climate)

admin.site.register(Plant)
admin.site.register(Soil_Moisture)

admin.site.register(Water_Body)
admin.site.register(Water_Level)

admin.site.register(Actuator)


