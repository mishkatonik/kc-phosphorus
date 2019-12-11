from django.shortcuts import render
from django import forms
import requests
import json
# from PostCity.forms import PostCity

# ************************* "enter city" form, class, render ************************************

class PostCity(forms.Form):
    city = forms.CharField(label='Enter City', max_length=50)




def get_location(request):
    path = 'https://weather.api.here.com/weather/1.0/report.json'
    app_id_str = '?app_id=LF6lB05BNhxMkZeX4gwP'
    app_code_str = '&app_code=0oEv8qe3sZdef3SclxN-lQ'
    product_str = '&product=forecast_astronomy'
    local_sunset = None
    local_sunrise = None
    error_message = None
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
                print("Sunset", city, ":", local_sunset)
                print("Sunrise for", city, ":", local_sunrise)
                print(forecast)
                #    where do we return the parameters local_sunset, local_sunrise?

    else:
        form = PostCity()


    context = {
        'local_sunrise': local_sunrise,
        'local_sunset': local_sunset,
        'form': form,
        'error_message': error_message,
    }

    return render(request, 'pages/home.html', context)



####### AirVisual API, need to figure out how to pass city into it to get AQI ########

def get_airquality(request, city):
    path = "{{urlExternalAPI}}v2/city?city=Los Angeles&state=California&country=USA&key={{YOUR_API_KEY}}"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    aqi = response['forecasts'][0]['aqius']
    print(response.text.encode('utf8'))



###################  OTHER HTML PAGE RENDERS #############################



def about(request):
    context = {
        'text': "text"     # may extend from template
    }

    # cindys_sun_info = "stuff about sun"

    return render(request, 'pages/about.html', context)


