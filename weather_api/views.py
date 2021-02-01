from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def get_weather_for_city(request):
    return render(request, 'index.html')