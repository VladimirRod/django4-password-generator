from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def generator(request):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('1234567890')
    special_symbols = list('!@#$%^&*()')
    password = ''
    length = int(request.GET.get('length'))
    if request.GET.get('upper'):
        alphabet.extend(uppercase)
    if request.GET.get('numbers'):
        alphabet.extend(numbers)
    if request.GET.get('special_symbols'):
        alphabet.extend(special_symbols)
    while len(password) != length:
        password += random.choice(alphabet)
    print(password)

    return render(request, 'generator/generator.html', {'password':password})
