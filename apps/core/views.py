from django.shortcuts import render, redirect
from django import forms
import requests
import json
import environment


class PostCity(forms.Form):
    city = forms.CharField(label="ENTER A CITY", max_length=255)




def get_location(request):
    path = 'https://weather.api.here.com/weather/1.0/report.json'
    app_id_str = '?app_id=LF6lB05BNhxMkZeX4gwP'
    app_code_str = '&app_code=0oEv8qe3sZdef3SclxN-lQ'
    product_str = '&product=forecast_astronomy'
    local_sunset = None
    local_sunrise = None
    error_message = None
    local_ip_aqi = None

    if request.method == 'POST':
        form = PostCity(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            # 'city' here should match the name on the form ie <input name="city"...>
            city = request.POST.get('city')
            path = (path + app_id_str + app_code_str + product_str + '&name=' + city)
            response = requests.get(path)
            forecast = json.loads(response.text)

            if 'Message' in forecast:
                error_message = 'Hmm, looks like this city doesn\'t exist. Did you enter it correctly?'
            else:
                local_sunrise = forecast['astronomy']['astronomy'][0]['sunrise']
                local_sunset = forecast['astronomy']['astronomy'][0]['sunset']
                #need to change 'Local' below to user input city
                # print("Sunset", city, ":", local_sunset)
                # print("Sunrise for", city, ":", local_sunrise)
                # print(forecast)
                local_ip_aqi = get_airquality(request)
    else:
        form = PostCity()


    context = {
        'local_sunrise': local_sunrise,
        'local_sunset': local_sunset,
        'local_ip_aqi': local_ip_aqi,
        'form': form,
        'error_message': error_message,
    }

    return render(request, 'pages/home.html', context)


################ AIRVISUAL GET LOCAL AQI BASED ON IP ADDRESS ##############


def get_airquality(request):
    path = "https://api.airvisual.com/v2/nearest_city?key={}".format(environment.SECRET_KEY)
    payload = {}
    headers = {}
    response = requests.request('GET', path, headers=headers, data = payload, allow_redirects=False)
    text_response = response.text
    local_ip_aqi = json.loads(text_response)['data']['current']['pollution']['aqius']
    print('LOCAL AQI', local_ip_aqi)

    return local_ip_aqi



###################  OTHER HTML PAGE RENDERS #############################
def login(request):
    context = {
        '': ''
    }

    return render(request, 'pages/login.html', context)

def about(request):
    context = {}

    return render(request, 'pages/about.html', context)
