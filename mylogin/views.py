from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from spider.login_to_12306 import main


def index(request):
    return render(request, 'index.html')


def login_now(request):
    main()
    return render(request, 'index.html')
