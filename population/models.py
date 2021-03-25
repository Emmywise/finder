from django.db import models

# Create your models here

class building_data (models.Model): #model to take in building datas from csv file
    name = models.CharField(max_length=30)
    id=models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class meter_data(models.Model): #model to take in meters datas from csv file
    building_id = models.CharField(max_length=30)
    fuel = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    id=models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.fuel +" "+ self.unit


class hourly_data(models.Model): # model to take in halfhour datas from csv file
    consumption = models.CharField(max_length=30)
    meter_id = models.CharField(max_length=30)
    reading_date_time = models.CharField(max_length=30)

    def __str__(self):
        return ("power consumed:"+str(self.consumption) +"    "+ "date:"+" "  + str(self.reading_date_time))


