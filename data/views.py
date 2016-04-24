from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your content here.
class dataApi(TemplateView):
    template_name = 'data/api.html'

class ExploreView(TemplateView):
    template_name = 'data/explore.html'
