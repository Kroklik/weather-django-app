from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import render, redirect
from .weather_parser import weather_parser

User = get_user_model()


def index(request):
    queryset = weather_parser()
    context = {
        'title': 'Главная страница',
        'weather_infos': queryset
    }
    return render(request, 'main_pages/index.html', context)
