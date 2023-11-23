from django.contrib.auth import authenticate
from django.core.checks import templates
from django.http import HttpResponse
from django.shortcuts import render, redirect
from adminapp.models import Admin


def function2(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def login(request):
    return render(request, "login.html")


def contact(request):
    return render(request, "contact.html")


def diwali(request):
    return render(request, "diwali.html")


def search(request):
    return render(request, 'search.html')


def MahaShivaratri(request):
    return render(request, 'MahaShivaratri.html')


def Lohri(request):
    return render(request, 'Lohri.html')


def Eid(request):
    return render(request, 'Eid.html')


def GaneshChaturthi(request):
    return render(request, 'GaneshChaturthi.html')


def GuruPurnima(request):
    return render(request, 'GuruPurnima.html')


def Holi(request):
    return render(request, 'Holi.html')


def Janmashtami(request):
    return render(request, 'Janmashtami.html')
