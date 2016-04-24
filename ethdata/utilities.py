__author__ = 'smenji'
from django.shortcuts import render


def home(request):
    page_elements = "None"
    context_dict ={}
    context_dict['page_elements'] = page_elements

    return render(request, 'data_home.html', context_dict)