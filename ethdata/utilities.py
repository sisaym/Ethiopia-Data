__author__ = 'smenji'
from django.shortcuts import render
from data.models import HomeContent


def home(request):
    page_elements = HomeContent.objects.all()
    context_dict ={}
    context_dict['page_elements'] = page_elements

    return render(request, 'data_home.html', context_dict)