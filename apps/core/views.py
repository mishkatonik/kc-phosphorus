from django.shortcuts import render
from tests import heremaps_data
import suntime_adjust

# Pulls data from data structure to template
def reminder_time(request):
    sunrise = heremaps_data["astronomy"]["astronomy"][0]["sunrise"]
    sunset = heremaps_data["astronomy"]["astronomy"][0]["sunset"]
    print("Sunrise - - - - - ", sunrise)
    print("Sunset - - - - - ", sunset)

    context = {
        'sunrise': sunrise,
        'sunset': sunset,
        'sun_time': 'COMING SOON',  # results from suntime_adjust
    }

    return render(request, 'pages/home.html', context)


# Two example views. Change or delete as necessary.
def home(request):
    context = {
        'example_context_variable': 'Change me.',
        'sun_time': 'COMING SOON'   # use here maps reference for times
    }

    return render(request, 'pages/home.html', context)


cindys_sun_info = "stuff about sun"

def about(request):
    context = {
        'text': cindys_sun_info     # may extend from template
    }

    return render(request, 'pages/about.html', context)
