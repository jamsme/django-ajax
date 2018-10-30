from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core import serializers
from django.http import JsonResponse

def index(request):
    all_users = User.objects.all()
    return render(request, "ajax_search/index.html", {"all_users": all_users})

def create(request):
    p = request.POST

    if request.method == 'POST':
        error_messages = []

        if len(p['first_name']) < 3:
            error_messages.append("First name longer...")

        if len(p['last_name']) < 3:
            error_messages.append("Last name longer...")

        if len(p['image']) < 5:
            error_messages.append("C'mon real url..")

        if error_messages:
            return JsonResponse({'errors': error_messages}, status=400)

        else:
            users = User.objects.create(first_name=p['first_name'], last_name=p['last_name'], gender=p['gender'], image=p['image'], sport=p['sport'])
            print(users.__dict__)

        return redirect('/ajax_search')

def get(request):
    users = User.objects.filter(id__lte=request.POST['first_name'])
    return render(request, "ajax_search/search.html", {'users': users})

def filter(request):
    users = User.objects.filter(first_name__startswith=request.POST['first_name']).filter(gender__contains=request.POST['gender']).filter(sport__contains=request.POST['sport'])
    return render(request, "ajax_search/filter.html", {'users': users})


    