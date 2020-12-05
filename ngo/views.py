from django.shortcuts import render

# Create your views here.
def ngo_login(request):
    return render(request,"ngo_login.html")
