import requests

from django.shortcuts import render
from django.http import HttpResponse


API_KEY = '4fa02188ba9205a1f619645287c69336'

def weather(request):
    if request.method == 'GET':
        city = 'toronto'
        post_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + API_KEY
        r = requests.get(post_url)
        print(r.json)
        return HttpResponse(r.content, status=200)
    return HttpResponse('POST requests are not allowed, try GET.', status=202)

