from email.policy import default
from logging import Logger
import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import admin
from .forms import CreateCar
from .models import Car
import random

# Create your views here.
def viewIndex(request):
    cars = Car.objects.all()
    car  = random.choice(cars)
    return render(request,"catalog/index.html", {'randomCar':car})

def viewAdmin(request):
    return redirect("admin")

#Create
def viewCreateCar(request):
    form = CreateCar(request.POST or None, request.FILES or None)
    if form.is_valid():
            form.save()
            return redirect('detail', id=form.instance.id)

    return render(request, "catalog/car.html", {"form":form})

#Read
def viewCatalog(request):
    cars = Car.objects.all()
    return render(request, "catalog/catalog.html",{'cars':cars})

def viewCar(request, id):
    cars = Car.objects.all()
    selectedCar  = get_object_or_404(Car, pk=id)
    return render(request, "catalog/detail.html", {"selectedCar":selectedCar, "id":id})

#Update
def viewUpdateCar(request, id):
    searchedCar = get_object_or_404(Car, pk=id)
    form = CreateCar(request.POST or None, request.FILES or None, instance=searchedCar)
    if form.is_valid():
        form.save()
        return redirect('detail', id=form.instance.id)
    
    return render(request, "catalog/update.html", {"form":form})

#Delete
def viewDeleteCar(request, id):
    cars = Car.objects.all()

    selectedCar = get_object_or_404(Car, pk=id)
    selectedCar.delete()

    return redirect('catalog')