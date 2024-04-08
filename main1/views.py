from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Tutorial
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from . forms import NewUserForm
def homepage(request):
    return render(request=request,
                  template_name='main1/home.html',
                  context={'tutorials':Tutorial.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"NEW ACCOUNT CREATED :{username}")
            login(request, user)
            messages.info(request, f"You are now logged in as :{username}")
            return redirect("main1:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = NewUserForm
    return render(request,
                    "main1/register.html",
                    context={'form':form})
def logout_request(request):
    logout(request)
    messages.info(request, "Logged Out Successfully")
    return redirect("main1:homepage")
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                messages.info(request,f"You are now logged in as :{user.username}")
                return redirect("main1:homepage")
            else:
                messages.error(request,"INVALID USERNAME OR PASSWORD")
        else:
            messages.error(request,"INVALID USERNAME OR PASSWORD")

    form = AuthenticationForm
    return render(request,
                  "main1/login.html",
                  context = {"form":form})
