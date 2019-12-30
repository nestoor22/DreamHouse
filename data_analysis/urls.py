from django.urls import path
from data_analysis.views import *

urlpatterns = [
    path(r'', index, name='data_analytics'),
]