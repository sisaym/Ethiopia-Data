from tastypie.api import Api
from tastypie import fields
from tastypie.resources import ModelResource

from data.models import CropStatistics, Export, Import, Crop, Year, Region, Zone

class CropName(ModelResource):
    class Meta:
        queryset = Crop.objects.all()
        resource_name = 'crop_name'

class CropResource(ModelResource):
    # crop = fields.ForeignKey(CropName, 'crop')
    crop = fields.CharField(attribute='crop')
    region = fields.CharField(attribute='region')
    zone = fields.CharField(attribute='zone')
    year = fields.CharField(attribute='year')

    class Meta:
        queryset = CropStatistics.objects.all()
        resource_name = 'crop_data'

class ExportResource(ModelResource):
    year = fields.CharField(attribute='year')
    class Meta:
        queryset = Export.objects.all()
        item = fields.CharField(attribute='item')
        destination = fields.CharField(attribute='destination')
        resource_name = 'exports'

class ImportResource(ModelResource):
    year = fields.CharField(attribute='year')
    origin = fields.CharField(attribute='origin')
    consignment = fields.CharField(attribute='consignment')
    item = fields.CharField(attribute='item')


    class Meta:
        queryset = Import.objects.all()
        resource_name ='imports'


data_api = Api(api_name='data')
data_api.register(CropResource())
data_api.register(ExportResource())
data_api.register(ImportResource())
data_api.register(CropName())

