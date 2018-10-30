from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from django.core import serializers

def index(request):
    return render(request, "ajax_demo/index.html")

def all_json(request):
    users = User.objects.all()
    users_json = serializers.serialize("json", users)
    return HttpResponse(users_json, content_type="applications/json")

def all_html(request):

    users = User.objects.all()
    return render(request, "ajax_demo/all.html", {"users": users})

def find(request):
    users = User.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])
    print(users)
    return render(request, "ajax_demo/all.html", {"users": users})

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'], age=request.POST['age'])
    users = User.objects.order_by("-id")
    return render(request, "ajax_demo/all.html", {"users": users})
