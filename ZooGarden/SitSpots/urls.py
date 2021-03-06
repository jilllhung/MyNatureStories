from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('zooGarden', views.zooGarden),
    path('africaGarden', views.africaGarden),
    path('australiaGarden', views.australiaGarden),
    path('southAmericaGarden', views.southAmericaGarden),
    path('northAmericaGarden', views.northAmericaGarden),
    path('bajaCaliforniaGarden', views.bajaCaliforniaGarden), 
    path('californiaGarden', views.californiaGarden),
    path('sitspots/zoogarden/ajax', views.zGardenAjax),
    path('findYourSitSpot', views.findYourSitSpot),
    path('about', views.about),
    path('contact', views.contact),
]