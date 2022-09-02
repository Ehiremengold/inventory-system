from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from app.forms import LaptopForm, MobileForm, DesktopForm
from app.models import Laptop, Desktop, Mobile


@login_required
def index(request):
    context = {
        "laptops": Laptop.objects.all(),
        "desktops": Desktop.objects.all(),
        "mobile": Mobile.objects.all(),
    }
    return render(request, 'index.html', context)


def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        "header": "Laptops",
    }
    return render(request, 'index.html', context)


def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        "header": "Desktops",
    }
    return render(request, 'index.html', context)


def display_mobile(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        "header": "Mobile",
    }
    return render(request, 'index.html', context)


def add_laptop(request):
    if request.method == "POST":
        form = LaptopForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LaptopForm()
    return render(request, "add_new.html", {"form": form, "header": "Laptop"})


def add_desktop(request):
    if request.method == "POST":
        form = DesktopForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DesktopForm()
    return render(request, "add_new.html", {"form": form, "header": "Desktop"})


def add_mobile(request):
    if request.method == "POST":
        form = MobileForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MobileForm()
    return render(request, "add_new.html", {"form": form, "header": "Mobile"})


def edit_laptop(request, pk):
    item = get_object_or_404(Laptop, pk=pk)
    if request.method == "POST":
        form = LaptopForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LaptopForm(instance=item)

        return render(request, 'edit_item.html', {"form": form, "header": "Laptop"})


def edit_desktop(request, pk):
    item = get_object_or_404(Desktop, pk=pk)
    if request.method == "POST":
        form = DesktopForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DesktopForm(instance=item)

        return render(request, 'edit_item.html', {"form": form, "header": "Desktop"})


def edit_mobile(request, pk):
    item = get_object_or_404(Mobile, pk=pk)
    if request.method == "POST":
        form = MobileForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MobileForm(instance=item)

        return render(request, 'edit_item.html', {"form": form, "header": "Mobile"})


def delete_laptop(request, pk):
    Laptop.objects.filter(id=pk).delete()
    items = Laptop.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


def delete_desktop(request, pk):
    Desktop.objects.filter(id=pk).delete()
    items = Desktop.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


def delete_mobile(request, pk):
    Desktop.objects.filter(id=pk).delete()
    items = Mobile.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)
