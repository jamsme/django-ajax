from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from django.core import serializers

def index(request):
    return render(request, "ajax_pagination/index.html")

def look(request):
    users = User.objects.filter(first_name__startswith=request.POST['first_name_starts_with']).filter(created_at__gte=request.POST['created_at_starts_with']).filter(created_at__lte=request.POST['created_at_ends_with'])
    return render(request, "ajax_pagination/user.html", {"users": users})
