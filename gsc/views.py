from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# mapping the first page.

def index(request):
    return render(request, 'gsc/index.html')


def about(request):
    return render(request, 'gsc/about.html')


def signup(request):
    if request.method=='POST':
        email=request.POST['email']

    return render(request, 'gsc/signup.html')


def signin(request):
    return render(request, 'gsc/signin.html')


def addsite(request):
    return render(request, 'gsc/addsite.html')


def documentation(request):
    return render(request, 'gsc/documentation.html')


def letsstart(request):
    return render(request, 'gsc/letsstart.html')


def visualize(request):
    return render(request, 'gsc/visualize.html')
