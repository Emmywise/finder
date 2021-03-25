from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(building_data)
admin.site.register(meter_data)
admin.site.register(hourly_data)