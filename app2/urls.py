from django.urls import path
from app2.views import *
app_name='aa'
urlpatterns=[
    path('venkey/',venkey,name='venkey'),
    path('venkey_1/',venkey_1,name='venkey_1'),
]