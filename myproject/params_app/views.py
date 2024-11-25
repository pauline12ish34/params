from django.shortcuts import render
from django.http import JsonResponse

# from django.http import HttpResponse
def home(request):
    return render(request,"index.html")
    # return HttpResponse("welcome to Django app")
def login(request):
   return render(request,"login.html")
def dashboard(request):
    return render(request, 'dashboard.html')
def dashboard_data(request):
    data = {
        "users": 140,
        "parkings": 140,
        "cars": 200,
    }
    return JsonResponse(data)