"""
URL configuration for IndianCultureManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.function2, name="index"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("login", views.login, name="login"),
    path("contact", views.contact, name='contact'),
    path("diwali", views.diwali, name="diwali"),
    path("search", views.search, name="search"),
    path("eid", views.Eid, name="eid"),
    path("ganeshchaturthi", views.GaneshChaturthi, name="ganeshchaturthi"),
    path("janmashtami", views.Janmashtami, name="janmashtami"),
    path("mahashivaratri", views.MahaShivaratri, name="mahashivaratri"),
    path("gurupurnima", views.GuruPurnima, name="gurupurnima"),
    path("lohri", views.Lohri, name="lohri"),
    path("holi", views.Holi, name="holi"),

    path("", include("adminapp.urls")),
]
