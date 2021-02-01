import requests

from django.shortcuts import render
from django.http import HttpResponse


API_KEY = '1c0bed04fed1f0a7b3b106ca6ae717a6'

def weather(request):
    '''
        Returns weather information as a JSON repsonse

        Required params: City name(str)
    '''
    if request.method == 'GET':
        try:
            city = request.GET['city']
        except Exception as e:
            return HttpResponse('Search parameter ' + str(e) + ' required.' , status=202)
        if not city:
            return HttpResponse('Please provide a city name.', status=202)
        # make OpenWeatherMap API request
        post_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + API_KEY + '&unit=metric'
        r = requests.get(post_url)
        return HttpResponse(r.content, status=200)
    return HttpResponse('POST requests are not allowed, try GET.', status=202)
    