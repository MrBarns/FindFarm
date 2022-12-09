from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .decorators import *

@unauthenticated
def RegisterView(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.email = user.email.lower()
            user.save()

            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, "Error occured during registration.\n \
            Please try again.")

    context = {'form' : form}
    return render(request, 'farm_app/register_user.html', context)

@unauthenticated
def LoginView(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                user = User.objects.get(email = email)
            except:
                messages.error(request, "User does not exist")
                return redirect('login')

            user = authenticate(request, email = email, password = password)

            if user:
                login(request, user)
                messages.success(request, "Login Successful")
                return redirect('home')

    context = {'form': form}
    return render(request, 'farm_app/login.html', context)

@login_required
def logoutView(request):
    logout(request)
    return redirect('login')

@login_required
@farmer_required
def createFarm(request):
    form = FarmForm(initial={'owner': request.user})

    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Farm added successfully")
            return redirect('home')
        else:
            messages.error(request, "Some error occured. Pls try again")
            return redirect('add_farm')

    context = {'form': form}
    return render(request, 'farm_app/create_farm.html', context)

@login_required
@farmer_required
def updateFarm(request, pk):
    farm = Farm.objects.get(id = pk)
    form = FarmForm(instance = farm)

    if request.method == 'POST':
        town_id = request.POST.get('town')
        town = Town.objects.get(id = town_id)

        farm.name = request.POST.get('name')
        farm.address = request.POST.get('address')
        farm.produce = request.POST.get('produce')
        farm.town = town
        farm.save()
        return redirect('farm', pk)

    context = {'form': form}
    return render(request, 'farm_app/create_farm.html', context)

login_required
@farmer_required
def deleteFarm(request, pk):
    farm = Farm.objects.get(id = pk)
    name = farm.name

    if request.method == 'POST':
        farm.delete()
        messages.success(request, f"{name} deleted successfully")
        return redirect('home')

    context = {'farm': farm}
    return render(request, 'farm_app/delete_farm.html', context)

@login_required
def farm(request, pk):
    farm = Farm.objects.get(id = pk)


    context = {'farm':farm}
    return render(request, 'farm_app/farm.html', context)

@login_required
def homeView(request):
    farms = Farm.objects.all()
    towns = Town.objects.all()


    context = {
        'farms': farms,
        'towns': towns
    }
    
    return render(request, 'farm_app/home.html', context)


# @login_required
