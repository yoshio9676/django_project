from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db import IntegrityError
from .models import SnsModel
from .forms import SnsForm
from django.views.generic import CreateView


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

@login_required
def goodFunc(request, pk):
    object = SnsModel.objects.get(pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('sns_detail', pk=pk)

@login_required
def readFunc(request, pk):
    object = SnsModel.objects.get(pk=pk)
    username = request.user.get_username()
    readtext = object.readtext if object.readtext else ''
    
    if username in readtext:
        return redirect('sns_detail', pk=pk)
    else:
        object.read = object.read + 1
        object.readtext = readtext + ' ' + username
        object.save()
        return redirect('sns_detail', pk=pk)

class SnsCreate(LoginRequiredMixin, CreateView):
    template_name = "sns/create.html"
    model = SnsModel
    form_class = SnsForm
    success_url = reverse_lazy('sns_list')