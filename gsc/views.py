from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
#from paste.wsgiwrappers import settings

from .models import users
from .models import website
# from .forms import websiteForm
import psycopg2
from django.contrib.auth.models import User, auth

import google.oauth2.credentials
import google_auth_oauthlib.flow
from apiclient import errors
from apiclient.discovery import build


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


def viewsites(request):
    sites = website.objects.filter(user_id=request.user.id)
    print('############################################')
    return render(request, 'gsc/viewsites.html', {'websites': sites})


def signup(request):
    return render(request, 'gsc/signup.html')


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
    selected_site = request.POST['website']
    return render(request, 'gsc/letsstart.html', {'website': selected_site})


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


def signin_action(request):
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


# adding the website to application

def addsite_action(request):
    web_name = request.POST['web_name']
    website_url = request.POST['website_url']
    website_obj = website(web_name=web_name, website_url=website_url, user_id=request.user.id)
    website_obj.save()
    return render(request, 'gsc/index.html')


def authorize(request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
        ['https://www.googleapis.com/auth/webmasters.readonly'])
    flow.redirect_uri = 'http://we5.com:8000/oauth2callback'
    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')

    # redirect user to authorization_url
    return redirect(authorization_url)


def handleOAuth2Callback(request):
    state = request.GET.get('state', '')
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
        scopes=['https://www.googleapis.com/auth/webmasters.readonly'], state=state)
    flow.redirect_uri = 'http://we5.com:8000/oauth2callback'
    url = request.build_absolute_uri().replace('http:', 'https:')
    print(url)
    flow.fetch_token(authorization_response=url)

    credentials = flow.credentials
    storeThisAgainstUser = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes}
    print( storeThisAgainstUser )

def scheduledTask():

    # for user in users:
    # fetch users credentials from database
    credentials = {}

    webmasters_service = build('webmasters', 'v3', http=http, credentials=credentials)

    # Retrieve list of properties in account
    site_list = webmasters_service.sites().list().execute()