from django.shortcuts import render
from django.views.generic import ListView

from .models import HomePage, SubPages
# Create your views here.
class return_home_pages_list(ListView):
    model = HomePage
    template_name = ('utility/homepage_list.html')
    # context_object_name = 'object_list'

def return_home_pages_listfun(request):
    pages_list = HomePage.objects.all()


    return render(request, 'utility/homepage_list.html',{'object_list': pages_list })

