from django.shortcuts import render

# Two example views. Change or delete as necessary.
def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

def get_location(request):
    path = 'https://weather.api.here.com/weather/1.0/report.json'
    app_id_str = '?app_id=LF6lB05BNhxMkZeX4gwP'
    app_code_str = '&app_code=0oEv8qe3sZdef3SclxN-lQ'
    product_str = '&product=forecast_astronomy'
    if request.method == 'POST':
        city_name = request.POST.get('city')   # 'city' should match the name on the form ie <input name="city"...>
        path = (path + app_id_str + app_code_str + product_str + '&name=' + city_name)
    response = requests.get(path)
    forecast = json.loads(response.text)
    context = {
        'forecast': forecast,
    }
    print(forecast)
    return render(request, 'jobsearch.html', context)   # change 'jobsearch' to whatever template


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
