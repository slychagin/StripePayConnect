from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')
