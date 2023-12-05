from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from .models import SnsModel

# Create your views here.

def signupFunc(request):
    if request.method == 'POST':
        # 登録処理
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.create_user(username, '', password)
        except IntegrityError:
            return render(request, 'sns/signup.html', {'error': 'このユーザーは既に登録されています。'})
    else:
        # ユーザー登録画面表示
        print('this is get method')
    return render(request, 'sns/signup.html')

def loginFunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'sns/login.html', {'context': 'logged in'})
        else:
            return render(request, 'sns/login.html', {'context': 'not logged in'})
    else:
        return render(request, 'sns/login.html')
    
def logoutFunc(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sns_login')
    else:
        return render(request, 'sns/logout.html')
    
def listFunc(request):
    object_list = SnsModel.objects.all()
    return render(request, 'sns/list.html', {'object_list': object_list})