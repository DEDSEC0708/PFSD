from django.urls import path
from . import views

urlpatterns = [
    path("adminhome", views.adminhome, name="adminhome"),
    path("adminlogout", views.logout, name="adminlogout"),
    path('signup', views.signup_page, name='signup'),  # Update this line
    path('login/', views.LoginPage, name='login'),
]
