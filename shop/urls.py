from django.urls import path
from . import views
from .converters import FourDigitYearConverter
from django.urls import register_converter

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('archives/<year:yyyy>', views.archives_year)
]