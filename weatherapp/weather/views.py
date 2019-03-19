from django.shortcuts import render
import requests
from .models import  city
from  .forms import Cityform

def index(request):

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1f2e989533864c217bef3ada1e9ddbe6'

    if request.method=='POST':
        form = Cityform(request.POST)
        form.save()
    form  = Cityform()

    cities = city.objects.all()

    weather_data = []
    for c in cities:
        r = requests.get(url.format(c)).json()

        city_weather = {
            'city' : c.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = {'weather_data': weather_data,'form':form}

    return render(request,'weather/weather.html',context)
