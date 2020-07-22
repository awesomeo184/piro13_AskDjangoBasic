from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse()


def archives_year(request, year):
    return HttpResponse(f'{year}년도에 대한 정보')