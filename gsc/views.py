from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import users
import psycopg2
from django.contrib.auth.models import User, auth


# from tkinter import tkinter
# import tinker.messagebox


def popmsg(msg):
    window.Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()
    if messagebox.askyesno('question', msg, icon='error') == True:
        print('Yes')
    else:
        print('no')

    window.deiconify()
    window.destroy()
    window.quit()


# Create your views here.
# mapping the first page.

def index(request):
    return render(request, 'gsc/index.html')


def about(request):
    return render(request, 'gsc/about.html')


def signup(request):
    return render(request, 'gsc/signup.html')


def signin_action(request):

    #if request.method == 'post':
    if True:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            return render(request, 'gsc/index.html')
        else:
            messages.info(request, 'invalid credentials')
            ##################pop up msg
            return render(request, 'gsc/signin.html')


def signin(request):
    return render(request, 'gsc/signin.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def addsite(request):
    return render(request, 'gsc/addsite.html')


def documentation(request):
    return render(request, 'gsc/documentation.html')


def letsstart(request):
    return render(request, 'gsc/letsstart.html')


def visualize(request):
    return render(request, 'gsc/visualize.html')


def graph(request):
    return render(request, 'gsc/graph.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['org_name']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['repassword']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Already exists')
                return render(request, 'gsc/signup.html')
            else:
                user = User.objects.create_user(password=password, first_name=name, username=username, email=username)
                user.save()
        else:
            print('pop up')
        return redirect('/')
    else:
        return render(request, 'gsc/index.html')
