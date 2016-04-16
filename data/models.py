from django.db import models
from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage
# Create your models here.
class Year(models.Model):
    year_code = models.IntegerField(primary_key=True)
    ethiopian_year = models.CharField(max_length=7)
    european_year = models.CharField(max_length=7)
    # Ethiopian and European year taking the starting year
    eth_year = models.IntegerField()
    eur_year = models.IntegerField()

    def __str__(self):
        return self.year_code.__str__()

class Commodity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, null=True)
    commodity = models.ForeignKey(Commodity)
    name_slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name).__str__()
        super(Item, self).save(*args, **kwargs)

class Country(models.Model):
    name = models.CharField(max_length=100)
    name_slug = models.SlugField(max_length=110)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name).__str__()
        super(Country, self).save(*args, **kwargs)

class Export(models.Model):
    year = models.ForeignKey(Year)
    item = models.ForeignKey(Item, null=True)
    Volume_in_tons = models.FloatField()
    fob_Value_in_usd = models.IntegerField(verbose_name="Export FOB value in "
                                                        "USD")
    fob_Value_in_etb = models.IntegerField(verbose_name="Export FOB value in "
                                                        "ETB", null=True)
    destination = models.ForeignKey(Country)


    def __str__(self):
        return "{0}: {1} tons exported with {2} USD earnings".format(
            self.year, self.Volume_in_tons, self.fob_Value_in_usd)




class Import(models.Model):
    year = models.ForeignKey(Year)
    item = models.ForeignKey(Item, null=True)
    Volume_in_tons = models.FloatField(verbose_name="Volume-tons")
    cif_Value_in_usd = models.FloatField(verbose_name="Import CIF value in "
                                                        "USD")
    cif_Value_in_etb = models.FloatField(verbose_name="Import CIF value in "
                                                        "ETB", null=True)
    origin = models.ForeignKey(Country, verbose_name="Country of origin",
                               related_name="origin_country")
    consignment = models.ForeignKey(Country, verbose_name="Country of "
                                                          "consignment",
                                    related_name="consignment_origin", null=True)

    def __str__(self):
        return "{0}: {1} tons imported amounting {2} USD ".format(
            self.year, self.Volume_in_tons, self.cif_Value_in_usd)

class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name="Region")
    flag = models.ImageField(verbose_name="region_flag",null=True)
    name_slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name).__str__()
        super(Region, self).save(*args, **kwargs)

class Zone(models.Model):
    # geo choices identify whether a data is national, regional or zonal
    geo_choices = (
        ('Zonal', 'Zonal'),
        ('Regional', 'Regional'),
        ('National', 'National')
    )
    name = models.CharField(max_length=60, verbose_name="Zone")
    region = models.ForeignKey(Region)
    flag = models.ImageField(verbose_name="zone_flag",null=True)
    name_slug = models.SlugField()
    geo_choices = models.CharField(max_length=10,choices=geo_choices,
                                       default="Zonal")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name).__str__()
        super(Zone, self).save(*args, **kwargs)


class Crop(models.Model):
    crop_choices = (
        ('Crop', 'Crop'),
        ('Sub', 'Crop_sub_group'),
        ('Major', 'Crop_major_group')
    )
    name = models.CharField(max_length=60, verbose_name="Crop")
    major_group = models.CharField(max_length=30, verbose_name="Major Group")
    sub_group = models.CharField(max_length=30, verbose_name="Sub Group")
    flag = models.ImageField(verbose_name="crop_flag", null=True)
    name_slug = models.SlugField()
    major_group_slug = models.SlugField()
    sub_group_slug = models.SlugField()
    data_identifier = models.CharField(max_length=50,choices=crop_choices,
                                       default="Crop")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name).__str__()
        self.major_group_slug = slugify(self.major_group).__str__()
        self.sub_group_slug = slugify(self.sub_group).__str__()
        super(Crop, self).save(*args, **kwargs)

    def is_crop(self):
        return self.name_slug != self.sub_group_slug

    def is_sub_group(self):
        return self.name_slug == self.sub_group_slug != self.major_group_slug

    def is_major_group(self):
        return self.name_slug == self.sub_group_slug == self.major_group_slug


class CropStatistics(models.Model):
    year = models.ForeignKey(Year)
    crop = models.ForeignKey(Crop)
    region = models.ForeignKey(Region)
    zone = models.ForeignKey(Zone)
    production_in_quintal = models.FloatField(verbose_name="Production ("
                                                            "Quintal)")
    area_cultivate_in_hectares = models.FloatField(verbose_name="Area ("
                                                                "Hectares)")
    farmers_growing_crop = models.FloatField(verbose_name="Farmers growing "
                                                          "the crop")
    yield_in_quintal_per_hectare = models.FloatField(
        verbose_name="Yield-Qt/ha")
    data_missing = models.BooleanField(default=True)










# *********************** UTILITY MODELS ******************************


class HomeContent(models.Model):
    home_fs = FileSystemStorage(location='/media/home_page')
    status_choices = (
        ("None", 'None'),
        ('Updated', 'Updated'),
        ('under_development', 'Under Development'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    page_url = models.CharField(max_length=100)
    # sub-pages-ul will contain comma separated page urls
    sub_pages_url = models.CharField(max_length=300, help_text="Please insert comma separated list of pages urls", null=True)
    bg_image =models.ImageField(null=True, default=None, storage=home_fs, upload_to="home_page")
    glyphicon_class = models.CharField(max_length=100, null=True, default=None)
    status = models.CharField(max_length=50,choices=status_choices, null=True, default=None)

    def __str__(self):
        return self.title


