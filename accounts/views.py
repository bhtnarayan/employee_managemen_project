from django.shortcuts import render, redirect 
from django.contrib.auth import login 
from django.urls import reverse 
from django.http import HttpResponse
from . forms import CustomUserCreationForm
from django.contrib.auth.models import User 
from . forms import EditProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "GET":
        context = {"form": CustomUserCreationForm}
        return render(request, "registration/register.html", context) 

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            return redirect("/main")

@login_required
def profile(request, pk = None):
    if pk:
        user = User.objects.get(pk = pk)
    else:
        user = request.user
    context = {'user': user }
    return render(request, 'registration/profile.html', context) 


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance = request.user) 

        if form.is_valid():
            form.save() 
            return redirect("/profile/") 
    else:
        form = EditProfileForm(instance = request.user) 
        context = {'form': form} 
        return render(request, 'registration/edit_profile.html', context) 

    return HttpResponse("<h2>Form is Not valid OR 404 error.</h2>")