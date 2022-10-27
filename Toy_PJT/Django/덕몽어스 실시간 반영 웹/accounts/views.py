from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import CustomUserCreationForm
from .models import User
 
# Create your views here.
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person':person
    }
    return render(request, 'accounts/profile.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.win_cnt, user.lose_cnt, user.kill_cnt = 0, 0, 0
            user.save()
            user_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_login(request, form.get_user())
            return redirect('accounts:index')            
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    user_logout(request)
    return redirect('accounts:index')

def index(request):
    users = get_list_or_404(get_user_model())
    context = {
        'users':users
    }
    return render(request, 'accounts/index.html', context)

def follow(request, user_pk):
    if request.user.is_authenticated:
        me = request.user
        you = get_object_or_404(get_user_model(), pk=user_pk)
        if me != you:
            if you.followings.filter(pk=me.pk).exists():
                you.followings.remove(me)
                is_liked = False
            else:
                you.followings.add(me)
                is_liked = True
            context = {
                'is_liked': is_liked
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')

def plus(request, user_pk, target):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if target == 'win':
        person.win_cnt += 1
    elif target == 'lose':
        person.lose_cnt += 1
    else:
        person.kill_cnt += 1
    person.save()
    return redirect('accounts:profile', person.username)

def minus(request, user_pk, target):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if target == 'win':
        if person.win_cnt:
            person.win_cnt -= 1
    elif target == 'lose':
        if person.lose_cnt:
            person.lose_cnt -= 1
    else:
        if person.kill_cnt:
            person.kill_cnt -= 1
    person.save()
    return redirect('accounts:profile', person.username)

def reset(request, user_pk, target):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if target == 'win':
        if person.win_cnt:
            person.win_cnt = 0
    elif target == 'lose':
        if person.lose_cnt:
            person.lose_cnt = 0
    else:
        if person.kill_cnt:
            person.kill_cnt = 0
    person.save()
    return redirect('accounts:profile', person.username)
