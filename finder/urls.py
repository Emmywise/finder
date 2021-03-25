"""finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from population.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_buildings/', upload_buildings, name="upload_buildings"),
    path('upload_meters/', upload_meters, name="upload_meters"),
    path('upload_halfHour/', upload_halfHour, name="upload_halfHour"),
    path('consumption_chart/', ChatbarView.as_view(), name='consumption_chart'),
    path('building_chart/', ChatbarBuildingView.as_view(), name='building_chart'),
    path('meter_chart/', ChatbarMeterView.as_view(), name='meter_chart')
]
