from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Post
from django.core import serializers

def index(request):
    return render(request, "ajax_post/index.html")

def create(request):
    Post.objects.create(content=request.POST['content'])
    posts = Post.objects.all()
    return render(request, "ajax_post/all.html", {"posts": posts})