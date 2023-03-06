from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'blog/index.html')

def posts(request):
    title ='this is a test'
    return render(request,'blog/posts.html')

def post_detail(request):
    pass
