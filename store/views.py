from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Brand,Category,Product
from .forms import RegistrationForm, LoginForm, EditProfileForm, ChangePasswordForm
# Create your views here.
def index(request):
    brands = Brand.get_all_brand()[:10]
    category = Category.get_all_category()
    products = Product.objects.all().order_by('-id')[:7]  
    
    return render(
        request,
        "store/index.html",
        {
            "brand": brands,
            "category": category,
            "products": products,
            
        },
    )
    

def clothes(request):
    return render(request, 'store/clothes.html')

def jeans(request):
    brands = Brand.get_all_brand()[:10]
    category = Category.get_all_category()
    products = Product.objects.all().order_by('-id')[:7]  
    
    return render(
        request,
        "store/jeans.html",
        {
            "brand": brands,
            "category": category,
            "products": products,
            
        },
    )
    
    

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
      

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, "store/edit_profile.html", {"form": form})

@login_required
def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data["old_password"]
            new_password = form.cleaned_data["new_password"]

            if not request.user.check_password(old_password):
                messages.error(request, "Old password is incorrect!")
            else:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user) 
                return redirect("profile")
    else:
        form = ChangePasswordForm()

    return render(request, "store/change_password.html", {"form": form})
