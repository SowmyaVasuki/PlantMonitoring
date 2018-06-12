from django.db import models
from datetime import datetime

class Weather_Station(models.Model):
	name = models.CharField(max_length=250)
	ws_id = models.IntegerField(default=0)
	longitude = models.FloatField(default=0)
	latitude = models.FloatField(default=0)

	def __str__(self):
		return str(self.ws_id) + ' - ' + str(self.name)
	
class Climate(models.Model):
	ws_id = models.ForeignKey(Weather_Station, on_delete = models.CASCADE)
	raining = models.IntegerField(default=0)
	temperature = models.FloatField(default=0)
	humidity = models.FloatField(default=0)
	time = models.DateTimeField(default=datetime.now, blank =True)
	
	def __str__(self):
		return 'From ws_id: '+str(self.ws_id)

class Farmer(models.Model):
	First_name = models.CharField(max_length=250)
	Last_name = models.CharField(max_length=250)
	username = models.CharField(max_length=250,default='dhruv')
	farmerid = models.IntegerField(default=0)
	password = models.CharField(max_length=250)

	def __str__(self):
		return str(self.farmerid)+' - '+self.First_name

class Farmerlogin(models.Model):
	farmerid = models.ForeignKey(Farmer, on_delete = models.CASCADE,default=0)
	login = models.IntegerField(default=0)
	time = models.DateTimeField(default=datetime.now, blank =True)

	def __str__(self):
		return str(self.login)+' { '+str(self.farmerid)+' } '+str(self.time)

class Plant(models.Model):
	farmerid = models.ForeignKey(Farmer, on_delete = models.CASCADE,default=0)
	name = models.CharField(max_length=250)
	plant_id = models.IntegerField(default=0)
	ws_id = models.IntegerField(default=0)
	date_planted_on = models.DateTimeField(default=datetime.now, blank =True)
	longitude = models.FloatField(default=0)
	latitude = models.FloatField(default=0)

	def __str__(self):
		return str(self.plant_id)+' - '+self.name
	
class Soil_Moisture(models.Model):
	plant_id = models.ForeignKey(Plant, on_delete = models.CASCADE)
	
	sm_value = models.FloatField(default=0)
	time = models.DateTimeField(default=datetime.now, blank =True)
	
	def __str__(self):
		return 'To '+ str(self.plant_id)

class Actuator(models.Model):
	plant_id = models.ForeignKey(Plant, on_delete = models.CASCADE)
	wb_id = models.IntegerField(default=1)
	pump_id = models.IntegerField(default=1)
	mode = models.CharField(max_length=10,default='Automatic')
	status = models.CharField(max_length=10,default='OFF')
	time = models.DateTimeField(default=datetime.now, blank = True)
	def __str__(self):
		return 'From WBID :'+str(self.wb_id)+' To Plant_id :'+ str(self.plant_id)

class Water_Body(models.Model):
	name= models.CharField(max_length=250)
	wb_id = models.IntegerField(default=0)
	longituge = models.FloatField(default=0)
	latitude = models.FloatField(default=0)
	
	def __str__(self):
		return self.name + ' - ' + str(self.wb_id)

class Water_Level(models.Model):
	wb_id=models.ForeignKey(Water_Body, on_delete= models.CASCADE)
	
	water_level = models.FloatField(default=0)
	time= models.DateTimeField(default=datetime.now, blank = True)

	def __str__(self):
		return str(self.wb_id)+ ' - ' + str(self.water_level) + ' - ' +str(self.time)
