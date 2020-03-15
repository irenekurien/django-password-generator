from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'Generator/home.html')


def about(request):
    return render(request, 'Generator/about.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHOJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length', 12))  # 12 is thw default length

    my_password = ''
    for x in range(length):
        my_password += random.choice(characters)

    return render(request, 'Generator/password.html', {'password': my_password})
