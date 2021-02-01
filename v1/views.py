import requests

from django.shortcuts import render
from django.http import HttpResponse


API_KEY = '4fa02188ba9205a1f619645287c69336'

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
        post_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + API_KEY
        r = requests.get(post_url)
        print(r.json)
        return HttpResponse(r.content, status=200)
    return HttpResponse('POST requests are not allowed, try GET.', status=202)
