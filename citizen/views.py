from django.shortcuts import render


def citizen_login(request):
    return render(request,"citizen_login.html")


def citizen_register(request):
    return render(request,"citizen_register.html")

