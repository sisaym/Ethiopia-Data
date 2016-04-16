__author__ = 'admin'
from django import forms
from .models import Commodity,Country, Item, Export, Year, Import, Region,\
    Year, Crop, CropStatistics, Zone


class ExportForm(forms.ModelForm):
    item = forms.CharField(max_length=250)


    class Meta:
        model= Export
        fields = ('year', 'item', 'destination')

class ImportForm(forms.ModelForm):
    item = forms.CharField(max_length=250)


    class Meta:
        model= Import
        fields = ('year', 'item', 'origin')

class AgriculturalProduction(forms.Form):
    year_choices = Year.objects.all()
    year = forms.SelectMultiple(choices=year_choices)
    region_choices = Region.objects.all()
    region = forms.Select(choices=region_choices)

class AgriculturalProductionForm(forms.ModelForm):
    # zone = forms.CharField(max_length=100)
    class Meta:
        model = CropStatistics
        fields = ('year', 'region','zone','crop' )