__author__ = 'admin'
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import slugify
from django.db.models import Count,Avg,Sum

from data.models import Crop, CropStatistics, Year, Region, Zone
from data.forms import ExportForm, ImportForm, AgriculturalProduction, AgriculturalProductionForm

def agricultural_production(request, year=None, sub_group=None):
    context_dict = {}

    if year==sub_group==None:
        crop_production = CropStatistics.objects.filter(
            crop__data_identifier="Sub", region__name="Ethiopia").order_by(
            '-year','-production_in_quintal')

        context_dict['data'] = crop_production

        return render(request, 'data/agriculture/agriculture.html', context_dict)

    if sub_group==None and year!= None:
        crop_production = CropStatistics.objects.filter(
            crop__data_identifier="Crop", region__name="Ethiopia",
            year__year_code=year).order_by(
            '-year','-production_in_quintal')

        context_dict['data'] = crop_production

        return render(request, 'data/agriculture/agriculture.html', context_dict)

    if sub_group!=None and year ==None:
        crop_production = CropStatistics.objects.filter(
            crop__sub_group_slug=sub_group, crop__data_identifier="Crop",
        zone__geo_choices="National",).order_by(
            '-year','-production_in_quintal')
        page_title = sub_group + " production in Ethiopia"
        context_dict['page_title'] = page_title
        context_dict['data'] = crop_production

        return render(request, 'data/agriculture/agriculture_national.html',
                      context_dict)

    if sub_group!=None and year !=None:
        crop_production = CropStatistics.objects.filter(
            crop__name_slug=sub_group, zone__geo_choices="Regional",
            year__year_code=year).order_by(
            '-year','-production_in_quintal')
        page_title = sub_group + " regional production in " +  year
        context_dict['page_title'] = page_title
        context_dict['data'] = crop_production

        return render(request, 'data/agriculture/agriculture_regional.html',
                      context_dict)


