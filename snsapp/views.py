from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def getSns(request):
    return HttpResponse('<h1>SNS Page</h1>')

def signupFunc(request):
    return render(request, 'sns/signup.html', {
        'some': 'some string'
    })