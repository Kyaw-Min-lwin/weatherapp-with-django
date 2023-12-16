from django.shortcuts import render, redirect
import requests
from .forms import cityForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = cityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['name']
            API = '4a56c3d5b17cbc8e082c506721b008aa'
            a = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API}')
            geoLocation = a.json()
            lat = geoLocation[0]['lat']
            lon = geoLocation[0]['lon']
            r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}")
            temp = r.json()
            content = {
                'city' : temp['name'],
                'weather' : temp['weather'][0]['description'],
                'temperature': temp['main']['temp'],
                'country_code' : temp['sys']['country'],
                'form': form
            }
            return render(request, 'index.html', content)
    else:
        form = cityForm()
        return render(request, 'index.html', {'form': form})