from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Zipcode


def index(request):
    zipcode_list = Zipcode.objects.order_by('entered')[:5]
    template = loader.get_template('Home/index.html')
    context = {
        'zipcode_list': zipcode_list,
    }
    return HttpResponse(template.render(context, request))


def search(request, zipcode_id):
    response = "Zipcode searched: %s."
    return HttpResponse(response % zipcode_id)
