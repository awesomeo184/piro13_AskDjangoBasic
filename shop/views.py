from django.http import HttpResponse
from django.shortcuts import render
from . models import Item

def archives_year(request, year):
    return HttpResponse(f'{year}년도에 대한 정보')


def index(request):
    item_list = Item.objects.order_by('-created_at')
    content = {'item_list':item_list}
    return render(request, 'shop/item_lsit.html', content)