__author__ = 'admin'
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import slugify
from django.db.models import Count,Avg,Sum

from data.models import Import, Export, Year, Country, Item, Commodity, Crop,\
    CropStatistics,Zone
from data.forms import ExportForm, ImportForm

# Utility functions
def Nation_Name(country_id):
    """
    function to get the name of a country from the id
    :param request:
    :param country_id: the id of the country
    :return:string name of the country
    """

    nation = Country.objects.get(pk=country_id)
    nation_name = nation.name

    if nation_name:
        return nation_name
    else:
        return "Not found"



# Functions to generate views for export pages

def export(request):
    context_dict = {}
    export_form = ExportForm()
    if export_form:
        context_dict['form'] = export_form
    exports = Export.objects.values('year').annotate(export_amount=Sum(
        'Volume_in_tons'),
        export_usd=Sum(
        'fob_Value_in_usd'), export_etb=Sum('fob_Value_in_etb')).order_by(
        '-year')

    context_dict['data'] = exports

    return render(request, 'data/exports/export.html', context_dict)


def export_for_year(request, year, destination=None):
    context_dict = {}
    if destination is None:
        exports = Export.objects.filter(year=year)
        exports = exports.values('destination').annotate(fob_Value_in_usd=Sum(
            'fob_Value_in_usd'),Volume_in_tons=Sum('Volume_in_tons'),
                                                         fob_Value_in_etb=Sum('fob_Value_in_etb')).order_by('-fob_Value_in_usd')

        # replace destination id's with names to solve problem caused by
        # using values to aggregate over
        for i in range(len(exports)):
            destination_id = exports[i]['destination']
            exports[i]['destination'] = Nation_Name(destination_id)


        context_dict['data'] = exports
        context_dict['year'] = year

        return render(request, 'data/exports/export_by_year.html', context_dict)
    else:
        exports = Export.objects.filter(year=year,
                                        destination__name_slug=destination).order_by(
            '-fob_Value_in_usd')
        context_dict['data'] = exports
        context_dict['year'] = year

        return render(request, 'data/exports/export_by_year_destination.html', context_dict)


def export_by_item(request, item, destination=None):
    context_dict = {}
    if destination is None:
        exports = Export.objects.all().filter(item__name_slug=item).order_by(
            '-year')
        context_dict['item'] = item
        context_dict['data'] = exports

        return render(request, 'data/exports/export_by_item.html', context_dict)

    else:
        exports = Export.objects.all().filter(item__name_slug=item,
                                        destination__name_slug=destination).order_by(
            '-year')
        context_dict['item'] = item
        context_dict['data'] = exports
        context_dict['destination'] = destination

        return render(request, 'data/exports/export_by_item_destination.html', context_dict)


def export_search(request):
    context_dict = {}

    form = ExportForm()
    context_dict['form'] = form
    error = False
    if request.method == 'POST':
        if request.POST['year']:
            year = request.POST.get('year')
        else:
            error = True
        if request.POST['item']:
            item = request.POST['item']
        else:
            error = True
        if request.POST['destination']:
            destination = request.POST['destination']
        else:
            error = True

        if error:
            context_dict['warning'] = "Your search didn't match any of the " \
                                          "available data. Please try again"
        else:
            context_dict['year'] = year
            context_dict['destination'] = destination

            exports = Export.objects.all().filter(year__year_code=year,
                                                  item__name__icontains=item,
                                                  destination__id=destination)
            context_dict['data'] = exports
            if len(exports)==0:
                context_dict['warning'] = "Your search didn't match any of the " \
                                          "available data. Please try again"

        return render(request, 'data/exports/export_search.html',context_dict)

    else:
        return render(request, 'data/exports/export_search.html',context_dict)

    
# Functions to generate views for import pages

def import_data(request):
    context_dict = {}
    import_form = ImportForm()
    if import_form:
        context_dict['form'] = import_form
    imports = Import.objects.values('year').annotate(import_amount=Sum(
        'Volume_in_tons'),
        import_usd=Sum(
        'cif_Value_in_usd'), import_etb=Sum('cif_Value_in_etb')).order_by(
        '-year')
    context_dict['data'] = imports

    return render(request, 'data/imports/import.html', context_dict)


def import_for_year(request, year, origin=None):
    context_dict = {}
    if origin is None:
        imports = Import.objects.filter(year=year)
        imports = imports.values('origin').annotate(cif_Value_in_usd=Sum(
            'cif_Value_in_usd'),Volume_in_tons=Sum('Volume_in_tons'),
                                                         cif_Value_in_etb=Sum('cif_Value_in_etb')).order_by('-cif_Value_in_usd')

        # replace origin id's with names
        for i in range(len(imports)):
            origin_id = imports[i]['origin']
            imports[i]['origin'] = Nation_Name(origin_id)


        context_dict['data'] = imports
        context_dict['year'] = year

        return render(request, 'data/imports/import_by_year.html', context_dict)
    else:
        imports = Import.objects.filter(year=year, origin__name_slug=origin)
        context_dict['data'] = imports
        context_dict['year'] = year
        country = Country.objects.filter(
            name_slug=origin)
        country_name = country[0].name
        context_dict['origin'] = country_name

        return render(request, 'data/imports/import_by_year_origin.html',
                      context_dict)


def import_by_item(request, item, origin=None):
    context_dict = {}
    if origin is None:
        imports = Import.objects.all().filter(item__name_slug=item).order_by(
            '-year','-cif_Value_in_usd')
        context_dict['item'] = item
        context_dict['data'] = imports

        return render(request, 'data/imports/import_by_item.html', context_dict)

    else:
        imports = Import.objects.all().filter(item__name_slug=item,
                                              origin__name_slug=origin).order_by(
            '-year','-cif_Value_in_usd')
        context_dict['item'] = item
        context_dict['data'] = imports
        context_dict['origin'] = origin

        return render(request, 'data/imports/import_by_item_origin.html',
                      context_dict)


def import_search(request):
    context_dict = {}

    form = ImportForm()
    context_dict['form'] = form
    error = False
    if request.method == 'POST':
        if request.POST['year']:
            year = request.POST.get('year')
        else:
            error = True
        if request.POST['item']:
            item = request.POST['item']
        else:
            error = True
        if request.POST['origin']:
            origin = request.POST['origin']
        else:
            error = True

        if error:
            context_dict['warning'] = "Your search didn't match any of the " \
                                          "available data. Please try again"
        else:
            context_dict['year'] = year
            context_dict['origin'] = origin

            imports = Import.objects.all().filter(year__year_code=year,
                                                  item__name__icontains=item,
                                                  origin__id=origin)
            context_dict['data'] = imports
            if len(imports)==0:
                context_dict['warning'] = "Your search didn't match any of the " \
                                          "available data. Please try again"

        return render(request, 'data/imports/import_search.html',context_dict)

    else:
        return render(request, 'data/imports/import_search.html',context_dict)




def test(request):
    zones = Zone.objects.all()

    for zone in zones:
        if zone.name_slug =="ethiopia":
            zone.geo_choices = "National"
            zone.save()


    # for i in range(len(countrys)):
    #     countrys[i]['name_slug'] = slugify(countrys[i]['name']).__str__()
    #     countrys[i].save()

    return HttpResponse("Saved")