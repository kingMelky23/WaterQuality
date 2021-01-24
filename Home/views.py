from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Home index.")

def search(request, zipcode_id):
    response = "Zipcode searched: %s."
    return HttpResponse(response % zipcode_id)
