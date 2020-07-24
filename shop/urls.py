from django.urls import path
from . import views
from .converters import FourDigitYearConverter
from django.urls import register_converter

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('archives/<yyyy:year>/', views.archives_year),
    path('<int:item_id>/', views.detail, name='detail'),
    path('new/', views.item_new, name='item_new'),
    path('<int:pk>/edit/', views.item_edit, name='item_edit'),

]