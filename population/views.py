from django.shortcuts import render
import os
import csv, io
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import *
from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
import pandas as pd
import json
from django.views.generic import TemplateView

# @permission_required('admin.an_add_log_entry') #mean the superuser should have access to this upload not just any user
def upload_buildings(request):
    template = "building.html"
    if request.method =="GET":
        return render(request, template)
    csv_file = request.FILES['file'] #get the file
    if not csv_file.name.endswith('.csv'): #check user upload only csv file format is allowed
        message.error(request, 'This is not a csv file, upload a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set) #loop through data to be string
    next(io_string) #skip the first line which is the header
    for colum in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = building_data.objects.update_or_create(
            id=colum[0],
            name=colum[1],     
        )
    context = {}
    return render(request, template, context)


def upload_meters(request):
    template = "meter.html"
    if request.method =="GET":
        return render(request, template)
    csv_file = request.FILES['file'] #get the file
    if not csv_file.name.endswith('.csv'): #check user upload only csv file format is allowed
        message.error(request, 'This is not a csv file, upload a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set) #loop through data to be string
    next(io_string) #skip the first line which is the header
    for colum in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = meter_data.objects.update_or_create(
            building_id=colum[0],
            id=colum[1],
            fuel=colum[2],
            unit=colum[3],
        )
    context = {}
    return render(request, template, context)


def upload_halfHour(request): #fucntion that fetch the datas from haflhour consumption csv file to the datbase
    template = "halfHour.html"
    if request.method =="GET":
        return render(request, template)
    csv_file = request.FILES['file'] #get the file
    if not csv_file.name.endswith('.csv'): #check user upload only csv file format is allowed
        message.error(request, 'This is not a csv file, upload a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set) #loop through data to be string
    next(io_string) #skip the first line which is the header
    for colum in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = hourly_data.objects.update_or_create(
            consumption=colum[0],
            meter_id=colum[1],
            reading_date_time=colum[2],
        )
    context = {}
    return render(request, template, context)

class ChatbarView(APIView): #class function that fetch datas from the database to the screen

    def get(self,  request, format=None):
        template_name = "halfHour.html"
        qs=hourly_data.objects.all()
        labels = []
        data = []
        for item in qs:
            labels.append(item.reading_date_time)
            data.append(item.consumption)
        data={
            'labels': labels,
            'data': data,   
        }
        return Response(data)


class ChatbarBuildingView(APIView): #class function that fetch datas from the building database and display a chart to the screen
    def get(self,  request, format=None):
            template_name = "building.html"
            qs=building_data.objects.all()
            labels = []
            data = []
            for item in qs:
                labels.append(item.name)
                data.append(item.id)
            data={
                'labels': labels,
                'data': data,        
            }  
            return Response(data)

class ChatbarMeterView(APIView): #class function that fetch datas from the meter consumption database and display a chart to the screen

    def get(self,  request, format=None):
            template_name = "meter.html"
            qs=meter_data.objects.all()
            labels = []
            data = []
            for item in qs:
                labels.append(item.fuel)
                data.append(item.id)
            data={
                'labels': labels,
                'data': data,
            }
            return Response(data)

