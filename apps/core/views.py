from django.shortcuts import render
from django import forms
import requests
import json

class PostCity(forms.Form):
    city = forms.CharField(label='Enter City', max_length=100)

# def home(request, forecast):
#     form = PostCity()
#     forecast = get_location(request)
#     context = {
#         'forecast': forecast,
#         'form': form
#     }
#     return render(request, 'pages/home.html', context)

cindys_sun_info = "stuff about sun"

def about(request):
    context = {
        'text': cindys_sun_info     # may extend from template
    }

    return render(request, 'pages/about.html', context)

def get_location(request):
    path = 'https://weather.api.here.com/weather/1.0/report.json'
    app_id_str = '?app_id=LF6lB05BNhxMkZeX4gwP'
    app_code_str = '&app_code=0oEv8qe3sZdef3SclxN-lQ'
    product_str = '&product=forecast_astronomy'
    if request.method == 'POST':
        form = PostCity(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
        # city = request.POST.get('city')   # 'city' here should match the name on the form ie <input name="city"...>
            path = (path + app_id_str + app_code_str + product_str + '&name=' + city)
    else:
        form = PostCity()
    response = requests.get(path)
    forecast = json.loads(response.text)
    print(forecast)
    context = {
        'forecast': forecast,
        'form': form
    }
    return render(request, 'pages/home.html', context)
    # return forecast   



#incomplete/non-returned function that retrieves a list of Longitude/Latitute coordinates as non decimal numbers

def get_purpleair(request):
    path = 'https://www.purpleair.com/json'
    response = requests.get(path)
    purple_air_data = response.json()
    sensor_list = purple_air_data['results']
    # print(len(sensor_list))
    # # print(sensor_list)
    for sensor in sensor_list:
        print("Longitude: ", int(round(sensor["Lon"])))
        print("Latitude: ", int(round(sensor["Lat"])))
