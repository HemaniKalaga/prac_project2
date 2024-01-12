from django.urls import path
from specific.views import *
app_name='specific'

urlpatterns=[
    path('page2/',page2,name='page2'),
]