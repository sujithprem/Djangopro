from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def signup_handler(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confrimpassword = request.POST.get("confirm-password")
        if password == confrimpassword:
            if User.objects.filter(username=username).exists():
                return redirect("signup")
            elif User.objects.filter(email=email).exists():
                return redirect("signup")
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                return redirect("login")
        else:
            return redirect("signup")


def login_handler(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            return redirect("signup")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("/admin/")
            else:
                return redirect("shop")
        else:
            return redirect("login")

