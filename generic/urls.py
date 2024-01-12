from django.urls import path
from generic.views import *
app_name='generic'

urlpatterns=[
    path('page1/',page1,name='page1'),
]