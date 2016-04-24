from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class PublicationsHome(TemplateView):
    template_name = 'publications/publications_list.html'
