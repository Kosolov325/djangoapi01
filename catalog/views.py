from logging import Logger
import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import admin
from .forms import CreateCar, CreateMarca
from .models import Car, Marca
import random


# Create your views here.
def viewIndex(request):
    cars = Car.objects.all()
    if cars.count() > 0:
        car  = random.choice(cars)
        return render(request,"index.html", {'randomCar':car})
    else:
        return render(request,"index.html", {'randomCar':None})

def viewAdmin(request):
    return redirect("admin")

#Create
def viewCreateCar(request):
    form = CreateCar(request.POST or None, request.FILES or None)
    if form.is_valid():
            form.save()
            return redirect('detail', id=form.instance.id)

    return render(request, "catalog/car.html", {"form":form})

def viewCreateMarca(request):
    form = CreateMarca(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('detailMarca', id=form.instance.id)
    
    return render(request, 'marca/marca.html', {"form":form})

#Read

def viewCatalog(request):
    cars = Car.objects.all()
    return render(request, "catalog/catalog.html",{'cars':cars})

def viewCar(request, id):
    cars = Car.objects.all()
    selectedCar  = get_object_or_404(Car, pk=id)
    return render(request, "catalog/detail.html", {"selectedCar":selectedCar, "id":id})


def view_Marcas(request):
    marcas = Marca.objects.all()
    return render(request, "marca/marcas.html", {"marcas":marcas})

def viewMarca(request, id):
    marcas = Marca.objects.all()
    selectedMarca = get_object_or_404(Marca, pk=id)
    return render(request, "marca/detail.html", {"selectedMarca":selectedMarca, "id":id})

#Update
def viewUpdateMarca(request, id):
    searchedMarca = get_object_or_404(Marca, pk=id)
    form = CreateMarca(request.POST or None, request.FILES or None, instance=searchedMarca)
    if form.is_valid():
        form.save()
        return redirect('deatailMarca', id=form.instance.id)
    
    return render(request, "marca/update.html", {"form":form})

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


def viewDeleteMarca(request, id):
    marcas = Marca.objects.all()

    selectedMarca = get_object_or_404(Marca, pk=id)
    selectedMarca.delete()

    return redirect('marcas')