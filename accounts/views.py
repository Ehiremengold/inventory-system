from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegForm


def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST or None)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('/')
    else:
        form = UserRegForm()
    context = {"form": form}
    return render(request, 'register.html', context)