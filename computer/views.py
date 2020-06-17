from django.shortcuts import render, redirect
from . import models
from .forms import ComputerForm, BrandForm
from django.contrib import messages


# Create your views here.


def home(request):
    title = "Welcome to the world of GADGETS"
    template = 'computer/home.html'
    context = {"title": title}
    return render(request, template, context)


def gadget_list(request):
    title = "List of gadgets"
    gadgets = models.Computer.objects.all()
    template = 'computer/gadget_list.html'
    context = {
        "title": title,
        "gadgets": gadgets

    }
    return render(request, template, context)


def add_gadgets(request):
    title = "Add the Gadget"
    if request.method == "POST":
        form = ComputerForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Gadget added"))
        return redirect('list')
    else:
        form = ComputerForm()
    template = 'computer/addgadgets.html'
    context = {
        "title": title,
        "form": form
    }
    return render(request, template, context)


def add_brand(request):
    title = "Add New Brand"
    if request.method == "POST":
        form = BrandForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Brand Added"))
        return redirect('list')
    else:
        form = BrandForm()
    template = 'computer/add_brand.html'
    context = {
        "title": title,
        "form": form
    }
    return render(request, template, context)


def edit(request, id):
    title = "Edit the details"

    computer = models.Computer.objects.get(pk=id)
    form = ComputerForm(request.POST or None, instance=computer)
    if form.is_valid():
        form.save()
        messages.success(request, ("Details  Updated"))

        return redirect('list')

    template = 'computer/edit.html'
    context = {
        "title": title,
        "form": form
    }
    return render(request, template, context)


def delete(request, id):
    computer = models.Computer.objects.get(pk=id)
    computer.delete()
    return redirect('list')
