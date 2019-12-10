from django.shortcuts import render
from django import forms
import requests
import json
# from PostCity.forms import PostCity

################# "enter city" form, class, render ###############################

class PostCity(forms.Form):
    city = forms.CharField(label='Enter City', max_length=50)


def get_location(request):
    path = 'https://weather.api.here.com/weather/1.0/report.json'
    app_id_str = '?app_id=LF6lB05BNhxMkZeX4gwP'
    app_code_str = '&app_code=0oEv8qe3sZdef3SclxN-lQ'
    product_str = '&product=forecast_astronomy'
    local_sunset = None
    local_sunrise = None
    if request.method == 'POST':
        form = PostCity(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            # 'city' here should match the name on the form ie <input name="city"...>
            city = request.POST.get('city')
            path = (path + app_id_str + app_code_str + product_str + '&name=' + city)
            response = requests.get(path)
            forecast = json.loads(response.text)
            local_sunrise = forecast['astronomy']['astronomy'][0]['sunrise']
            local_sunset = forecast['astronomy']['astronomy'][0]['sunset']
            #need to change 'Local' below to user input city
            print("Local Sunset: ", local_sunset)
            print("Local Sunrise: ", local_sunrise)
            #    where do we return the parameters local_sunset, local_sunrise?

    else:
        form = PostCity()


    context = {
        'local_sunrise': local_sunrise,
        'local_sunset': local_sunset,
        'form': form,
    }

    return render(request, 'pages/home.html', context)


################ AIRVISUAL GET AQI FUNCTION FROM IP ADDRESS ######################


def get_airquality(request):
    path = 'api.airvisual.com/v2/nearest_city?key={{SECRET_KEY}}'
    payload = {}
    headers = {}
    response = requests.request('GET', path, headers=headers, data = payload, allow_redirects=False, timeout=undefined)
    print(response.text)
    #aqi variable is written here
    aqi = response['forecasts'][0]['aqius']
    print(aqi)

    context = {
        'aqi': aqi,
    }

    return render(request, 'pages/home.html', context)



###################  OTHER HTML PAGE RENDERS #############################



def about(request):
    context = {
        'text': cindys_sun_info     # may extend from template
    }

    # cindys_sun_info = "stuff about sun"

    return render(request, 'pages/about.html', context)
