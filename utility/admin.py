from django.contrib import admin

from .models import *
# Register your models here.
class SubPageInline(admin.StackedInline):
    model = SubPages
    list = 3

class HomePageAdmin(admin.ModelAdmin):
    inlines = (SubPageInline,)

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(SubPages)