def agricultural_production_search(request):
    context_dict = {}
    form1 = AgriculturalProduction()
    form = AgriculturalProductionForm()
    context_dict['form1'] = form1
    context_dict['form'] = form
    context_dict['text'] = "Woops why"

    if request.method == 'GET':
        if request.GET['year'] != None:
            year = request.GET['year']
        else:
            year = None
        year = request.GET['year'] if request.GET['year'] != None else None
        region = request.GET['region'] if request.GET['region'] != None else \
            None
        zone = request.GET['zone'] if request.GET['zone'] != None else None
        crop = request.GET['crop'] if request.GET['crop'] != None else None

        if len(year)>1 and len(region)==len(zone)==len(crop)==0:
            crop_production = CropStatistics.objects.filter(
            crop__data_identifier="Sub",
            zone__geo_choices="National",year=year).order_by(
            '-year','-production_in_quintal')

            context_dict['data'] = crop_production

            return render(request, 'data/agriculture/search.html', context_dict)
        elif len(year)>0  and len(region)>0 and len(zone)==len(
                crop)==0:
            if region =="ethiopia":
                data_level = "National"
            else:
                data_level = "Regional"
            if data_level == "National":
                crop_production = CropStatistics.objects.filter(
                    crop__data_identifier="Crop",year=year,
                    zone__geo_choices=data_level).order_by(
                    '-year','-production_in_quintal')
                context_dict['level'] = "National"
                context_dict['data'] = crop_production
            elif data_level =="Regional":
                crop_production = CropStatistics.objects.filter(
                    crop__data_identifier="Crop",year=year,
                    zone__geo_choices=data_level,
                    region=region).order_by(
                    '-year','-production_in_quintal')

                context_dict['level'] = "Regional"
                context_dict['data'] = crop_production


            return render(request, 'data/agriculture/search.html', context_dict)

        elif len(year)>0 and len(region)>0 and len(zone)>0 and len(crop)>0:
            data_level = "Zonal"
            crop_production = CropStatistics.objects.filter(year=year,
                 region=region,zone=zone, crop=crop).order_by(
                 '-year','-production_in_quintal')
            context_dict['level'] = "Zonal"
            context_dict['data'] = crop_production

            return render(request, 'data/agriculture/search.html', context_dict)

        elif len(region)>0 and len(year)==len(zone)==len(crop)==0:
            data_level = "Regional"
            crop_production = CropStatistics.objects.filter(
                zone__geo_choices__in=("Regional","National"),
                region=region).order_by(
                 '-year','-production_in_quintal')
            context_dict['level'] = "Regional"
            context_dict['data'] = crop_production

            return render(request, 'data/agriculture/search.html', context_dict)

        elif len(region)>0 and len(zone)>0 and len(year)==len(crop)==0:
            data_level = "Zonal"
            crop_production = CropStatistics.objects.filter(
                zone__geo_choices=data_level,
                region=region, zone=zone).order_by(
                 '-year','-production_in_quintal')
            context_dict['level'] = "Zonal"
            context_dict['data'] = crop_production

            return render(request, 'data/agriculture/search.html', context_dict)

        elif len(region)>0 and len(crop)>0 and len(zone)==len(year)==0:
            data_level = "Regional"
            crop_production = CropStatistics.objects.filter(
                zone__geo_choices=data_level,
                region=region, crop=crop).order_by(
                 '-year','-production_in_quintal')
            context_dict['level'] = "Regional"
            context_dict['data'] = crop_production

            return render(request, 'data/agriculture/search.html', context_dict)

        elif len(zone)>0 and len(region)==len(year)==len(crop)==0:
            data_level = "Zonal"
            crop_production = CropStatistics.objects.filter(zone=zone, zone__geo_choices="Zonal").order_by(
                 '-year','-production_in_quintal')
            context_dict['level'] = "Zonal"
            context_dict['data'] = crop_production

            return render(request, 'data/agriculture/search.html', context_dict)

        elif len(zone)>0 and len(year)>0 and len(region)==len(crop)==0:
            data_level = "Zonal"
            crop_production = CropStatistics.objects.filter(zone=zone, year=year, zone__geo_choices="Zonal").order_by(
                 '-year','-production_in_quintal')
            context_dict['level'] = "Zonal"
            context_dict['data'] = crop_production

            return render(request, 'data/agriculture/search.html', context_dict)

        elif len(zone)>0 and len(crop)>0 and len(region)==len(region)==0:
            data_level = "Zonal"
            crop_production = CropStatistics.objects.filter(zone=zone, crop=crop, zone__geo_choices=data_level).order_by(
                 '-year','-production_in_quintal')
            context_dict['level'] = data_level
            context_dict['data'] = crop_production

            return render(request, 'data/agriculture/search.html', context_dict)

        elif len(crop)>0 and len(zone)==len(region)==len(year)==0:
            data_level = "National"
            crop_production = CropStatistics.objects.filter(crop=crop, zone__geo_choices=data_level).order_by(
                 '-year','-production_in_quintal')
            context_dict['level'] = data_level
            context_dict['data'] = crop_production

            return render(request, 'data/agriculture/search.html', context_dict)

        elif len(crop)>0 and len(year)>0 and len(zone)==len(region)==0:
            data_level = ["National", "Regional"]
            crop_production = CropStatistics.objects.filter(crop=crop, zone__geo_choices__in=data_level, year=year).order_by(
                 '-year','-production_in_quintal')
            context_dict['level'] = data_level
            context_dict['data'] = crop_production

            return render(request, 'data/agriculture/search.html', context_dict)

        elif len(year)>0 and len(region)>0 and len(zone)>0 and len(crop)==0:
            data_level = "Zonal"
            crop_production = CropStatistics.objects.filter(year=year,
                 zone__geo_choices=data_level,zone=zone, \
                                                     region=region).order_by(
                 '-year','-production_in_quintal')
            context_dict['level'] = "Zonal"
            context_dict['data'] = crop_production

            return render(request, 'data/agriculture/search.html', context_dict)

        else:
            response_txt = "you got here" + year + region + zone + crop + \
                           "True/False: "
            return HttpResponse(response_txt)

    else:
        crop_production = CropStatistics.objects.filter(
            crop__data_identifier="Sub", region__name="Ethiopia").order_by(
            '-year','-production_in_quintal')

        context_dict['data'] = crop_production

        return render(request, 'data/agriculture/search.html', context_dict)