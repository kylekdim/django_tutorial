from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Kyle Kisun Chang / d645920e is the polls index.")
