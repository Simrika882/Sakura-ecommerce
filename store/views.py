from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
# Create your views here.
def index(request):
    return render(request, "store/index.html")

def clothes(request):
    return render(request, 'store/clothes.html')

def jeans(request):
    return render(request, 'store/jeans.html')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)  
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("index")
            else:
                messages.success(request, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "store/login.html", {"form": form})


def signup(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")
    
    return render(request, "store/signup.html", {"form": form})


def logout(request):
    auth_logout(request)
    return redirect("index")

def shoes(request):
    return render(request, 'store/shoes.html')

def accessories(request):
    return render(request, 'store/accessories.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def profile(request):
    return render(request, 'store/profile.html')

def order(request):
    return render(request, 'store/order.html')
      