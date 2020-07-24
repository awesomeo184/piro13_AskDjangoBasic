from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from . models import Item
from .forms import ItemForm

def archives_year(request, year):
    return HttpResponse(f'{year}년도에 대한 정보')


def index(request):
    item_list = Item.objects.order_by('-created_at')
    content = {'item_list':item_list}
    return render(request, 'shop/item_lsit.html', content)

def detail(request, item_id):
    question = get_object_or_404(Item, id=item_id)
    content = {'question': question}
    return render(request, 'shop/detail.html', content)


# def item_new(request, item=None):
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES, instance=item)
#         if form.is_valid():
#             item = form.save()
#             return redirect(item)
#     else:
#         form = ItemForm(instance=item)

#     return render(request, 'shop/item_form.html', {
#         'form': form,
#     })


# def item_edit(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return item_new(request, item)

item_new = CreateView.as_view(model=Item, form_class=ItemForm)

item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)