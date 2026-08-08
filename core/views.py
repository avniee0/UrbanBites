from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import MenuItem, ContactMessage


# Home Page
def home(request):
    return render(request, 'home.html')


# Menu Page
def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {'items': items})


# About Page
def about(request):
    return render(request, 'about/about.html')


# Reservation Page
def reservation(request):
    return render(request, 'reservation/reservation.html')


# Contact Page
def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )

        messages.success(request, 'Message sent successfully.')
        return redirect('contact')

    return render(request, 'contact/contact.html')


# Register Page
def register(request):
    if request.method == "POST":

        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        first_name = fullname.split()[0]
        last_name = " ".join(fullname.split()[1:])

        User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "register/register.html")


# Login Page
def login_user(request):
    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")

        messages.error(request, "Invalid email or password.")

    return render(request, "login/login.html")


# Logout
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("home")