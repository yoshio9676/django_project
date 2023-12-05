from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import IntegrityError
from .models import SnsModel

# Create your views here.

# サインアップ
def signupFunc(request):
    if request.method == 'POST':
        # 登録処理
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.create_user(username, '', password)
            newuser = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, newuser)
                return redirect('sns_list')
            else:
                return render(request, 'sns/signup.html', {'error': 'このユーザーは既に登録されています。'})
        except IntegrityError:
            return render(request, 'sns/signup.html', {'error': 'このユーザーは既に登録されています。'})
    else:
        # ユーザー登録画面表示
        print('this is get method')
    return render(request, 'sns/signup.html')

# ログイン
def loginFunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sns_list')
        else:
            return render(request, 'sns/login.html', {'context': 'not logged in'})
    else:
        return render(request, 'sns/login.html')

# ログアウト
@login_required
def logoutFunc(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sns_login')
    else:
        return render(request, 'sns/logout.html')
    
# 投稿リスト
@login_required
def listFunc(request):
    object_list = SnsModel.objects.all()
    return render(request, 'sns/list.html', {'object_list': object_list})

# 投稿詳細
@login_required
def detailFunc(request, pk):
    object = get_object_or_404(SnsModel, pk=pk)
    return render(request, 'sns/detail.html', {'object': object})