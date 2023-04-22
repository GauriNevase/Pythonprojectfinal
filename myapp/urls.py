from django.urls import path
from . import views

urlpatterns = [
    path('', views.sos,),
    path('sos', views.sos_details)
]
