from ast import Add
from multiprocessing import context
from xml.etree.ElementTree import Comment
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from requests import request

from custom_user.models import MyUser
from .forms import CommentForm, EditForm, LoginForm, RegisterForm, Work
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import AddWork, Comment
from django.core.paginator import Paginator


# Create your views here.

@login_required()
def home(request):
    # user = MyUser.objects.filter()
    total_data = AddWork.objects.count()
    works = AddWork.objects.filter(author=request.user).order_by('id')[:6]
    context = {
        'works': works,
        'total-data': total_data,


    }

    return render(request, 'homepage.html', context)


def register(request):
    context = {
        'form': RegisterForm
    }

    if request.method == 'POST':
        form = RegisterForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            newUser = User(username=username)
            newUser.set_password(password)

            newUser.save()
            messages.info(request, 'Registered is success!')
            return redirect('register')
        else:
            messages.info(request, 'Pasword is wrong')
            return redirect('register')

    return render(request, 'register.html', context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'User is undefined')
            return render(request, 'login.html', context)
        messages.info(request, 'Logined is success!')
        login(request, user)
        return redirect('home')
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'Logout is success!')
    return redirect('login')


@login_required(login_url="user:login")
def addwork(request):

    context = {
        'form': Work()
    }

    if request.method == 'POST':
        form = Work(request.POST or None, request.FILES or None)
        if form.is_valid():
            work = form.save(commit=False)
            work.author = request.user
            work.save()
            messages.success(request, 'Work was added sucessfully!')
            return redirect('home')
    return render(request, 'work.html', context)


@login_required(login_url="user:login")
def mywork(request):

    works = AddWork.objects.filter(author=request.user)
    pagination = Paginator(works, 2)
    page_num = request.GET.get('page')
    page = pagination.get_page(page_num)
    context = {
        'works': works,
        'form': Work(),
        'count': pagination.count,
        'page': page
    }
    if request.method == 'POST':
        form = Work(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'mywork.html', context)


# @login_required(login_url='user:login')
# def editProfile(request):
#     form = EditForm(instance=request.user)
#     context = {
#         'form': form
#     }

#     messages.info(request,'Profile is updated!')
#     return render(request, 'edit.html', context)


@login_required(login_url="user:login")
def project_details(request, id):

    data = AddWork.objects.filter(id=id)
    context = {
        'data': data
    }
    return render(request, 'project_details.html', context)


@login_required(login_url="user:login")
def update(request, id):
    works = get_object_or_404(AddWork, id=id)
    form = Work(request.POST or None, request.FILES or None, instance=works)
    context = {

        'form': form
    }
    if form.is_valid():
        works = form.save(commit=False)
        works.author = request.user

        works.save()
        messages.success(request, 'Works is updated')
        return redirect('home')

    return render(request, 'update.html', context)


@login_required(login_url='user:login')
def delete(request, id):
    works = get_object_or_404(AddWork, id=id)
    works.delete()
    messages.success(request, 'Work is deleted!')
    return redirect('home')


def about(request):
    return render(request, 'about_us.html')


@login_required(login_url="user:login")
def portfolio(request):
    data = AddWork.objects.filter(author=request.user)
    context = {
        'data': data
    }

    return render(request, 'portfolio.html', context)


def whatwedo(request):
    return render(request, 'whatwedo.html')


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    comment = Comment.objects.filter()
    context = {
        'comment':comment,
        'form':CommentForm(instance=request.user)
    }
    if request.method == 'POST':
        form = CommentForm(request.Post or None)
        if form.is_valid():
            form.save()
            messages.info(request,'added!')
            return redirect('home')

    return render(request, 'blog_details.html',context)


def contact(request):
    return render(request, 'contact.html')


def editProfile(request):
    user = MyUser.objects.filter()
    context = {
        'form': EditForm(instance=request.user),
        'user': user
    }
    if request.method == 'POST':
        form = EditForm(request.POST or None,
                        request.FILES or None, instance=request.user)
        if form.is_valid():
            print(form)
            form.save()
            messages.info(request, 'Profile is updated!')
            return redirect('home')

    return render(request, 'edit.html', context)
