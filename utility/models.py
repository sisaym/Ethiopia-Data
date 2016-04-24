from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage


# Create your models here.
class HomePage(models.Model):
    home_fs = FileSystemStorage(location='/media/home_page')
    status_choices = (
        ("None", 'None'),
        ('Updated', 'Updated'),
        ('under_development', 'Under Development'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    page_url = models.CharField(max_length=100, blank=True)
    # sub-pages-ul will contain comma separated page urls
    bg_image =models.ImageField(null=True, default=None, storage=home_fs, upload_to="home_page")
    glyphicon_class = models.CharField(max_length=100, null=True, default=None)
    status = models.CharField(max_length=50,choices=status_choices, null=True, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        page_url = self.page_url
        return redirect(page_url)

class SubPages(models.Model):
    homepage = models.ForeignKey(HomePage, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500,blank=True)
    page_url = models.CharField(max_length=50)

    def __str__(self):
        return "{} : {}".format(self.homepage, self.title)

    def get_parent_page(self):
        parent_page_url = self.homepage.page_url
        return parent_page_url

    def get_absolute_url(self):
        page_url = self.get_parent_page() +'_'+self.page_url + ':' + self.page_url
        return reverse(page_url)
