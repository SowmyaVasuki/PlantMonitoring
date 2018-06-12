from django.http import HttpResponse
from . models import *
import json
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.template import loader

def welcome(request):
	template = loader.get_template('plant/welcome.html')
	context = {
		
	}
	return HttpResponse(template.render(context,request))

def dashboard(request,fid):

	try:
		x = Farmer.objects.get(farmerid=fid)
	except(KeyError, Farmer.DoesNotExist):
		template = loader.get_template('plant/welcome.html')
		context = {
		}
		return HttpResponse(template.render(context,request))

	if(x.farmerlogin_set.last().login==1):
		template = loader.get_template('plant/dashboard.html')
		if(x.plant_set.count()==0):
			lt=40.634112
			lg=-74.831944
		else:
			lt=x.plant_set.last().latitude
			lg=x.plant_set.last().longitude
		print('dash',lt,lg)
		context = {
			'name':x.First_name,
			'plants':x.plant_set.all(),
			'waterbodies': Water_Body.objects.all(),
			'stations':Weather_Station.objects.all(),
			'lat':lt,
			'long':lg,
			'farmer':fid,
		}
		return HttpResponse(template.render(context,request))
	else:
		template = loader.get_template('plant/welcome.html')
		context = {
		}
		return HttpResponse(template.render(context,request))
@csrf_exempt
def login(request):
	if request.method=='POST':
		try:
			x = Farmer.objects.get(username=request.POST['username'])
		except(KeyError, Farmer.DoesNotExist):
			template = loader.get_template('plant/farmer-login.html')
			context = {
					'IDinvalid':"Invalid Username, Did you register?",
				}
			return HttpResponse(template.render(context,request))
		if request.POST['password'] != x.password:
			template = loader.get_template('plant/farmer-login.html')
			context = {
					'Passwordinvalid':"Incorrect password!",
				}
			return HttpResponse(template.render(context,request))

		else:

			x.farmerlogin_set.create(farmerid=x.farmerid,login=1,time=timezone.now())
			template = loader.get_template('plant/farmer-login.html')
			context = {
					'Valid':"Proceed to Dashboard",
					'fid':x.farmerid
				}
			return HttpResponse(template.render(context,request))



	template = loader.get_template('plant/farmer-login.html')
	context = {
	}
	return HttpResponse(template.render(context,request))

def logout(request,fid):
		x = Farmer.objects.get(farmerid=fid)
		x.farmerlogin_set.create(farmerid=x.farmerid,login=0,time=timezone.now())
		return welcome(request)
@csrf_exempt
def register(request):
	#error checking
	if request.method=='POST':
		if(request.POST['Password']==request.POST['Again']):
			new = Farmer()
			new.First_name = request.POST['FirstName']
			new.Last_name = request.POST['LastName']
			new.username = request.POST['Username']
			new.password = request.POST['Password']
			new.farmerid = Farmer.objects.count() + 1
			new.save()

			template = loader.get_template('plant/farmer-register.html')
			context = {
				'dashboard':'Congratulations! You have been registered, please login.',
				'username': new.username,
			}
			return HttpResponse(template.render(context,request))
		
		else:
			template = loader.get_template('plant/farmer-register.html')
			context = {
				'error':'Password does not match,please try again!'
			}
			return HttpResponse(template.render(context,request))
		
	
	template = loader.get_template('plant/farmer-register.html')
	context = {
	}
	return HttpResponse(template.render(context,request))
@csrf_exempt
def addplant(request,fid):
	if request.method=='POST':
		p = Plant.objects.last()
		f = Farmer.objects.get(farmerid=fid)
		f.plant_set.create(
			name = request.POST['id'],
			latitude = request.POST['lat'],
			longitude = request.POST['log'],
			plant_id = p.plant_id +1,
			date_planted_on = timezone.now(),
			ws_id = 1
		)
		np = Plant.objects.last()
		np.actuator_set.create(plant_id=1)
		print('added')
		template = loader.get_template('plant/addplant.html')
		context = {
			'message':'Plant is added! Add another plant or close the window.',
			'farmer': fid,
		}
		return HttpResponse(template.render(context,request))

	else:

		template = loader.get_template('plant/addplant.html')
		context = {
			'message':'',
			'farmer': fid,
		}
		return HttpResponse(template.render(context,request))
@csrf_exempt
def control(request,pid):

	plant=Plant.objects.get(plant_id=pid)
	actuator=plant.actuator_set.last()
	if request.method=='POST':
		if request.POST['Status'] == 'Automatic':
			actuator.mode='Automatic'
		else:
			actuator.mode='Manual'
			actuator.status = request.POST['Status']
		actuator.save()
		print(request.POST['Status'])

	template = loader.get_template('plant/control.html')
	context = {
		'pid':pid,
		'a':actuator,
	}
	return HttpResponse(template.render(context,request))
