from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Year)
admin.site.register(Commodity)
admin.site.register(Item)
admin.site.register(Country)
admin.site.register(Export)
admin.site.register(Import)
admin.site.register(Crop)
admin.site.register(CropStatistics)
admin.site.register(Zone)
admin.site.register(Region)
