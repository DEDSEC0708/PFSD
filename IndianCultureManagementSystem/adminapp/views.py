from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import UserManager

from .models import User

def adminhome(request):
    return render(request, 'adminhome.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_page(request):
    if request.method == 'POST':
        full_name = request.POST.get('Full_Name')
        email = request.POST.get('E_mail')
        gender = request.POST.get('Gender')
        password = request.POST.get('password')

        # Check if any field is empty
        if not (full_name and email and gender and password):
            return HttpResponse("All fields are required. Please fill in all the details.")

        # Create the user using the UserManager
        user_manager = UserManager()
        new_user = user_manager.create_user(
            username=email,
            email=email,
            password=password,
            full_name=full_name,
            gender=gender
        )

        # Handle successful user creation and redirection
        return redirect('login')
    return render(request, 'signup.html')

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('E_mail')
        password = request.POST.get('password')

        if not (email and password):
            return HttpResponse("Both Email and password are required for login.")

        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            return redirect('home')  # Assuming 'home' is the URL for the home page
        else:
            return HttpResponse("Email or Password is incorrect.")

    return render(request, 'login.html')