def soil(request,pid):
	#print(pid)
	template = loader.get_template('plant/soil.html')
	context = {
		'plant':Plant.objects.get(plant_id=pid),
	}
	return HttpResponse(template.render(context,request))
def new(request):
	template = loader.get_template('plant/new.html')
	context = {
		'noplants': Plant.objects.count(),
		'plants':Plant.objects.all(),
		'waterbodies': Water_Body.objects.get(wb_id=1),
		'ws':Weather_Station.objects.get(ws_id=1),
	}
	return HttpResponse(template.render(context,request))
def wechart(request):
	template = loader.get_template('plant/wechart.html')
	context = {
		#'plant':Plant.objects.get(plant_id=pid),
		'station':Weather_Station.objects.get(ws_id=1),
	}
	return HttpResponse(template.render(context,request))
def wbchart(request):
	
	template = loader.get_template('plant/wbchart.html')
	context = {
		#'plant':Plant.objects.get(plant_id=pid),
		'wb':Water_Body.objects.get(wb_id=1),
	}
	return HttpResponse(template.render(context,request))
def madhu(request,pid):
	plant=Plant.objects.get(plant_id=pid)
	ws=Weather_Station.objects.get(ws_id=plant.ws_id)
	#actuator=Actuator.objects.get(plant_id=pid)
	actuator=plant.actuator_set.last()
	wb=Water_Body.objects.get(wb_id=actuator.wb_id)
	template = loader.get_template('plant/madhu.html')
	context = {

		'plant': plant,
		'weather_station': ws,
		'actuator': actuator,
		'water_body':wb,
		#'water_level':wl,
	}
	return HttpResponse(template.render(context,request))
def index(request):
	template = loader.get_template('plant/demo.html')
	context = {
		'noplants': Plant.objects.count(),
		'nowaterbodys': Water_Body.objects.count(),
		'noweathers': Weather_Station.objects.count(),
		'plants':Plant.objects.all(),
		'waterbodies': Water_Body.objects.all(),
		'stations':Weather_Station.objects.all(),
	}
	return HttpResponse(template.render(context,request))



def start(request):
	template = loader.get_template('plant/welcome.html')
	context = {
		'plants':Plant.objects.all(),
		'waterbodies': Water_Body.objects.all(),
		'stations':Weather_Station.objects.all(),
	}
	return HttpResponse(template.render(context,request))

def maps(request,pid):
	print(pid)
	template = loader.get_template('plant/maps.html')
	context = {
		'plants':Plant.objects.all(),
		'waterbodies': Water_Body.objects.all(),
		'weathers':Weather_Station.objects.all(),
	}
	return HttpResponse(template.render(context,request))	
def ws_dashboard(request,pid):
	print(pid)
	template = loader.get_template('plant/weather.html')
	context = {
		'ws':Weather_Station.objects.get(ws_id=pid),
	}
	return HttpResponse(template.render(context,request))	
def wb_illustration(request,pid):
	print(pid)
	template = loader.get_template('plant/water.html')
	context = {
		'wb':Water_Body.objects.get(wb_id=pid),
	}
	return HttpResponse(template.render(context,request))	
def update_climate(data):
	a=Weather_Station.objects.get(ws_id=data['climate'][0]['ws_id'])
	a.climate_set.create(temperature=data['climate'][1]['temp'],humidity=data['climate'][2]['humi'],raining=data['climate'][3]['raining'],time=timezone.now())
def update_waterlevel(data):
	a=Water_Body.objects.get(wb_id=data['waterlevel'][0]['wb_id'])
	b=data['waterlevel'][1]['waterlevel']
	if(b>100):
		b=100
	else:
		b=100-b
	a.water_level_set.create(water_level=b,time=timezone.now())
def update_soilmoisture(data):
	a=Plant.objects.get(plant_id=data['soilmoisture'][0]['plant_id'])
	a.soil_moisture_set.create(sm_value=data['soilmoisture'][1]['soilmoisture'],time=timezone.now())
def update_actuator(data):
	a=Actuator.objects.get(ac_id=data['actuator'][0]['ac_id'])
	if data['actuator'][1]['onoff']=='off':
		a.actuator_status_set.create(time=a.actuator_status_set.last().time,onoff='off')
	else:
		a.actuator_status_set.create(time=timezone.now(),onoff='on')

def all_pumps_info():
	pumps = Actuator.objects.all()
	info={}
	for pump in pumps:
		info[pump.pump_id] = [pump.mode,pump.status]
	print(info)
	return str(info)

@csrf_exempt
def update(request):
	if request.method=='POST':
		data=json.loads(request.body.decode("utf-8"))
		print('it was post requestas: '+str(data))

		if 'climate' in data:
			update_climate(data)
		if 'waterlevel' in data:
			update_waterlevel(data)
		if 'soilmoisture' in data:
			update_soilmoisture(data)
		if 'actuator' in data:
			update_actuator(data)

		return StreamingHttpResponse(all_pumps_info())
	return StreamingHttpResponse('it was GET request')