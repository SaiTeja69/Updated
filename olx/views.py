from django.shortcuts import render,get_object_or_404
from post.models import post


def home(request):
    adds=post.objects.all()
    return render(request,'home.html',{'adds':adds})
